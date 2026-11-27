"""About page — infographic redesign."""

# Rough outline of mainland Australia (lon, lat)
COAST = [(113.6,-22.6),(114.2,-21.8),(116.7,-20.6),(118.8,-20.3),(121.0,-19.5),(122.3,-17.9),(122.9,-16.4),(123.6,-17.2),
 (124.4,-16.3),(125.2,-14.6),(126.9,-13.8),(128.1,-15.0),(129.0,-14.9),(129.6,-13.5),(130.6,-12.4),(131.9,-11.3),(132.6,-11.5),
 (133.5,-11.8),(135.2,-12.2),(136.7,-12.2),(136.5,-13.3),(135.5,-14.7),(136.8,-15.9),(138.2,-16.8),(139.3,-17.5),(140.8,-17.4),
 (141.6,-15.0),(141.5,-13.0),(142.1,-10.9),(142.8,-11.0),(143.5,-14.0),(144.6,-14.3),(145.4,-16.3),(146.3,-19.0),(148.8,-20.4),
 (150.8,-22.6),(153.0,-25.2),(153.6,-28.6),(153.1,-31.0),(151.5,-33.2),(150.2,-35.7),(149.9,-37.5),(147.9,-37.9),(146.3,-39.1),
 (144.6,-38.3),(141.6,-38.4),(139.8,-37.3),(139.6,-36.0),(138.1,-35.6),(138.5,-34.8),(137.8,-33.0),(137.0,-34.7),(135.9,-34.9),
 (135.2,-34.0),(134.2,-32.9),(131.1,-31.5),(128.9,-31.7),(126.1,-32.3),(124.0,-33.6),(121.9,-33.8),(118.0,-35.0),(115.9,-34.3),
 (115.0,-33.6),(115.7,-32.6),(115.0,-30.0),(114.6,-28.7),(113.5,-26.5),(113.9,-24.6)]
K = 14
def P(lon, lat): return ((lon - 111.5) * K, (-9.5 - lat) * K)
def pts(seq): return ' '.join(f'{x:.0f},{y:.0f}' for x, y in (P(*c) for c in seq))

def map_svg():
    coast = pts(COAST)
    wa = pts([(100,-5),(129,-5),(129,-45),(100,-45)])
    nt = pts([(129,-5),(138,-5),(138,-26),(129,-26)])
    qld = pts([(138,-5),(160,-5),(160,-29),(141,-29),(141,-26),(138,-26)])
    bx, by = P(131.05, -12.49)
    def lab(text, lon, lat, size=15):
        x, y = P(lon, lat)
        return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" fill="#07150F" font-family="Anton,Impact,sans-serif" font-size="{size}" letter-spacing="1">{text}</text>'
    return f'''<svg viewBox="0 -50 620 490" class="info-map" role="img" aria-label="Map of Australia with Western Australia, the Northern Territory and Queensland highlighted as the service area, and the base at Howard Springs near Darwin">
<defs><clipPath id="oz"><polygon points="{coast}"/></clipPath>
<radialGradient id="pulse"><stop offset="0" stop-color="#E3B23C" stop-opacity=".55"/><stop offset="1" stop-color="#E3B23C" stop-opacity="0"/></radialGradient></defs>
<polygon points="{coast}" fill="#1E3A2D"/>
<g clip-path="url(#oz)"><polygon points="{wa}" fill="#E3B23C" opacity=".92"/><polygon points="{nt}" fill="#F5CC63"/><polygon points="{qld}" fill="#E3B23C" opacity=".92"/></g>
<polygon points="{coast}" fill="none" stroke="#07150F" stroke-width="2"/>
<g stroke="#07150F" stroke-width="1.5" stroke-dasharray="4 4" fill="none"><polyline points="{pts([(129,-14.9),(129,-31.7)])}"/><polyline points="{pts([(129,-26),(141,-26)])}"/><polyline points="{pts([(138,-16.8),(138,-26)])}"/><polyline points="{pts([(141,-26),(141,-29),(153.4,-29)])}"/></g>
{lab('WA',121,-25,26)}{lab('NT',133.5,-20,26)}{lab('QLD',145,-22,26)}
<circle cx="{bx:.0f}" cy="{by:.0f}" r="46" fill="url(#pulse)" class="map-pulse"/>
<circle cx="{bx:.0f}" cy="{by:.0f}" r="7" fill="#07150F" stroke="#fff" stroke-width="3"/>
<line x1="{bx:.0f}" y1="{by:.0f}" x2="{bx-70:.0f}" y2="{by-38:.0f}" stroke="#fff" stroke-width="1.5"/>
<text x="{bx-74:.0f}" y="{by-44:.0f}" text-anchor="end" fill="#fff" font-family="Inter,sans-serif" font-size="16" font-weight="700">Base: Howard Springs NT</text>
</svg>'''

