/* The AI SDLC Map — progressive enhancement. No dependencies. */
(function () {
  'use strict';
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* ignore */ } }
  };

  /* ---------- theme ---------- */
  const themeBtn = $('#theme-toggle');
  if (themeBtn) themeBtn.addEventListener('click', () => {
    const root = document.documentElement;
    const dark = matchMedia('(prefers-color-scheme: dark)').matches;
    const cur = root.dataset.theme && root.dataset.theme !== 'auto' ? root.dataset.theme : (dark ? 'dark' : 'light');
    const next = cur === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next; store.set('aisdlcmap-theme', next);
  });

  /* ---------- navigation drawer (small screens, D-020) ---------- */
  const menu = $('#menu-toggle'), sidenav = $('#sidenav'), scrim = $('#scrim');
  function setDrawer(open, returnFocus) {
    if (!menu || !sidenav) return;
    sidenav.classList.toggle('open', open);
    if (scrim) scrim.hidden = !open;
    // While the drawer is open, the page behind it cannot take focus (it sits under the scrim).
    $$('main, .onpage, .footer').forEach(el => { if (open) el.setAttribute('inert', ''); else el.removeAttribute('inert'); });
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    if (open) { const first = $('a', sidenav); if (first) first.focus(); }
    else if (returnFocus) menu.focus();
  }
  if (menu && sidenav) {
    menu.addEventListener('click', () => setDrawer(!sidenav.classList.contains('open'), true));
    if (scrim) scrim.addEventListener('click', () => setDrawer(false, true));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && sidenav.classList.contains('open')) setDrawer(false, true); });
    matchMedia('(min-width: 961px)').addEventListener('change', e => { if (e.matches) setDrawer(false, false); });
  }

  /* ---------- reading progress + active TOC ---------- */
  const bar = $('#progress span'), article = $('#article');
  const tocLinks = $$('.onpage a');
  const headings = tocLinks.map(a => document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
  function onScroll() {
    if (bar && article) {
      const r = article.getBoundingClientRect();
      const total = r.height - innerHeight;
      const p = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 0;
      bar.style.width = (p * 100).toFixed(1) + '%';
    }
    if (headings.length) {
      let cur = headings[0];
      for (const h of headings) if (h.getBoundingClientRect().top < 120) cur = h;
      tocLinks.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + cur.id));
    }
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- glossary tooltips ---------- */
  let glossary = {};
  try { glossary = JSON.parse(($('#glossary-data') || {}).textContent || '{}'); } catch (e) { glossary = {}; }
  const tip = $('#tip');
  const ATTR = { adopted: 'Adopted from source', adapted: 'Adapted from source', coined: 'Coined here', common: 'Common usage' };
  function showTip(el, html) {
    if (!tip) return;
    tip.innerHTML = html; tip.hidden = false;
    const r = el.getBoundingClientRect(), tw = tip.offsetWidth, th = tip.offsetHeight;
    let x = Math.min(Math.max(8, r.left), innerWidth - tw - 8);
    let y = r.top - th - 10; if (y < 8) y = r.bottom + 10;
    tip.style.left = x + 'px'; tip.style.top = y + 'px';
  }
  function hideTip() { if (tip) tip.hidden = true; }
  $$('a.term').forEach(a => {
    const g = glossary[a.dataset.term]; if (!g) return;
    const html = `<b>${g.term}</b>${g.def.length > 260 ? g.def.slice(0, 257) + '…' : g.def}<div class="attr attr-${g.attr}">${ATTR[g.attr] || g.attr}</div>`;
    a.addEventListener('mouseenter', () => showTip(a, html));
    a.addEventListener('focus', () => showTip(a, html));
    a.addEventListener('mouseleave', hideTip); a.addEventListener('blur', hideTip);
  });
  /* footnote popovers */
  $$('sup a.footnote-ref, sup a[href^="#fn"]').forEach(a => {
    const target = document.getElementById(a.getAttribute('href').slice(1)); if (!target) return;
    const html = target.innerHTML.replace(/<a[^>]*footnote-backref[^>]*>.*?<\/a>/, '');
    a.addEventListener('mouseenter', () => showTip(a, html));
    a.addEventListener('mouseleave', hideTip);
  });
  addEventListener('scroll', hideTip, { passive: true });

  /* ---------- code copy buttons ---------- */
  $$('.prose pre').forEach(pre => {
    const b = document.createElement('button'); b.className = 'copybtn'; b.type = 'button'; b.textContent = 'Copy';
    b.addEventListener('click', async () => {
      const code = $('code', pre);
      if (!code || !navigator.clipboard) { toast('Copy unavailable'); return; }
      try {
        await navigator.clipboard.writeText(code.textContent);
        toast('Copied');
      } catch (e) { toast('Copy failed'); }
    });
    pre.appendChild(b);
  });
  $$('[data-copy]').forEach(b => b.addEventListener('click', () => {
    navigator.clipboard && navigator.clipboard.writeText(b.dataset.copy).then(() => toast('Link copied'));
  }));
  function toast(msg) {
    const t = document.createElement('div'); t.className = 'toast'; t.textContent = msg; document.body.appendChild(t);
    setTimeout(() => t.remove(), 1600);
  }

  /* ---------- lightbox for diagrams ---------- */
  const lb = $('#lightbox'), lbBody = lb && $('.lightbox-body', lb);
  function openLightbox(svg) {
    if (!lb) return;
    // A separate image document isolates IDs from the original inline diagram.
    const image = document.createElement('img');
    const figure = svg.closest('.diagram');
    image.src = base + 'diagrams/' + encodeURIComponent(figure.dataset.diagram) + '.svg';
    const caption = $('figcaption', figure);
    image.alt = caption ? caption.textContent.trim() : 'Diagram';
    lbBody.replaceChildren(image); lb.hidden = false; document.body.style.overflow = 'hidden';
  }
  function closeLightbox() { if (lb) { lb.hidden = true; document.body.style.overflow = ''; } }
  $$('.diagram .zoom').forEach(b => b.addEventListener('click', e => { e.preventDefault(); openLightbox($('svg', b.parentElement)); }));
  $$('.diagram-frame svg').forEach(svg => svg.addEventListener('dblclick', () => openLightbox(svg)));
  if (lb) { lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lightbox-close')) closeLightbox(); }); }

  /* ---------- model explorer (home) ---------- */
  $$('#model-explorer .layer').forEach(l => {
    l.addEventListener('mouseenter', () => $$('#model-explorer .layer').forEach(x => x.classList.toggle('on', x === l)));
    l.addEventListener('mouseleave', () => l.classList.remove('on'));
  });

  /* ---------- reference sheet toggles ---------- */
  $$('.toggle').forEach(t => {
    $$('button', t).forEach(b => b.addEventListener('click', () => setVariant(t.closest('.ref-pair'), b.dataset.variant)));
  });
  function setVariant(section, v) {
    $$('.toggle button', section).forEach(b => b.classList.toggle('on', b.dataset.variant === v));
    $$('.variant', section).forEach(x => x.hidden = x.dataset.variant !== v);
  }
  const toggleAll = $('#toggle-all');
  if (toggleAll) {
    let generic = false;
    toggleAll.addEventListener('click', () => {
      generic = !generic; $$('.ref-pair').forEach(s => setVariant(s, generic ? 'generic' : 'export'));
      toggleAll.textContent = generic ? 'switch all to the worked example' : 'switch all to generic';
    });
  }

  /* ---------- glossary filter ---------- */
  const tf = $('#term-filter');
  if (tf) $$('button', tf).forEach(b => b.addEventListener('click', () => {
    $$('button', tf).forEach(x => x.classList.toggle('on', x === b));
    $$('.term-entry').forEach(e => e.hidden = b.dataset.attr !== 'all' && e.dataset.attr !== b.dataset.attr);
  }));

  /* ---------- workflow catalog ---------- */
  const wfData = $('#wf-data');
  if (wfData) initCatalog(JSON.parse(wfData.textContent));
  function initCatalog(D) {
    const phases = D.phases, byPhase = {}, byId = {};
    D.workflows.forEach(w => { (byPhase[w.phase] = byPhase[w.phase] || []).push(w); byId[w.id] = w; });
    const state = { q: '', m: 'all', a: 'all', view: 'map', sort: 'id', desc: false };
    const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    const phaseName = k => (phases.find(p => p.key === k) || {}).name || k;
    function visible(w) {
      if (state.m !== 'all' && w.maturity !== state.m) return false;
      if (state.a !== 'all' && !(w.applies_to.includes('All') || w.applies_to.includes(state.a))) return false;
      if (state.q) {
        const hay = [w.id, w.name, w.decision, w.agent, w.checks, w.people, w.evidence].join(' ').toLowerCase();
        if (!hay.includes(state.q)) return false;
      }
      return true;
    }
    /* map */
    const map = $('#wf-map');
    map.innerHTML = phases.map(p => `<div class="wf-col" data-phase="${p.key}"><div class="wf-col-head"><b>${esc(p.name)}</b><br>${(byPhase[p.key] || []).length} workflows</div>${(byPhase[p.key] || []).map(w => `
      <button class="wf-card m-${w.maturity}" type="button" data-id="${w.id}" id="${w.id}"><span class="id">${w.id} · ${w.maturity}</span><span class="name">${esc(w.name)}</span><span class="tags">${w.applies_to.map(a => `<span class="tag">${esc(a)}</span>`).join('')}</span></button>`).join('')}<div class="wf-empty" hidden>No match</div></div>`).join('');
    /* table */
    const tbl = $('#wf-table');
    const cols = [['id', 'ID'], ['phase', 'Phase'], ['name', 'Workflow'], ['decision', 'Decision it supports'], ['maturity', 'Maturity'], ['applies', 'Change type']];
    function renderTable() {
      const rows = D.workflows.slice().sort((x, y) => {
        const k = state.sort; const vx = k === 'applies' ? x.applies_to.join() : x[k]; const vy = k === 'applies' ? y.applies_to.join() : y[k];
        return (vx > vy ? 1 : vx < vy ? -1 : 0) * (state.desc ? -1 : 1);
      });
      tbl.innerHTML = `<div class="table-wrap"><table><thead><tr>${cols.map(c => `<th data-k="${c[0]}" class="${state.sort === c[0] ? 'sorted' + (state.desc ? ' desc' : '') : ''}">${c[1]}</th>`).join('')}</tr></thead><tbody>${rows.map(w => `
        <tr data-id="${w.id}"${visible(w) ? '' : ' hidden'}><td>${w.id}</td><td>${esc(phaseName(w.phase))}</td><td><b>${esc(w.name)}</b></td><td>${esc(w.decision)}</td><td><span class="pill m-${w.maturity}">${w.maturity}</span></td><td>${w.applies_to.join(', ')}</td></tr>`).join('')}</tbody></table></div>`;
      $$('th', tbl).forEach(th => th.addEventListener('click', () => { if (state.sort === th.dataset.k) state.desc = !state.desc; else { state.sort = th.dataset.k; state.desc = false; } renderTable(); }));
      $$('tr[data-id]', tbl).forEach(tr => tr.addEventListener('click', () => openDetail(tr.dataset.id)));
    }
    function apply() {
      $$('.wf-card', map).forEach(c => c.hidden = !visible(byId[c.dataset.id]));
      $$('.wf-col', map).forEach(col => { const any = $$('.wf-card:not([hidden])', col).length; $('.wf-empty', col).hidden = any > 0; });
      $$('tr[data-id]', tbl).forEach(tr => tr.hidden = !visible(byId[tr.dataset.id]));
    }
    $('#wf-search').addEventListener('input', e => { state.q = e.target.value.trim().toLowerCase(); apply(); });
    $$('#wf-maturity button').forEach(b => b.addEventListener('click', () => { $$('#wf-maturity button').forEach(x => x.classList.toggle('on', x === b)); state.m = b.dataset.m; apply(); }));
    $$('#wf-applies button').forEach(b => b.addEventListener('click', () => { $$('#wf-applies button').forEach(x => x.classList.toggle('on', x === b)); state.a = b.dataset.a; apply(); }));
    $$('.viewtabs button').forEach(b => b.addEventListener('click', () => {
      $$('.viewtabs button').forEach(x => x.classList.toggle('on', x === b)); state.view = b.dataset.view;
      $$('[data-view]', $('.section-inner')).forEach(v => { if (v.tagName !== 'BUTTON') v.hidden = v.dataset.view !== state.view; });
    }));
    $$('.wf-card', map).forEach(c => c.addEventListener('click', () => openDetail(c.dataset.id)));
    /* detail panel */
    const detail = $('#wf-detail'), body = $('.wf-detail-body', detail);
    function openDetail(id) {
      const w = byId[id]; if (!w) return;
      const ids = D.workflows.map(x => x.id), i = ids.indexOf(id);
      body.innerHTML = `
        <div class="k">${esc(phaseName(w.phase))} · ${w.id}</div>
        <h2>${esc(w.name)}</h2>
        <div><span class="pill m-${w.maturity}">${w.maturity}</span> <span class="muted" style="font-size:13px">${esc(D.maturity[w.maturity] || '')}</span></div>
        <div class="decision">${esc(w.decision)}</div>
        <div class="wf-grid">
          <div class="wf-cell agent"><span class="k">The agent</span>${esc(w.agent)}</div>
          <div class="wf-cell checks"><span class="k">The checks</span>${esc(w.checks)}</div>
          <div class="wf-cell people"><span class="k">The people</span>${esc(w.people)}</div>
        </div>
        <div class="wf-row"><span class="k">Trigger</span><span>${esc(w.trigger)}</span><span class="k">Evidence record</span><span>${esc(w.evidence)}</span><span class="k">Applies to</span><span>${w.applies_to.join(', ')}</span>${w.notes ? `<span class="k">Notes</span><span>${esc(w.notes)}</span>` : ''}</div>
        <div class="wf-nav">${i > 0 ? `<button class="btn small" type="button" data-go="${ids[i - 1]}">← ${ids[i - 1]}</button>` : '<span></span>'}<a class="btn small" href="${esc(D.definition.url)}" rel="noopener">${esc(D.definition.label)}</a>${i < ids.length - 1 ? `<button class="btn small" type="button" data-go="${ids[i + 1]}">${ids[i + 1]} →</button>` : '<span></span>'}</div>`;
      $$('[data-go]', body).forEach(b => b.addEventListener('click', () => openDetail(b.dataset.go)));
      detail.hidden = false; document.body.style.overflow = 'hidden'; history.replaceState(null, '', '#' + id);
    }
    function closeDetail() { detail.hidden = true; document.body.style.overflow = ''; }
    detail.addEventListener('click', e => { if (e.target === detail || e.target.classList.contains('lightbox-close')) closeDetail(); });
    renderTable();
    if (location.hash && byId[location.hash.slice(1)]) openDetail(location.hash.slice(1));
    addEventListener('keydown', e => { if (e.key === 'Escape') closeDetail(); });
  }

  /* ---------- search ---------- */
  const sBox = $('#search'), sIn = $('#search-input'), sRes = $('#search-results');
  let index = null, sel = -1;
  const base = (document.querySelector('link[rel=stylesheet]').getAttribute('href') || '').replace(/assets\/style\.css.*$/, '');
  function openSearch() { if (!sBox) return; sBox.hidden = false; sIn.value = ''; sRes.innerHTML = ''; sIn.focus(); if (!index) fetch(base + 'search-index.json').then(r => r.json()).then(d => { index = d; if (sIn.value) sIn.dispatchEvent(new Event('input')); }); }
  function closeSearch() { if (sBox) sBox.hidden = true; }
  const sBtn = $('#search-open'); if (sBtn) sBtn.addEventListener('click', openSearch);
  if (sBox) sBox.addEventListener('click', e => { if (e.target === sBox) closeSearch(); });
  addEventListener('keydown', e => {
    if (e.key === '/' && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
    if (e.key === 'Escape') { closeSearch(); closeLightbox(); hideTip(); }
    if (sBox && !sBox.hidden && (e.key === 'ArrowDown' || e.key === 'ArrowUp' || e.key === 'Enter')) {
      const items = $$('a', sRes); if (!items.length) return;
      if (e.key === 'Enter') { (items[sel] || items[0]).click(); return; }
      e.preventDefault(); sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
      items.forEach((a, i) => a.classList.toggle('on', i === sel)); items[sel].scrollIntoView({ block: 'nearest' });
    }
  });
  if (sIn) sIn.addEventListener('input', () => {
    const q = sIn.value.trim().toLowerCase(); sel = -1;
    if (!index || q.length < 2) { sRes.innerHTML = ''; return; }
    const terms = q.split(/\s+/);
    const scored = index.map(it => {
      const t = it.t.toLowerCase(), b = (it.b || '').toLowerCase();
      let s = 0; for (const w of terms) { if (t.includes(w)) s += 10; const n = b.split(w).length - 1; s += Math.min(n, 8); }
      return [s, it];
    }).filter(x => x[0] > 0).sort((a, b) => b[0] - a[0]).slice(0, 12);
    // index text is plain text: escape it, then mark the matches (terms are escaped the same way)
    const escHtml = str => String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    // split on the raw terms, then escape each piece, so a term never matches inside an entity
    const marks = new RegExp('(' + terms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'gi');
    const mark = str => String(str).split(marks).map((part, k) => k % 2 ? `<mark>${escHtml(part)}</mark>` : escHtml(part)).join('');
    sRes.innerHTML = scored.map(([, it]) => {
      const b = (it.b || ''); const i = b.toLowerCase().indexOf(terms[0]);
      const snip = i >= 0 ? b.slice(Math.max(0, i - 60), i + 90) : it.s;
      const hl = mark(snip);
      return `<a href="${escHtml(/^https?:/.test(it.u) ? it.u : base + it.u)}"><span class="rk">${escHtml(it.k)}</span>${escHtml(it.t)}<span class="rs">…${hl}…</span></a>`;
    }).join('') || '<div class="search-hint">Nothing found.</div>';
  });
})();

