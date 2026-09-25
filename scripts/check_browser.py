"""Browser regressions. Build first; requires Playwright Chromium.

Run explicitly (also required by CI): python scripts/check_browser.py
The ordinary unit suite remains runnable without a browser installation.
"""
from __future__ import annotations

import functools
import http.server
import os
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


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
                result = page.locator("#search-results a", has_text="Part 3").first
                result.wait_for(state="visible")
                assert result.get_attribute("href").startswith("https://vishalkhondre.github.io/ai-sdlc/")
                page.keyboard.press("Escape")

                assert page.locator("nav.routes .route").count() == 5
                kit = page.get_by_role("link", name="Engineering Kit", exact=True)
                assert kit.get_attribute("href") == "https://vishalkhondre.github.io/ai-sdlc/engineering-kit.html"
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
                assert definition.get_attribute("href") == "https://vishalkhondre.github.io/ai-sdlc/workflows.html"
                assert not errors, errors
                browser.close()
        finally:
            server.shutdown()
    print("Browser checks passed: home map, lightbox, map links and routes, search into the series, catalog views and detail link.")


if __name__ == "__main__":
    main()