CROC_SIDE = ('M0 60 C60 56 140 52 220 48 C290 44 350 42 400 44 L428 44 C436 32 452 30 464 42 L500 46 C540 48 575 52 600 58 '
             'C580 65 540 67 500 67 L220 71 C140 71 60 67 0 63 Z')

def scale_svg():
    # 1 m = 100 units; croc 6 m long, person 1.8 m tall
    ticks = ''.join(f'<line x1="{60+i*100}" y1="236" x2="{60+i*100}" y2="248" stroke="#9DB1A4" stroke-width="2"/>'
                    f'<text x="{60+i*100}" y="270" text-anchor="middle" fill="#9DB1A4" font-family="Inter,sans-serif" font-size="15">{i} m</text>' for i in range(7))
    return f'''<svg viewBox="0 0 760 290" class="info-scale" role="img" aria-label="Scale comparison: a saltwater crocodile can reach 6 metres, more than three times the height of a 1.8 metre adult">
<path d="{CROC_SIDE}" transform="translate(60 150) scale(1 1.4)" fill="#33503D"/>
<path d="M205 48 l9-10 9 10z M236 46 l9-11 9 11z M268 45 l9-11 9 11z M300 44 l9-11 9 11z M332 43 l9-10 9 10z M364 43 l8-9 8 9z M60 57 l6-7 6 7z M90 55 l6-7 6 7z M120 54 l7-8 7 8z M150 52 l7-8 7 8z M178 50 l7-8 7 8z" transform="translate(60 150) scale(1 1.4)" fill="#4A7058"/>
<circle cx="508" cy="206" r="5" fill="#FFC23A"/>
<g transform="translate(690 52)" fill="#E9E1C8"><circle cx="15" cy="14" r="13"/><path d="M2 34 h26 l4 62 h-8 l-3 84 h-8 l-1-70 h-2 l-1 70 h-8 l-3-84 h-8z"/></g>
<line x1="60" y1="242" x2="660" y2="242" stroke="#9DB1A4" stroke-width="2"/>{ticks}
<line x1="740" y1="52" x2="740" y2="232" stroke="#E3B23C" stroke-width="2"/><text x="748" y="148" fill="#E3B23C" font-family="Anton,Impact,sans-serif" font-size="18" transform="rotate(90 748 148)" text-anchor="middle">1.8 M</text>
<text x="60" y="40" fill="#E3B23C" font-family="Anton,Impact,sans-serif" font-size="40">UP TO 6 M</text>
<text x="60" y="66" fill="#C8D3C9" font-family="Inter,sans-serif" font-size="15">Saltwater crocodile — the largest living reptile</text>
</svg>'''

LADDER = [
    ('Avoid', 'Plan the work away from the water’s edge: exclusion zones, timing, camp and access siting.', 'Most preferred'),
    ('Watch', 'Dedicated spotters and overwatch with stop-work authority when crews must be near water.', ''),
    ('Train', 'Toolbox talks and awareness training so every worker recognises and responds to the risk.', ''),
    ('Remove', 'Capture and relocation — only when other controls are impractical, and fully permitted.', 'Last resort'),
]

def ladder_html():
    rows = []
    for i, (t, d, tag) in enumerate(LADDER):
        w = 100 - i * 14
        tag_html = f'<span class="ladder-tag">{tag}</span>' if tag else ''
        rows.append(f'<li class="reveal" style="--w:{w}%"><div class="ladder-bar"><span class="ladder-n">{i+1}</span><strong>{t}</strong>{tag_html}</div><p>{d}</p></li>')
    return '<ol class="ladder">' + ''.join(rows) + '</ol>'

