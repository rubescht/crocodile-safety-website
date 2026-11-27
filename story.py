"""Chris Peberdy / track record / point of difference — content from crocodilesafety.com.au."""

FOUNDER = 'Chris Peberdy'

# (year label, title, text, icon)
TIMELINE = [
    ('2002', 'CSA established in Darwin', 'Began delivering hands-on wildlife projects and research across Northern Australia.', 'pin'),
    ('2005', 'Alice Springs Reptile Centre', 'An ongoing partnership delivering hundreds of reptile handling and husbandry training programs.', 'cap'),
    ('2006', 'The croc now known as Elvis', 'Captured and relocated a 4.5-metre saltwater crocodile from Darwin, flown to the Australian Reptile Park in Sydney.', 'trap'),
    ('Kakadu', 'Parks Australia SOPs & SWMS', 'Developed, reviewed and enhanced procedures for Kakadu National Park personnel working with crocodiles.', 'doc'),
    ('Film & TV', 'International productions', 'Animal wrangling and safety officer for BBC Top Gear, Animal Planet, National Geographic and 20+ productions.', 'film'),
    ('Today', 'Across NT, WA & QLD', 'Spotting, capture, fauna spotter catcher, feral animal management, consulting and awareness training.', 'shield'),
]

KNOWN_FOR = [
    ('4.5 m', 'saltwater crocodile captured in Darwin and flown to Sydney — now known as Elvis'),
    ('100s', 'of reptile handling and husbandry programs with Alice Springs Reptile Centre'),
    ('1000s', 'of snakes rescued and relocated, and hundreds of crocodiles captured and managed'),
    ('Antivenom', 'venomous snakes collected for the production of life-saving antivenom'),
]

CREDITS = [
    ('BBC', 'Top Gear', 'Animal wrangling & safety officer'),
    ('Animal Planet', 'River Monsters with Jeremy Wade', 'Animal wrangling & safety officer'),
    ('National Geographic', 'Dangerous Encounters with Dr. Brady Barr', 'Animal wrangling & safety officer'),
    ('Wildlife photography', 'Gregory Colbert Australian tour', 'Underwater animal wrangling & site safety'),
    ('Various', '20+ wildlife productions & documentaries', 'Animal handling, risk management & on-site safety'),
]

POD = [
    ('eye', 'In the field since 2002', 'Two decades of hands-on work with crocodiles, snakes and native fauna — not desk-based advice.'),
    ('phone', 'A direct line to the operator', 'You deal with the person who does the work. No call centres, no hand-offs.'),
    ('shield', 'Licensed, insured, WHS-compliant', 'Current licensing and comprehensive insurance, with SOPs, SWMS and risk assessments provided as required.'),
    ('doc', 'Trusted to write the standard', 'Parks Australia engaged us to develop and enhance crocodile SOPs and SWMS for Kakadu National Park.'),
    ('trap', 'Every line of defence, one team', 'Spotting, capture, fauna spotter catchers, feral animals, training and consulting from one provider.'),
    ('film', 'Proven under pressure', 'Trusted on set by the BBC, National Geographic and Animal Planet, where safety can’t be an afterthought.'),
]


def timeline_html(icon):
    items = ''.join(
        f'<li class="tl-item reveal"><span class="tl-dot">{icon(ic, 22)}</span><span class="tl-year">{y}</span>'
        f'<strong>{t}</strong><p>{d}</p></li>' for y, t, d, ic in TIMELINE)
    return f'<ol class="timeline">{items}</ol>'


def known_for_html():
    return '<div class="grid g4 known">' + ''.join(
        f'<div class="known-item reveal"><span class="display">{n}</span><p>{t}</p></div>' for n, t in KNOWN_FOR) + '</div>'


def credits_html():
    return '<ul class="credits">' + ''.join(
        f'<li class="reveal"><span class="cr-net">{a}</span><strong>{b}</strong><small>{c}</small></li>' for a, b, c in CREDITS) + '</ul>'


def pod_html(icon):
    return '<div class="grid g3 pod">' + ''.join(
        f'<div class="card reveal">{icon(ic, 36)}<h3>{t}</h3><p>{d}</p></div>' for ic, t, d in POD) + '</div>'


def chris_section(icon, root=''):
    return f'''<section class="section" id="chris" style="background:var(--ink-2)"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Meet the founder</p><h2>What {FOUNDER} is known for</h2></div>
<p>Chris founded Crocodile Safety Australia in Darwin in 2002. Since then he’s become the person government, industry and film crews call when crocodiles and snakes are part of the job.</p></div>
{known_for_html()}
<h3 class="sub-h" style="margin-top:56px">Two decades in the field</h3>
{timeline_html(icon)}
<p style="margin-top:28px"><a class="btn btn-ghost" href="{root}about.html">Read the full story</a></p>
</div></section>'''


def pod_section(icon, root=''):
    return f'''<section class="section scales" id="why"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Our point of difference</p><h2>Why crews choose CSA</h2></div>
<p>Practical, experience-driven and accountable — so you get reliable, tailored controls that keep people safe and keep the project moving.</p></div>
{pod_html(icon)}
<div class="asseen reveal"><span>Trusted on set by</span><strong>BBC</strong><strong>National Geographic</strong><strong>Animal Planet</strong><a href="{root}film-television.html">See credits →</a></div>
</div></section>'''
