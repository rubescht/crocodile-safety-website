// Bring a playing video fully into view (clear of the phone call bar)
function showVideo(v) {
  if (!v) return;
  var r = v.getBoundingClientRect(), bar = document.querySelector('.callbar');
  var barH = bar && getComputedStyle(bar).display !== 'none' ? bar.offsetHeight : 0;
  var room = window.innerHeight - barH;
  if (r.top >= 8 && r.bottom <= room - 8) return;
  var top = window.scrollY + r.top - Math.max(12, (room - r.height) / 2);
  var smooth = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.scrollTo({ top: top, behavior: smooth ? 'smooth' : 'auto' });
}
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
      showVideo(v);
    });
    v.addEventListener('ended', function () { v.muted = true; v.loop = true; fig.classList.remove('has-sound'); v.controls = false; v.play(); });
    // transcript: highlight the line being spoken; tap a line to jump there
    var lines = fig.querySelectorAll('.transcript button');
    if (lines.length) {
      // on phones the transcript replaces the small in-video captions
      if (window.matchMedia('(max-width: 640px)').matches && v.textTracks && v.textTracks[0]) v.textTracks[0].mode = 'hidden';
      v.addEventListener('timeupdate', function () {
        var t = v.currentTime;
        lines.forEach(function (b) { b.classList.toggle('is-on', t >= +b.dataset.start - 0.3 && t < +b.dataset.end + 1.5); });
      });
      lines.forEach(function (b) { b.addEventListener('click', function () {
        v.currentTime = +b.dataset.start; var p = v.play(); if (p && p.catch) p.catch(function () {});
      }); });
    }
  });


  // Synced infographics: highlight the line of defence being narrated; tap to jump
  document.querySelectorAll('[data-sync]').forEach(function (box) {
    var v = box.querySelector('video'); if (!v) return;
    var CH = [0, 8, 16, 24, 32, 40, 48, 56];
    var btns = box.querySelectorAll('.ch'), marks = box.querySelectorAll('.mk[data-ch]'), dets = box.querySelectorAll('.ch-detail');
    var cur = -1;
    function chapterAt(t) { var c = 0; for (var i = 1; i < CH.length; i++) if (t >= CH[i]) c = i; return c > 6 ? 0 : c; }
    function set(c) {
      if (c === cur) return; cur = c;
      btns.forEach(function (b) { var n = +b.dataset.ch; b.classList.toggle('is-on', n === c); b.classList.toggle('is-done', c > 0 && n < c); b.setAttribute('aria-current', n === c ? 'true' : 'false'); });
      marks.forEach(function (m) { m.classList.toggle('is-on', +m.dataset.ch === c); });
      dets.forEach(function (d) { d.classList.toggle('is-on', +d.dataset.ch === c); });
    }
    v.addEventListener('timeupdate', function () {
      var t = v.currentTime, c = chapterAt(t); set(c);
      btns.forEach(function (b) { var n = +b.dataset.ch, bar = b.querySelector('.ch-bar i');
        if (bar && n === c) bar.style.width = Math.min(100, (t - CH[n]) / 8 * 100) + '%'; else if (bar) bar.style.width = n < c ? '100%' : '0'; });
    });
    v.addEventListener('play', function () { box.classList.add('playing'); });
    btns.forEach(function (b) { b.addEventListener('click', function () {
      v.currentTime = +b.dataset.t + 0.05; var p = v.play(); if (p && p.catch) p.catch(function () {}); set(+b.dataset.ch);
    }); });
    set(0);
  });

  // "Watch the film with sound" buttons
  document.querySelectorAll('[data-watch]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var fig = document.querySelector('[data-explainer]'); if (!fig) return;
      e.preventDefault();
      var b = fig.querySelector('.sound-btn'); if (b) b.click(); else showVideo(fig.querySelector('video'));
    });
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