def numbers_html():
    items = [('20+', 'years in the field', 'Working with crocodiles and snakes since 2002'),
             ('3', 'states &amp; territories', 'Northern Territory, Western Australia, Queensland'),
             ('6', 'service lines', 'From overwatch to capture, training and consulting'),
             ('1', 'standard', 'Licensed, insured and documented on every job')]
    return '<div class="grid g4 numbers">' + ''.join(
        f'<div class="number reveal"><div class="ring-wrap"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52" fill="none" stroke="#1E3A2D" stroke-width="10"/>'
        f'<circle cx="60" cy="60" r="52" fill="none" stroke="#E3B23C" stroke-width="10" stroke-linecap="round" stroke-dasharray="{int(326*f)} 400" transform="rotate(-90 60 60)" class="ring"/></svg>'
        f'<span class="display">{n}</span></div><strong>{l}</strong><p>{d}</p></div>'
        for (n, l, d), f in zip(items, (0.9, 0.75, 0.6, 1.0))) + '</div>'

SECTORS = [('Government agencies', 'shield'), ('Mining &amp; resources', 'trap'), ('Construction &amp; infrastructure', 'doc'),
           ('Environmental projects', 'snake'), ('Zoos &amp; wildlife parks', 'eye'), ('Film &amp; TV', 'film')]

def scale_mobile_svg():
    # 6 m = 330 units (55/m); person 1.8 m = 99 units tall
    ticks = ''.join(f'<line x1="{20+i*55}" y1="222" x2="{20+i*55}" y2="234" stroke="#9DB1A4" stroke-width="2"/>' for i in range(7))
    nums = ''.join(f'<text x="{20+i*55}" y="260" text-anchor="middle" fill="#C8D3C9" font-family="Inter,sans-serif" font-size="20">{i}m</text>' for i in (0, 2, 4, 6))
    return f'''<svg viewBox="0 0 400 270" class="info-scale scale-m" role="img" aria-label="Scale comparison: a 6 metre saltwater crocodile beside a 1.8 metre adult">
<path d="{CROC_SIDE}" transform="translate(20 140) scale(.55 1.1)" fill="#6E8F5A" stroke="#0B1611" stroke-width="1.5"/>
<circle cx="266" cy="185" r="5" fill="#FFC23A"/>
<g transform="translate(360 113) scale(.55)" fill="#E9E1C8"><circle cx="15" cy="14" r="13"/><path d="M2 34 h26 l4 62 h-8 l-3 84 h-8 l-1-70 h-2 l-1 70 h-8 l-3-84 h-8z"/></g>
<text x="370" y="100" text-anchor="middle" fill="#E3B23C" font-family="Anton,Impact,sans-serif" font-size="20">1.8m</text>
<line x1="20" y1="228" x2="350" y2="228" stroke="#9DB1A4" stroke-width="2"/>{ticks}{nums}
<text x="20" y="40" fill="#E3B23C" font-family="Anton,Impact,sans-serif" font-size="40">UP TO 6 M</text>
<text x="20" y="68" fill="#C8D3C9" font-family="Inter,sans-serif" font-size="17">Saltwater crocodile vs an adult</text>
</svg>'''

