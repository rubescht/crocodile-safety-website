// Crocodile Safety Australia — site script
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('site-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Services dropdown (click / tap)
  document.querySelectorAll('.has-drop > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var li = btn.parentElement;
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.has-drop.open').forEach(function (li) {
      li.classList.remove('open');
      li.querySelector('button').setAttribute('aria-expanded', 'false');
    });
  });

  // Hero video: respect reduced motion, allow pause
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hv = document.querySelector('.hero video');
  var vt = document.querySelector('.video-toggle');
  if (hv) {
    if (reduce) { hv.removeAttribute('autoplay'); hv.pause(); }
    if (vt) {
      var setLabel = function () {
        vt.setAttribute('aria-label', hv.paused ? 'Play background video' : 'Pause background video');
        vt.innerHTML = hv.paused
          ? '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4l13 8-13 8z" fill="currentColor"/></svg>'
          : '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z" fill="currentColor"/></svg>';
      };
      vt.addEventListener('click', function () { hv.paused ? hv.play() : hv.pause(); setLabel(); });
      hv.addEventListener('play', setLabel); hv.addEventListener('pause', setLabel);
      setLabel();
    }
  }


  // Explainer film: autoplays muted with captions; tap for sound restarts with voiceover
  document.querySelectorAll('[data-explainer]').forEach(function (fig) {
    var v = fig.querySelector('video'), btn = fig.querySelector('.sound-btn');
    if (!v) return;
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); v.controls = true; }
    // play only while on screen
    if ('IntersectionObserver' in window && !reduce) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
          else if (v.muted) v.pause();
        });
      }, { threshold: 0.35 }).observe(v);
    }
    if (btn) btn.addEventListener('click', function () {
      v.muted = false; v.loop = false; v.currentTime = 0; v.controls = true;
      fig.classList.add('has-sound');
      var p = v.play(); if (p && p.catch) p.catch(function () {});
    });
    v.addEventListener('ended', function () { v.muted = true; v.loop = true; fig.classList.remove('has-sound'); v.controls = false; v.play(); });
  });

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Enquiry forms: until a form endpoint is configured, open the visitor's
  // email app with the details filled in.
  document.querySelectorAll('form[data-enquiry]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var action = form.getAttribute('action') || '';
      if (action && action.indexOf('YOUR-FORM-ID') === -1) return; // real endpoint set
      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (v, k) { if (v) lines.push(k + ': ' + v); });
      var subject = 'Website enquiry' + (data.get('Service') ? ' – ' + data.get('Service') : '');
      window.location.href = 'mailto:Chris@crocodilesafety.com.au?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      var status = form.querySelector('.form-status');
      if (status) status.textContent = 'Opening your email app… If nothing happens, call 0409 326 307.';
    });
  });

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
