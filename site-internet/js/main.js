/* =====================================================================
   SA LA GARONNE — moteur d'interactions & d'animations
   Vanilla JS, aucune dépendance. Conçu par PMC Marketing.
   ===================================================================== */
(() => {
  'use strict';

  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const coarse  = matchMedia('(pointer: coarse)').matches;
  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const lerp  = (a, b, t) => a + (b - a) * t;
  const easeOutExpo = t => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t));
  const CONFIG = Object.assign({ formEndpoint: '', email: 'contact@lagaronnetp.org' }, window.SLG_CONFIG || {});

  /* Chaînes produites par le script, selon la langue du document */
  const LANG = (document.documentElement.lang || 'fr').toLowerCase().split('-')[0];
  const STR = ({
    fr: { sending: 'Envoi en cours…', sent: 'Merci, votre message a bien été envoyé. Nous revenons vers vous rapidement.',
          error: 'Une erreur est survenue. Vous pouvez nous écrire directement à ', mail: 'Votre messagerie va s’ouvrir avec le message pré-rempli.',
          subject: '[Site web] ', defaultSubject: 'Demande de contact',
          lName: 'Nom', lOrg: 'Organisation', lEmail: 'Email', lPhone: 'Téléphone', lSubject: 'Objet' },
    en: { sending: 'Sending…', sent: 'Thank you, your message has been sent. We will get back to you shortly.',
          error: 'Something went wrong. You can also write to us directly at ', mail: 'Your email client will open with the message pre-filled.',
          subject: '[Website] ', defaultSubject: 'Contact enquiry',
          lName: 'Name', lOrg: 'Organisation', lEmail: 'Email', lPhone: 'Phone', lSubject: 'Subject' },
    zh: { sending: '正在发送……', sent: '感谢您的留言，我们已收到并将尽快回复。',
          error: '发送失败。您也可以直接发送邮件至 ', mail: '系统将打开您的邮件客户端，内容已自动填好。',
          subject: '［网站留言］', defaultSubject: '联系咨询',
          lName: '姓名', lOrg: '单位', lEmail: '电子邮箱', lPhone: '电话', lSubject: '主题' }
  })[LANG] || null;

  /* ------------------------------------------------------------------
     1. Préchargeur
  ------------------------------------------------------------------ */
  const loader = $('.loader');
  const boot = () => {
    document.body.classList.add('is-ready');
    initReveals();
    initSplit();
  };
  if (loader && !reduced && !sessionStorage.getItem('slg-seen')) {
    sessionStorage.setItem('slg-seen', '1');
    document.body.classList.add('is-locked');
    setTimeout(() => {
      loader.classList.add('is-done');
      document.body.classList.remove('is-locked');
      boot();
    }, 1500);
  } else {
    if (loader) loader.remove();
    document.body.classList.add('no-loader');
    boot();
  }

  /* ------------------------------------------------------------------
     2. Split de texte (mots) — appliqué avant l'observation
  ------------------------------------------------------------------ */
  function splitNode(node, counter) {
    if (node.nodeType === 3) {
      const frag = document.createDocumentFragment();
      const parts = node.textContent.split(/(\s+)/);
      parts.forEach(part => {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
        const w = document.createElement('span'); w.className = 'w';
        const wi = document.createElement('span'); wi.className = 'wi';
        wi.textContent = part;
        wi.style.transitionDelay = (counter.i++ * 0.045) + 's';
        w.appendChild(wi); frag.appendChild(w);
      });
      node.parentNode.replaceChild(frag, node);
    } else if (node.nodeType === 1 && node.tagName !== 'BR') {
      Array.from(node.childNodes).forEach(n => splitNode(n, counter));
    }
  }
  function initSplit() {
    $$('[data-split]').forEach(el => {
      if (el.dataset.splitDone) return;
      el.dataset.splitDone = '1';
      const counter = { i: 0 };
      Array.from(el.childNodes).forEach(n => splitNode(n, counter));
    });
  }

  /* ------------------------------------------------------------------
     3. Révélations au scroll
  ------------------------------------------------------------------ */
  function initReveals() {
    // Enveloppe interne des masques image (le clip-path est appliqué au wrapper, pas à l'élément observé)
    $$('.mask').forEach(m => {
      if ($('.mask__in', m)) return;
      const inner = document.createElement('div'); inner.className = 'mask__in';
      while (m.firstChild) inner.appendChild(m.firstChild);
      m.appendChild(inner);
    });
    const targets = $$('[data-reveal], .stagger, .mask, [data-split], .tl, .draw, [data-count], .exp-card');
    if (reduced || !('IntersectionObserver' in window)) {
      targets.forEach(t => { t.classList.add('is-in'); if (t.dataset.count) t.textContent = formatCount(t, +t.dataset.count); });
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        if (el.dataset.delay) el.style.transitionDelay = el.dataset.delay + 'ms';
        el.classList.add('is-in');
        if (el.dataset.count !== undefined) runCount(el);
        io.unobserve(el);
      });
    }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
    targets.forEach(t => io.observe(t));
  }

  function formatCount(el, v) {
    const dec = parseInt(el.dataset.decimals || '0', 10);
    let s = dec ? v.toFixed(dec).replace('.', ',') : Math.round(v).toString();
    return el.dataset.sep !== undefined ? s.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') : s;
  }
  function runCount(el) {
    const to = parseFloat(el.dataset.count);
    const from = parseFloat(el.dataset.from || (to > 100 ? to - 120 : 0));
    const dur = 1400; const t0 = performance.now();
    const tick = now => {
      const t = clamp((now - t0) / dur, 0, 1);
      el.textContent = formatCount(el, lerp(from, to, easeOutExpo(t)));
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  /* ------------------------------------------------------------------
     4. Navigation
  ------------------------------------------------------------------ */
  const nav = $('.nav');
  let lastY = window.scrollY;
  function updateNav() {
    if (!nav) return;
    const y = window.scrollY;
    nav.classList.toggle('is-scrolled', y > 40);
    if (!document.body.classList.contains('menu-open')) {
      if (y > 320 && y - lastY > 6) nav.classList.add('is-hidden');
      else if (lastY - y > 4 || y < 320) nav.classList.remove('is-hidden');
    }
    lastY = y;
  }
  updateNav();

  const burger = $('.burger');
  if (burger) {
    burger.addEventListener('click', () => {
      const open = document.body.classList.toggle('menu-open');
      document.body.classList.toggle('is-locked', open);
      burger.setAttribute('aria-expanded', open);
      nav && nav.classList.remove('is-hidden');
    });
    $$('.menu a').forEach(a => a.addEventListener('click', () => {
      document.body.classList.remove('menu-open', 'is-locked');
    }));
  }

  // Lien actif
  const path = location.pathname.split('/').pop() || 'index.html';
  $$('.nav__link[href], .menu__list a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) a.classList.add('is-active');
    if (a.dataset.group && path.startsWith(a.dataset.group)) a.classList.add('is-active');
  });
  const expertisePages = ['assainissement.html', 'eau-potable.html', 'rehabilitation-sans-tranchee.html', 'travaux-complexes.html'];
  if (expertisePages.includes(path)) $$('.nav__link[data-group="expertises"]').forEach(a => a.classList.add('is-active'));

  /* ------------------------------------------------------------------
     5. Curseur personnalisé & boutons magnétiques
  ------------------------------------------------------------------ */
  if (!coarse && !reduced) {
    const dot = document.createElement('div'); dot.className = 'cursor';
    const ring = document.createElement('div'); ring.className = 'cursor-ring';
    const lbl = document.createElement('span'); ring.appendChild(lbl);
    document.body.append(dot, ring);
    let mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my, shown = false;
    addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
      if (!shown) { shown = true; rx = mx; ry = my; }
    }, { passive: true });
    const loop = () => {
      rx = lerp(rx, mx, 0.16); ry = lerp(ry, my, 0.16);
      dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%,-50%)`;
      ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%,-50%)`;
      requestAnimationFrame(loop);
    };
    loop();
    document.addEventListener('mouseover', e => {
      const t = e.target.closest('a, button, [data-cursor], input, textarea, select, label');
      document.body.classList.toggle('cur-hover', !!t);
      const view = e.target.closest('[data-cursor]');
      document.body.classList.toggle('cur-view', !!view);
      if (view) lbl.textContent = view.dataset.cursor || 'Voir';
    });

    // Magnétisme
    $$('.btn, .burger').forEach(btn => {
      btn.addEventListener('mousemove', e => {
        const r = btn.getBoundingClientRect();
        const x = e.clientX - r.left - r.width / 2;
        const y = e.clientY - r.top - r.height / 2;
        btn.style.transform = `translate(${x * 0.22}px, ${y * 0.28}px)`;
      });
      btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
    });
  }

  /* ------------------------------------------------------------------
     6. Boucle de scroll : parallaxe, sections épinglées, frises
  ------------------------------------------------------------------ */
  const plx = $$('[data-parallax]');
  const scrubs = $$('[data-scrub]');
  const lines = $$('[data-scrub-line]');
  let ticking = false;

  function progressOf(el) {
    const r = el.getBoundingClientRect();
    const vh = innerHeight;
    return clamp(-r.top / (r.height - vh), 0, 1);
  }

  function frame() {
    ticking = false;
    const vh = innerHeight;
    updateNav();

    if (!reduced) {
      plx.forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const speed = parseFloat(el.dataset.parallax) || 0.15;
        const off = (r.top + r.height / 2 - vh / 2) * -speed;
        el.style.transform = `translate3d(0, ${off.toFixed(1)}px, 0)`;
      });
    }

    scrubs.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const p = matchMedia('(max-width: 960px)').matches ? 1 : progressOf(el);
      el.style.setProperty('--p', p.toFixed(4));
      const h = handlers[el.dataset.scrub];
      if (h) h(el, p);
    });

    lines.forEach(el => {
      const r = el.getBoundingClientRect();
      const p = clamp((vh * 0.75 - r.top) / r.height, 0, 1);
      el.style.setProperty('--p', p.toFixed(3));
    });
  }
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  frame();

  /* ------------------------------------------------------------------
     7. Gestionnaires de sections épinglées
  ------------------------------------------------------------------ */
  const handlers = {};

  // Libellés de la coupe animée « sans tranchée », selon la langue du document
  const COUPE_LABELS = ({
    fr: ['INSPECTION CAMÉRA', 'FRAISAGE ROBOTISÉ', 'CHEMISAGE EN COURS', 'CONDUITE RÉHABILITÉE'],
    en: ['CCTV INSPECTION', 'ROBOTIC MILLING', 'LINING IN PROGRESS', 'PIPE REHABILITATED'],
    zh: ['闭路电视检测', '机器人铣削', '内衬施工中', '管道已修复']
  })[(document.documentElement.lang || 'fr').toLowerCase().split('-')[0]] || ['INSPECTION CAMÉRA', 'FRAISAGE ROBOTISÉ', 'CHEMISAGE EN COURS', 'CONDUITE RÉHABILITÉE'];

  // 7a. Défilement horizontal des réalisations
  handlers.hscroll = (el, p) => {
    const track = $('.hscroll__track', el);
    if (!track) return;
    if (matchMedia('(max-width: 960px)').matches) { track.style.transform = ''; return; }
    const max = track.scrollWidth - innerWidth + 24;
    track.style.transform = `translate3d(${(-p * max).toFixed(1)}px, 0, 0)`;
  };

  // 7b. Coupe sous la ville — réhabilitation sans tranchée
  handlers.coupe = (() => {
    let ready = false, pipe, L, liner, linerIn, rover, cam, cutter, head, beam, cracks, flow, steps, lblLive, lblState;
    const PH = 4;
    const init = el => {
      pipe = $('#pipeAxis', el); if (!pipe) return false;
      L = pipe.getTotalLength();
      liner = $('#liner', el); linerIn = $('#linerIn', el);
      [liner, linerIn].forEach(l => { l.style.strokeDasharray = L; l.style.strokeDashoffset = L; });
      rover = $('#rover', el); cam = $('#camHead', el); cutter = $('#cutHead', el); head = $('#linerHead', el); beam = $('#beam', el);
      cracks = $$('.crack', el); flow = $('#flow', el);
      steps = $$('.step', el); lblLive = $('#lblLive', el); lblState = $('#lblState', el);
      ready = true; return true;
    };
    return (el, p) => {
      if (!ready && !init(el)) return;
      const mobile = matchMedia('(max-width: 960px)').matches;
      if (mobile) p = 0.999; // vue finale sur mobile : conduite réhabilitée
      const phase = Math.min(PH - 1, Math.floor(p * PH));
      const lp = clamp((p * PH) - phase, 0, 1); // progression locale
      steps.forEach((s, i) => {
        s.classList.toggle('is-active', i === phase || mobile);
        s.style.setProperty('--sp', i < phase ? 1 : i === phase ? lp : 0);
      });
      // Position de l'engin
      const travel = phase < 3 ? lp : 1;
      const pt = pipe.getPointAtLength(L * travel);
      const rx = pt.x, ry = pt.y;
      rover.setAttribute('transform', `translate(${rx.toFixed(1)}, ${ry.toFixed(1)})`);
      rover.style.opacity = phase < 2 ? 1 : 0;
      cam.style.opacity = phase === 0 ? 1 : 0;
      cutter.style.opacity = phase === 1 ? 1 : 0;
      beam.style.opacity = phase === 0 ? 0.8 : 0;
      if (phase === 1) cutter.setAttribute('transform', `rotate(${(lp * 1440).toFixed(0)})`);
      // Fissures : éliminées par le fraisage
      cracks.forEach(c => {
        const cx = parseFloat(c.dataset.x);
        c.style.opacity = (phase > 1 || (phase === 1 && rx > cx)) ? 0 : 1;
      });
      // Gaine : phase 3
      const lin = phase < 2 ? 0 : phase === 2 ? lp : 1;
      liner.style.strokeDashoffset = (L * (1 - lin)).toFixed(1);
      linerIn.style.strokeDashoffset = (L * (1 - lin)).toFixed(1);
      const hp = pipe.getPointAtLength(L * lin);
      head.setAttribute('transform', `translate(${hp.x.toFixed(1)}, ${hp.y.toFixed(1)})`);
      head.style.opacity = phase === 2 ? 1 : 0;
      // Remise en service : phase 4
      flow.style.opacity = phase === 3 ? clamp(lp * 1.6, 0, 1) : 0;
      if (lblLive) lblLive.style.opacity = phase === 3 ? 1 : 0;
      if (lblState) lblState.textContent = COUPE_LABELS[phase];
    };
  })();

  /* ------------------------------------------------------------------
     8. Transitions de page
  ------------------------------------------------------------------ */
  if (!reduced) {
    document.addEventListener('click', e => {
      const a = e.target.closest('a[href]');
      if (!a) return;
      const href = a.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || a.target === '_blank' || a.hasAttribute('download')) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) return;
      e.preventDefault();
      document.body.classList.add('is-leaving');
      setTimeout(() => { location.href = a.href; }, 520);
    });
    addEventListener('pageshow', e => { if (e.persisted) document.body.classList.remove('is-leaving'); });
  }

  /* ------------------------------------------------------------------
     8bis. Chargement anticipé des images
     `loading="lazy"` ne déclenche le téléchargement qu'à l'approche immédiate du
     bloc : sur une page longue avec sections épinglées, l'image arrive trop tard.
     On repasse en chargement immédiat dès que le bloc est à 1400 px du viewport.
  ------------------------------------------------------------------ */
  const startEarlyLoading = () => {
    const lazies = $$('img[loading="lazy"]');
    if (!lazies.length) return;
    if (!('IntersectionObserver' in window)) { lazies.forEach(i => { i.loading = 'eager'; }); return; }
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const img = e.target;
        img.loading = 'eager';
        img.decoding = 'async';
        if (img.dataset.pending !== undefined) return;
        img.dataset.pending = '1';
        const ready = () => {
          const holder = img.closest('.mask, .work, .scan, .band, .hq__img, .feature__media');
          if (holder) holder.classList.add('img-ready');
        };
        img.addEventListener('load', ready, { once: true });
        img.addEventListener('error', ready, { once: true });
        if (img.complete) ready();
        io.unobserve(img);
      });
    }, { rootMargin: '1000px 0px 1000px 0px' });
    lazies.forEach(i => io.observe(i));
  };
  // Après le chargement initial seulement : sinon ces images se disputent la bande
  // passante avec l'image du hero et retardent le premier affichage utile.
  const idle = window.requestIdleCallback || (fn => setTimeout(fn, 200));
  if (document.readyState === 'complete') idle(startEarlyLoading);
  else addEventListener('load', () => idle(startEarlyLoading), { once: true });

  /* ------------------------------------------------------------------
     9. Médias & divers
  ------------------------------------------------------------------ */
  $$('.hero__media img').forEach(img => {
    const done = () => img.classList.add('is-loaded');
    img.complete ? done() : img.addEventListener('load', done);
  });
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Images déjà présentes en cache : on lève tout de suite le fondu
  $$('.work img, .scan img, .hq__img img, .band img').forEach(img => {
    if (img.complete && img.naturalWidth) {
      const h = img.closest('.work, .scan, .hq__img, .band');
      if (h) h.classList.add('img-ready');
    }
  });

  // Filtres de galerie
  const filters = $$('[data-filter]');
  if (filters.length) {
    filters.forEach(btn => btn.addEventListener('click', () => {
      filters.forEach(b => b.classList.toggle('is-active', b === btn));
      const f = btn.dataset.filter;
      $$('.gallery .work').forEach(w => {
        const show = f === 'all' || (w.dataset.cat || '').split(' ').includes(f);
        w.classList.toggle('is-hidden', !show);
      });
    }));
  }

  // Formulaire de contact
  const form = $('form[data-form]');
  if (form) {
    const status = $('.form__status', form);
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form).entries());
      if (data._gotcha) return; // anti-spam
      const btn = $('button[type="submit"]', form);
      btn.disabled = true;
      if (CONFIG.formEndpoint) {
        status.textContent = STR.sending;
        try {
          const r = await fetch(CONFIG.formEndpoint, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
          if (!r.ok) throw new Error();
          status.textContent = STR.sent;
          form.reset();
        } catch (err) {
          status.textContent = STR.error + CONFIG.email + '.';
        }
      } else {
        const subject = encodeURIComponent(STR.subject + (data.objet || STR.defaultSubject) + ' — ' + (data.organisation || data.nom || ''));
        const body = encodeURIComponent(
          `${STR.lName} : ${data.nom || ''}\n${STR.lOrg} : ${data.organisation || ''}\n${STR.lEmail} : ${data.email || ''}\n${STR.lPhone} : ${data.telephone || ''}\n${STR.lSubject} : ${data.objet || ''}\n\n${data.message || ''}`
        );
        location.href = `mailto:${CONFIG.email}?subject=${subject}&body=${body}`;
        status.textContent = STR.mail;
      }
      btn.disabled = false;
    });
  }
})();