def build_about_page(g):
    icon, page, page_hero, cta_band, HERO = g['icon'], g['page'], g['page_hero'], g['cta_band'], 'assets/media/hero.jpg'
    sectors = ''.join(f'<li class="reveal">{icon(ic, 34)}<span>{name}</span></li>' for name, ic in SECTORS)
    import diagrams
    services = g['SERVICES']
    body = f'''<section class="page-hero scales vhero"><div class="wrap" style="position:relative">
<p class="eyebrow">About us</p><h1 style="max-width:900px">Six lines of defence</h1>
<p class="lead">Since 2002 we’ve kept crews safe in crocodile country. Watch how we do it — the graphics below follow along as each line is explained.</p>
<div style="height:28px"></div>
{diagrams.video_sync_block(services, '')}
</div></section>
''' + f'''
<section class="section" style="background:var(--ink-2)"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">By the numbers</p><h2>CSA at a glance</h2></div>
<p>More than two decades of practical, experience-driven work for the people who build, mine, research and film in crocodile country.</p></div>
{numbers_html()}
</div></section>

<section class="section scales"><div class="wrap split">
<div class="reveal prose"><p class="eyebrow">Where we work</p><h2>Across the north</h2>
<p>Based in Howard Springs, just outside Darwin, we service projects throughout the Northern Territory, Western Australia and Queensland — including remote and fly-in sites.</p>
<ul class="legend"><li><span style="background:#F5CC63"></span>Northern Territory — home base</li><li><span style="background:#E3B23C"></span>Western Australia &amp; Queensland</li><li><span style="background:#1E3A2D;border:1px solid #3A5A4A"></span>Outside regular service area</li></ul></div>
<figure class="info-card reveal">{map_svg()}<figcaption>Service area. Map simplified for illustration.</figcaption></figure>
</div></section>

<section class="section" style="background:var(--ink-2)"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Why it matters</p><h2>Know what you’re working beside</h2></div>
<p>Crocodiles are ambush predators that live in rivers, billabongs, estuaries and coastal waters across the north.</p></div>
<figure class="info-card reveal" style="padding:clamp(18px,3vw,36px)"><div class="scale-d">{scale_svg()}</div>{scale_mobile_svg()}</figure>
<div class="grid g3" style="margin-top:18px">
<div class="card reveal"><span class="display stat-big">~100,000</span><p>estimated saltwater crocodiles in the wild in the Northern Territory</p></div>
<div class="card reveal"><span class="display stat-big">6 m</span><p>maximum length a saltwater crocodile can reach</p></div>
<div class="card reveal"><span class="display stat-big">Night</span><p>is when crocodiles are often most active — and hardest to see</p></div>
</div>
<p class="muted" style="font-size:13px;margin-top:14px">Sources: Northern Territory Government (nt.gov.au) crocodile facts; University of Florida IFAS, <em>Counting and Capturing Crocodilians</em>.</p>
</div></section>

<section class="section scales"><div class="wrap split" style="align-items:flex-start">
<div class="reveal prose"><p class="eyebrow">How we control the risk</p><h2>The CSA control ladder</h2>
<p>We work down the ladder, starting with the least invasive control that keeps people safe. Capture sits at the bottom — it’s the last resort, not the default.</p>
<a class="btn btn-gold" href="services.html">See our services</a></div>
<div>{ladder_html()}</div>
</div></section>

<section class="section" style="background:var(--ink-2)"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Who we work with</p><h2>Trusted by government &amp; industry</h2></div>
<p>Six sectors, one approach: practical controls that fit the way your crew really works.</p></div>
<ul class="sector-grid">{sectors}</ul>
</div></section>

<section class="section sand"><div class="wrap split">
<div class="photo reveal"><img src="{HERO}" alt="Wildlife ranger in a boat on a Top End river with a catching pole" loading="lazy"><div class="photo-badge"><span class="display">2002</span><small>ESTABLISHED</small></div></div>
<div class="reveal"><p class="eyebrow">Our story</p><h2>Practical. Experienced. On site.</h2>
<p style="font-size:18px;margin:24px 0">Crocodile Safety Australia helps government and industry work safely where crocodiles, snakes and other wildlife live. We read the site, understand the animals and design controls that fit the way your crew actually works.</p>
<p>[FOUNDER NAME AND SHORT BIO — background, years handling crocodiles, licences, notable projects]</p>
<h3 style="margin:28px 0 14px;font-size:28px">Credentials</h3>
<ul class="pills"><li>Licensed &amp; insured</li><li>[PERMIT / LICENCE NO.]</li><li>[PUBLIC LIABILITY COVER]</li></ul></div>
</div></section>
''' + cta_band('')
    page('about.html', 'About | Crocodile Safety Australia',
         'Darwin-based wildlife-risk consultancy with 20+ years in the field, servicing the NT, WA and QLD. See where we work and how we control crocodile and snake risk.',
         'About', body)