/* Design system v1.0 (D-031): icons, map hover and band focus, legend, motion, back to the map.
   Decorative only: every page works the same without it. Icons are line icons in the Lucide style,
   drawn here as paths. Band icons and colours are keyed to a band's position and read from the map
   itself, not to band names, so another map with other bands gets the same treatment. */
(function () {
  'use strict';
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const P = {
    compass: 'M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z M16.2 7.8l-2.1 6.3-6.3 2.1 2.1-6.3z',
    cycle: 'M3 12a9 9 0 0 1 15.5-6.4L21 8 M21 3v5h-5 M21 12a9 9 0 0 1-15.5 6.4L3 16 M3 21v-5h5',
    chip: 'M6 6h12v12H6z M9.5 9.5h5v5h-5z M9 2v4 M15 2v4 M9 18v4 M15 18v4 M2 9h4 M2 15h4 M18 9h4 M18 15h4',
    layers: 'M12 2l10 5-10 5-10-5z M2 12l10 5 10-5 M2 17l10 5 10-5',
    shield: 'M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z M9 12l2 2 4-4',
    trend: 'M3 17l6-6 4 4 8-8 M14 7h7v7',
    book: 'M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2z M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z',
    box: 'M12 2l9 5v10l-9 5-9-5V7z M3 7l9 5 9-5 M12 12v10',
    play: 'M7 4l13 8-13 8z',
    flag: 'M4 22V4 M4 4h13l-2 4 2 4H4',
    search: 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14z M21 21l-5-5',
    list: 'M4 6h16 M4 12h16 M4 18h10',
    map: 'M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z M9 4v14 M15 6v14',
    user: 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M4 21a8 8 0 0 1 16 0'
  };
  /* Band roles by position: 1 sets the frame, 2 says where, 3 does the work, 4 enables it, 5 proves it. */
  const BAND_ICON = ['compass', 'cycle', 'chip', 'layers', 'shield'];
  const BAND_VAR = ['context', 'lifecycle', 'core', 'enablement', 'assurance'];
  const icon = (k, size) => `<svg class="ico" width="${size || 18}" height="${size || 18}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="${P[k]}"/></svg>`;
  const el = (tag, cls, html) => { const e = document.createElement(tag); e.className = cls; if (html) e.innerHTML = html; return e; };
  const NS = 'http://www.w3.org/2000/svg';

  /* ---------- the clickable map ---------- */
  const svg = document.querySelector('figure.clickable svg');
  if (svg) {
    // The browser's own tooltip would sit on top of ours: drop <title> and title, keep the names.
    $$('title', svg).forEach(t => t.parentNode.removeChild(t));
    $$('[title]', svg).forEach(e => { if (!e.getAttribute('aria-label')) e.setAttribute('aria-label', e.getAttribute('title')); e.removeAttribute('title'); });
    const bands = [];
    $$('text', svg).forEach(t => {
      const m = /^(\d) · (.+)$/.exec(t.textContent.trim());
      const r = t.previousElementSibling;
      if (!m || !r || r.tagName !== 'rect') return;
      const n = +m[1], x = +r.getAttribute('x'), y = +r.getAttribute('y'), w = +r.getAttribute('width'), h = +r.getAttribute('height');
      const name = m[2].charAt(0) + m[2].slice(1).toLowerCase();
      const b = { n, name, y, h, stroke: r.getAttribute('stroke'), fill: r.getAttribute('fill'), ink: t.getAttribute('fill'), els: [] };
      b.key = BAND_ICON[(n - 1) % BAND_ICON.length];
      const g = document.createElementNS(NS, 'g');
      g.setAttribute('class', 'band-icon'); g.setAttribute('aria-hidden', 'true');
      g.setAttribute('transform', `translate(${x + w - 30},${y + h - 30}) scale(.8)`);
      g.innerHTML = `<path d="${P[b.key]}" fill="none" stroke="${b.ink}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>`;
      svg.appendChild(g);
      bands.push(b);
    });
    bands.sort((a, b) => a.y - b.y);
    if (bands.length) {
      $$(':scope > *', svg).forEach(e => {
        if (/^(title|desc|defs|style)$/.test(e.tagName)) return;
        let bb; try { bb = e.getBBox(); } catch (_) { return; }
        const cy = bb.y + bb.height / 2;
        const b = bands.find(o => cy >= o.y - 4 && cy <= o.y + o.h + 4);
        e.classList.add('band-el');
        if (b) b.els.push(e);
      });
      let pinned = null;
      const focus = b => {
        $$('.band-cur', svg).forEach(e => e.classList.remove('band-cur'));
        svg.classList.toggle('band-focused', !!b);
        if (b) b.els.forEach(e => e.classList.add('band-cur'));
      };
      bands.forEach(b => b.els.filter(e => (e.tagName === 'rect' || e.tagName === 'text') && +e.getAttribute('x') < 240).forEach(e => {
        e.addEventListener('mouseenter', () => { if (!pinned) focus(b); });
        e.addEventListener('mouseleave', () => { if (!pinned) focus(null); });
      }));
      const fig = svg.closest('figure');
      const lg = el('div', 'band-legend');
      lg.setAttribute('role', 'group'); lg.setAttribute('aria-label', 'Focus a band of the map');
      lg.innerHTML = bands.map((b, i) => {
        const v = BAND_VAR[(b.n - 1) % BAND_VAR.length];
        return `<button type="button" data-i="${i}" aria-pressed="false" style="--c:var(--band-${v});--t:var(--band-${v}-bg);--k:var(--band-${v}-ink)">${icon(b.key, 15)}${b.name}</button>`;
      }).join('') + '<span class="hint">Choose a band to focus it</span>';
      fig.parentNode.insertBefore(lg, fig);
      lg.addEventListener('click', e => {
        const btn = e.target.closest('button'); if (!btn) return;
        const on = btn.getAttribute('aria-pressed') === 'true';
        $$('button', lg).forEach(x => x.setAttribute('aria-pressed', 'false'));
        pinned = on ? null : bands[+btn.dataset.i];
        if (pinned) btn.setAttribute('aria-pressed', 'true');
        focus(pinned);
      });
    }
    // Hover tooltip: "Open X →", kept inside the window.
    const tip = el('div', 'maptip'); tip.setAttribute('aria-hidden', 'true'); document.body.appendChild(tip);
    const place = (x, y) => {
      const tw = tip.offsetWidth, th = tip.offsetHeight;
      let left = x + 14, top = y + 16;
      if (left + tw > innerWidth - 8) left = x - tw - 14;
      if (top + th > innerHeight - 8) top = y - th - 12;
      tip.style.left = Math.max(8, left) + 'px'; tip.style.top = Math.max(8, top) + 'px';
    };
    $$('a.maplink', svg).forEach(a => {
      const name = a.getAttribute('aria-label') || a.textContent.trim();
      const where = (a.getAttribute('href') || '').replace(/\.html/, '').replace(/[-#]/g, ' ').trim();
      a.addEventListener('mouseenter', () => {
        tip.textContent = 'Open ' + name + ' →';
        const s = document.createElement('small'); s.textContent = where; tip.appendChild(s);
        tip.classList.add('on');
      });
      a.addEventListener('mousemove', e => place(e.clientX, e.clientY));
      a.addEventListener('mouseleave', () => tip.classList.remove('on'));
    });
    addEventListener('scroll', () => tip.classList.remove('on'), { passive: true });
  }

  /* ---------- home: route and stat icons ---------- */
  const ROUTE = ['book', 'box', 'play', 'flag', 'search', 'map'];
  const ROUTE_TINT = ['core', 'enablement', 'context', 'assurance', 'lifecycle', 'core'];
  $$('.route').forEach((r, i) => {
    const v = ROUTE_TINT[i % ROUTE_TINT.length];
    const s = el('span', 'route-ico', icon(ROUTE[i % ROUTE.length], 18));
    s.style.setProperty('--t', `var(--band-${v}-bg)`); s.style.setProperty('--k', `var(--band-${v}-ink)`);
    r.insertBefore(s, r.firstChild);
  });
  const STAT = ['layers', 'trend', 'play', 'list'];
  $$('.stats > div').forEach((s, i) => s.insertBefore(el('span', 'stat-ico', icon(STAT[i % STAT.length], 18)), s.firstChild));

  /* ---------- topic pages: breadcrumb icon, section icons, back to the map ---------- */
  const crumb = document.querySelector('.crumbs a');
  if (crumb) crumb.insertBefore(el('span', 'crumb-ico', icon('map', 16)), crumb.firstChild);
  const H2 = [[/source|reference|further|read/i, 'book'], [/check|verif|evidence|test|eval|prove|valid/i, 'shield'],
    [/risk|gate|decid|decision|approv|human|person|review/i, 'user'], [/example|walk|sample|in practice/i, 'play'],
    [/tool|kit|part|platform|skill|adapter|build/i, 'box'], [/agent|harness|core/i, 'chip'], [/how|step|loop|flow|cycle|stage|level/i, 'cycle'],
    [/start|adopt|next|path/i, 'trend'], [/why|problem|goal|purpose/i, 'flag'], [/what|defin|term|mean/i, 'list']];
  const article = document.getElementById('article');
  if (article) {
    $$('h2', article).forEach(h => {
      const k = (H2.find(([re]) => re.test(h.textContent)) || [0, 'compass'])[1];
      h.classList.add('has-ico'); h.insertBefore(el('span', 'h2-ico', icon(k, 15)), h.firstChild);
    });
    const brand = document.querySelector('a.brand');
    const back = el('a', 'back-to-map', icon('map', 16) + 'Back to the map');
    back.href = ((brand && brand.getAttribute('href')) || 'index.html').replace(/#.*$/, '') + '#map';
    document.body.appendChild(back);
    const upd = () => back.classList.toggle('on', scrollY > 600);
    addEventListener('scroll', upd, { passive: true }); upd();
  }

  /* ---------- gentle motion ---------- */
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const rise = $$('.section-head, .route, .card, .prose > figure').filter(e => e.getBoundingClientRect().top > innerHeight);
    rise.forEach(e => e.classList.add('rise'));
    const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rise.forEach(e => io.observe(e));
  }
})();
