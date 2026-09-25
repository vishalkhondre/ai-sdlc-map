"""Browser regressions. Build first; requires Playwright Chromium.

Run explicitly (also required by CI): python scripts/check_browser.py
The ordinary unit suite remains runnable without a browser installation.
"""
from __future__ import annotations

import functools
import http.server
import os
import re
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


PAGES = ["index.html", "workflow-catalog.html", "glossary.html", "references.html", "404.html"]
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"]


def accessibility(browser, base):
    """D-020: axe on every page in both themes and at desktop and phone widths, plus the layout's
    own promises: skip link, labelled landmarks, aria-current, drawer, visible focus, reduced motion."""
    from axe_playwright_python.sync_playwright import Axe
    axe = Axe()
    for scheme in ("light", "dark"):
        for width in (1440, 390):
            page = browser.new_page(color_scheme=scheme, viewport={"width": width, "height": 900})
            for name in PAGES:
                page.goto(f"{base}/{name}")
                page.wait_for_timeout(150)
                found = axe.run(page, options={"runOnly": {"type": "tag", "values": AXE_TAGS}}).response["violations"]
                assert not found, (scheme, width, name, [(v["id"], [n["target"] for n in v["nodes"][:3]]) for v in found])
            page.goto(f"{base}/workflow-catalog.html")
            page.locator(".wf-card").first.click()
            page.locator("#wf-detail").wait_for(state="visible")
            found = axe.run(page, options={"runOnly": {"type": "tag", "values": AXE_TAGS}}).response["violations"]
            assert not found, (scheme, width, "workflow detail", [(v["id"], [n["target"] for n in v["nodes"][:3]]) for v in found])
            page.close()

    import json
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    import page_text
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    expected = json.loads(page_text.RENDERED.read_text(encoding="utf-8"))["workflow-catalog.html"]
    assert page_text.catalog_rendered(page, base) == expected, "the catalog's rendered text changed"
    for name in PAGES:
        page.goto(f"{base}/{name}")
        for nav in page.locator("nav").all():
            assert nav.get_attribute("aria-label"), f"{name}: every nav landmark is labelled"
        assert page.locator("main").count() == 1, name
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        style = page.evaluate("(() => { const s = getComputedStyle(document.activeElement); return [s.outlineStyle, s.outlineWidth]; })()")
        assert style[0] != "none" and style[1] not in ("0px", ""), (name, "focus is visible", style)
    page.goto(base + "/glossary.html")
    page.keyboard.press("Tab")
    assert page.evaluate("document.activeElement.className") == "skip", "the skip link is the first stop"
    page.keyboard.press("Enter")
    assert page.evaluate("document.activeElement.id") == "content"
    assert page.locator('.tabs a[aria-current="true"]').inner_text() == "Reference"
    assert page.locator('.sidenav a[aria-current="page"]').inner_text() == "Terminology"
    assert page.locator(".onpage a").count() > 10
    for href in page.locator(".onpage a").evaluate_all("els => els.map(a => a.getAttribute('href'))"):
        assert page.locator(href).count() == 1, href
    assert page.locator(".pagenav-prev").get_attribute("href") == "workflow-catalog.html"
    assert page.locator(".pagenav-next").get_attribute("href") == "references.html"
    page.close()

    page = browser.new_page(viewport={"width": 390, "height": 800})
    page.goto(base + "/references.html")
    assert page.locator(".onpage").count() == 1 and not page.locator(".onpage").is_visible(), "On this page is hidden on phones"
    assert not page.locator("#sidenav").is_visible()
    page.click("#menu-toggle")
    page.locator("#sidenav").wait_for(state="visible")
    assert page.get_attribute("#menu-toggle", "aria-expanded") == "true"
    assert page.evaluate("document.getElementById('sidenav').contains(document.activeElement)")
    for _ in range(12):  # focus stays in the drawer or the header, never behind the scrim
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement === document.body || !!document.activeElement.closest('#sidenav, .topbar, .skip')"), "focus left the drawer"
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    assert page.get_attribute("#menu-toggle", "aria-expanded") == "false"
    assert page.evaluate("document.activeElement.id") == "menu-toggle"
    page.close()

    page = browser.new_page(reduced_motion="reduce")
    page.goto(base + "/index.html")
    assert page.evaluate("getComputedStyle(document.documentElement).scrollBehavior") == "auto"
    assert page.locator("nav.choose a").count() == 3, "the home page offers a section chooser"
    page.close()


def main():
    handler = functools.partial(QuietHandler, directory=str(ROOT / "site"))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{server.server_port}"
        try:
            with sync_playwright() as p:
                options = {}
                if os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
                    options["executable_path"] = os.environ["PLAYWRIGHT_CHROMIUM_EXECUTABLE"]
                browser = p.chromium.launch(**options)
                page = browser.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.add_init_script("""Object.defineProperty(navigator, 'clipboard', {
                  value: {writeText: async text => {window.copiedText = text;}}
                });""")
                page.goto(base + "/index.html")
                assert page.locator("figure.diagram").count() == 2
                page.locator(".diagram .zoom").first.click()
                image = page.locator("#lightbox img")
                image.wait_for(state="visible")
                page.wait_for_function("document.querySelector('#lightbox img').complete")
                assert image.evaluate("img => img.naturalWidth > 0")
                assert page.evaluate("""() => {
                  const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
                  return ids.length === new Set(ids).size;
                }""")
                page.keyboard.press("Escape")
                assert page.locator("#lightbox").is_hidden()

                # Delay the index so typing always happens before it loads: results must still appear.
                page.route("**/search-index.json", lambda route: (page.wait_for_timeout(800), route.continue_()))
                page.keyboard.press("/")
                page.locator("#search-input").fill("harness engineering")
                result = page.locator("#search-results a", has_text="Harness engineering").first
                result.wait_for(state="visible")
                assert result.get_attribute("href").endswith("glossary.html#harness-engineering")
                page.keyboard.press("Escape")

                assert page.locator("nav.routes .route").count() == 5
                assert page.locator("#map svg").first.get_attribute("role") == "group"
                assert page.locator("#adoption svg").first.get_attribute("role") == "img"
                tree = page.locator("#map svg").first.aria_snapshot()
                names = re.findall(r'- link "([^"]+)"', tree)
                assert len(names) == 18 and "Engineering Kit" in names, tree
                kit = page.get_by_role("link", name="Engineering Kit", exact=True)
                assert kit.get_attribute("href") == "glossary.html#engineering-kit"
                page.get_by_role("link", name="intake & triage", exact=True).click()
                page.wait_for_url("**/workflow-catalog.html#W01")
                page.locator("#wf-detail").wait_for(state="visible")
                assert "W01" in page.locator("#wf-detail").inner_text()

                page.goto(base + "/workflow-catalog.html")
                for label, visible in [("Table", "wf-table"), ("Traditional map", "wf-trad"), ("Map", "wf-map")]:
                    page.get_by_role("tab", name=label, exact=True).click()
                    for panel in ("wf-map", "wf-table", "wf-trad"):
                        assert page.locator("#" + panel).is_visible() == (panel == visible), (label, panel)
                page.locator(".wf-card").first.click()
                definition = page.locator(".wf-nav a")
                definition.wait_for(state="visible")
                assert definition.get_attribute("href") == "glossary.html#workflow"
                assert not errors, errors
                accessibility(browser, base)
                browser.close()
        finally:
            server.shutdown()
    print("Browser checks passed: home map, lightbox, map links and routes, search into the terminology, catalog views and detail link, accessibility (axe, skip link, landmarks, drawer, focus, reduced motion).")


if __name__ == "__main__":
    main()
