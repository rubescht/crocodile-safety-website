#!/usr/bin/env python3
"""Builds the Crocodile Safety Australia static site into ./dist."""
import json, os, shutil, html
import hashlib as _hl, pathlib as _pl
ASSET_V = _hl.md5(b"".join(_pl.Path(__file__).with_name("src").joinpath("assets", f).read_bytes() for f in ("styles.css", "main.js"))).hexdigest()[:8]
import diagrams
import story

SRC = os.path.join(os.path.dirname(__file__), 'src')
DIST = os.path.join(os.path.dirname(__file__), 'dist')
SITE = 'https://www.crocodilesafety.com.au'
PHONE = '0409 326 307'
TEL = 'tel:0409326307'
EMAIL = 'Chris@crocodilesafety.com.au'
POBOX = 'PO Box 1546, Howard Springs NT 0835'
HERO_MP4_CDN = 'https://cdn.creativeclaw.co/u/48eaa2c1/videos/68b182a8-f0cd-4dfe-a70f-ccfaeaf1f7bc.mp4'
HERO_POSTER_CDN = 'https://cdn.creativeclaw.co/u/48eaa2c1/images/de1fdcf4-3008-4f37-bacc-2dfa10351fca.jpg'

ICONS = {
 'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><path d="M12 8v8"/>',
 'trap': '<rect x="3" y="7" width="18" height="10" rx="2"/><path d="M7 7v10M11 7v10M15 7v10M19 7v10"/>',
 'snake': '<path d="M4 18c3 0 3-4 6-4s3 4 6 4 3-6 4-8"/><circle cx="19" cy="7" r="2"/>',
 'shield': '<path d="M12 3l8 4v5c0 5-4 8-8 9-4-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/>',
 'cap': '<path d="M3 7l9-4 9 4-9 4z"/><path d="M7 9v5c0 2 2 3 5 3s5-1 5-3V9"/>',
 'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/>',
 'film': '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M7 6l2 4M12 6l2 4M17 6l2 4"/>',
 'phone': '<path d="M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}
def icon(name, size=40):
    return (f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="#E3B23C" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

CROC_SVG = ('<svg class="card-croc" viewBox="0 0 600 80" aria-hidden="true"><path d="M0 60 C60 56 140 52 220 48 C290 44 350 42 400 44 '
            'L428 44 C436 32 452 30 464 42 L500 46 C540 48 575 52 600 58 C580 65 540 67 500 67 L220 71 C140 71 60 67 0 63 Z" fill="#33503D"/>'
            '<path d="M205 48 l9-10 9 10z M236 46 l9-11 9 11z M268 45 l9-11 9 11z M300 44 l9-11 9 11z M332 43 l9-10 9 10z" fill="#3E6049"/>'
            '<circle cx="448" cy="40" r="5" fill="#FFC23A"/></svg>')

LOGO = ('<svg width="46" height="46" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="none" stroke="#E3B23C" stroke-width="2.5"/>'
        '<path d="M6 24c6-9 30-9 36 0-6 9-30 9-36 0z" fill="#E3B23C"/><rect x="22" y="15" width="4" height="18" rx="2" fill="#07150F"/></svg>')

TEETH = ('<svg class="teeth" viewBox="0 0 1440 24" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0H1440V4' +
         ''.join(f'L{1440-20*(i+1)} {22 if i%2==0 else 4}' for i in range(72)) + 'Z" fill="#07150F"/></svg>')

# ---------------------------------------------------------------- services
SERVICES = [
 dict(slug='crocodile-capture-relocation', where='On the water — the last resort when a crocodile can’t be managed in place', name='Crocodile Capture & Relocation', icon='trap',
  short='When other controls are impractical, we trap and relocate problem crocodiles — assessed case by case and fully permitted.',
  intro='Sometimes a crocodile and a work site simply can’t share the same stretch of water. When spotting, exclusion and work-practice controls aren’t practical, our team removes the risk by capturing and relocating the animal — safely for your people and humanely for the crocodile.',
  includes=['Site inspection and assessment of the animal, its behaviour and the risk it poses',
            'Liaison on the permits and approvals required before any capture',
            'Trap deployment, monitoring and checking to an agreed schedule',
            'Hand, noose and trap capture by experienced operators',
            'Safe restraint, transport and relocation or hand-over as directed by the relevant authority',
            'A written job report for your records and HSE system'],
  when=['A crocodile is regularly sighted where people work, fish, swim or launch boats',
        'A crocodile is trapped or stranded in a pond, dam, drain or water-storage facility',
        'Works must proceed in or beside water and the animal can’t be safely managed in place',
        'Your risk assessment has ruled out lower-level controls'],
  faqs=[('Is capture always the answer?', 'No. Capture is a last resort. We start with a risk assessment and recommend the least invasive control that keeps people safe — often overwatch, exclusion zones or changed work practices.'),
        ('Do you need a permit to remove a crocodile?', 'Crocodiles are protected wildlife, so removal is controlled under state and territory law. We work within the approvals framework and help you arrange what’s required before any capture.'),
        ('How long does a capture take?', 'It depends on the animal, the site and the method. Some captures happen in a single session; trapping can take days of monitoring. We’ll give you an honest plan after the site assessment.')]),
 dict(slug='crocodile-spotting-overwatch', where='On the bank — eyes on the water while crews work', name='Crocodile Spotting & Safety Overwatch', icon='eye',
  short='Trained operators watch the water and banks so crews can work near croc habitat with eyes on every threat.',
  intro='The Northern Territory’s crocodile population has recovered strongly — a great conservation success, but more chance of human–crocodile encounters for crews in remote areas and on waterways. Our safety overwatch operators keep dedicated, uninterrupted eyes on the water and banks while your crew focuses on the job, with clear stop-work authority and communication protocols agreed before work starts. Armed safety overwatch is available where the risk requires it.',
  includes=['Dedicated spotters positioned for clear sight lines over water and banks',
            'Pre-start briefings on crocodile behaviour, warning signs and site rules',
            'Agreed alert, stop-work and evacuation protocols with your supervisors',
            'Day and night spotting, including spotlight surveys for eyeshine',
            'Monitoring of tides, water levels and conditions that change the risk',
            'Daily observation logs for your HSE records'],
  when=['Geotechnical drilling, survey or sampling at or near water',
        'Bridge, culvert, causeway, wharf and boat-ramp construction or maintenance',
        'Pipeline, cable and dredging works crossing rivers, creeks and floodplains',
        'Environmental monitoring, water sampling and field research'],
  faqs=[('Why not just have a crew member keep watch?', 'A spotter who is also doing their own job is not watching the water. Dedicated, trained overwatch removes that distraction and brings experience in reading crocodile behaviour and habitat.'),
        ('Do you work at night?', 'Yes. Crocodiles are often most active after dark, and spotlight surveys for eyeshine are a standard part of night-time overwatch.'),
        ('Can you work on remote sites?', 'Yes. We service projects across the Northern Territory, Western Australia and Queensland, including remote and fly-in sites.')]),
 dict(slug='fauna-spotter-catcher', where='Beside the machinery — snakes and fauna during clearing', name='Fauna Spotter Catcher Services', icon='snake',
  short='Onsite snake and fauna capture and relocation for construction, infrastructure, mining and environmental works.',
  intro='Clearing, earthworks and construction disturb wildlife — and bring snakes and other fauna into contact with your crew. Our highly trained team has extensive experience with the safe capture and relocation of venomous snakes, crocodiles and other native fauna. Our licensed spotter catchers work ahead of and alongside machinery to find, capture and relocate animals so works stay safe, compliant and moving.',
  includes=['Pre-clearing fauna surveys and inspection of hollows, logs and burrows',
            'Spotter catchers working alongside clearing and earthworks crews',
            'Safe capture and relocation of snakes, lizards, frogs, birds and mammals',
            'Call-out response to snakes in site offices, crib rooms and plant',
            'Fauna handling records and reports to support your environmental approvals'],
  when=['Vegetation clearing, grubbing and bulk earthworks',
        'Road, rail, pipeline, transmission and other linear infrastructure',
        'Mine site expansions, rehabilitation and camp works',
        'Projects whose environmental approvals require a fauna spotter catcher'],
  faqs=[('Are your spotter catchers licensed?', 'Yes. Every service is backed by current licensing, comprehensive insurance and compliance with Work Health and Safety obligations, with SOPs, SWMS and risk assessments provided as required.'),
        ('Do you handle venomous snakes?', 'Yes. Venomous snake capture and relocation is a core part of the service, carried out by experienced handlers with the right equipment.'),
        ('Can you provide records for our approvals?', 'Yes. We keep fauna encounter and relocation records and can supply reports for your environmental management plan.')]),
 dict(slug='feral-animal-management', where='In the surrounding land — licensed control programs', name='Feral Animal Management', icon='shield',
  short='Licensed, insured feral animal control programs across the Northern Territory.',
  intro='Feral animals damage infrastructure, degrade habitat and create safety risks on properties and project sites. We deliver licensed, insured feral animal management programs tailored to your land, your objectives and your obligations.',
  includes=['Assessment of feral animal activity, impacts and risks on your site',
            'A management program matched to your objectives and regulations',
            'Licensed control activities carried out to the relevant codes of practice',
            'Monitoring to measure results over time',
            'Reporting for landholders, managers and agencies'],
  when=['Pastoral, conservation and Indigenous land managers',
        'Mine sites, camps and infrastructure corridors',
        'Government agencies and councils',
        'Properties where feral animals threaten people, stock or assets'],
  faqs=[('Which animals do you manage?', 'Tell us what you’re dealing with. Every strategy is tailored to the site, the operating environment and the animal species involved.'),
        ('Where do you operate?', 'Feral animal management is delivered across the Northern Territory.'),
        ('Are programs humane?', 'Yes. Programs are carried out by licensed operators in line with the relevant codes of practice for humane control.')]),
 dict(slug='awareness-training', where='With the crew — toolbox talks and site briefings', name='Crocodile & Snake Awareness Training', icon='cap',
  short='Onsite training, toolbox talks and site briefings that keep crews croc-wise and snake-safe.',
  intro='Most wildlife incidents are avoidable. Our awareness training gives workers the knowledge to recognise crocodile and snake risk, change how they work around water and bush, and respond correctly if something goes wrong — delivered onsite, in plain language, by people who work with these animals every day.',
  includes=['Crocodile biology, behaviour and habitat — where and when the risk is highest',
            'Safe work practices near water: distances, boat and vehicle use, camp siting',
            'Snake identification, avoidance and what to do in an encounter',
            'Snakebite first-aid awareness and emergency response planning',
            'Toolbox talks and site inductions tailored to your project',
            'Attendance records for your training register'],
  when=['Site inductions for new crews and contractors',
        'Before works start near water or in crocodile habitat',
        'Wet-season refreshers when conditions change',
        'Any organisation whose people work where crocodiles and venomous snakes may be present'],
  faqs=[('How long is a session?', 'Anything from a toolbox talk or safety briefing to a site-specific presentation or comprehensive awareness course — tailored to your operational environment, workforce experience and risk profile.'),
        ('Do you come to our site?', 'Yes. Training is delivered onsite so it can reflect the real conditions your crew works in.'),
        ('Is training enough on its own?', 'Training is a key control, but on high-risk water sites it works best alongside overwatch and good work-practice controls.')]),
 dict(slug='wildlife-consulting', where='In the site office — SOPs, SWMS and risk assessments', name='Wildlife Consulting', icon='doc',
  short='SOP and SWMS development, captive husbandry advice and specialist training for parks, zoos and government agencies.',
  intro='Good wildlife-risk management starts on paper. Since 2002 our work has included collecting venomous snakes for the production of life-saving antivenom, rescuing and relocating thousands of snakes, and capturing and managing hundreds of crocodiles — and we worked with Parks Australia to develop, review and enhance SOPs and SWMS for Kakadu National Park personnel working with crocodiles.',
  includes=['Standard operating procedures (SOPs) for wildlife handling and response',
            'Safe work method statements (SWMS) for works in crocodile habitat',
            'Wildlife risk assessments for projects, sites and events',
            'Captive crocodile and reptile husbandry advice for parks and zoos',
            'Specialist handler training for staff and agency teams',
            'Expert advice for tenders, approvals and management plans'],
  when=['Wildlife parks, zoos and sanctuaries',
        'Government agencies and councils',
        'Principal contractors writing project HSE documentation',
        'Organisations reviewing procedures after an incident or near miss'],
  faqs=[('Can you write SWMS for our project?', 'Yes. We prepare SWMS and risk assessments for works in and around crocodile and snake habitat, tailored to your site and methods.'),
        ('Do you train zoo and park staff?', 'Yes. We provide specialist training and husbandry advice for teams that keep and handle crocodiles and reptiles.'),
        ('Can you support a tender?', 'Yes. We can contribute wildlife-risk methodology and documentation to support your tender or approvals.')]),
]

NAV = [('Home', 'index.html'), ('About', 'about.html'), ('Services', 'services.html'),
       ('Film & Television', 'film-television.html'), ('Contact', 'contact.html')]

def head(title, desc, path, root, extra=''):
    url = SITE + '/' + ('' if path == 'index.html' else path)
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#07150F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Crocodile Safety Australia">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/media/hero.jpg">
<link rel="icon" href="{root}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/styles.css?v={ASSET_V}">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(active, root, solid=True):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if label == active else ''
        if label == 'Services':
            drop = ''.join(f'<li><a href="{root}services/{s["slug"]}.html">{html.escape(s["name"])}</a></li>' for s in SERVICES)
            items.append(f'<li class="has-drop"><button type="button" aria-expanded="false" aria-haspopup="true">Services '
                         f'<svg width="12" height="12" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.5"/></svg></button>'
                         f'<ul class="drop"><li><a href="{root}services.html"{cur}><strong>All services</strong></a></li>{drop}</ul></li>')
        else:
            items.append(f'<li><a href="{root}{href}"{cur}>{html.escape(label)}</a></li>')
    return f'''<header class="site-header{' solid' if solid else ''}">
<div class="wrap nav">
<a class="brand" href="{root}index.html" aria-label="Crocodile Safety Australia – home"><span class="logo-anim" aria-hidden="true"><img class="logo-sign" src="{root}assets/logo-sign.png" alt="" width="80" height="83"><img class="logo-words" src="{root}assets/logo-words.png" alt="" width="116" height="83"><svg class="logo-bite" viewBox="0 0 196 83" preserveAspectRatio="none" aria-hidden="true"><g class="lb-rock"><polygon points="40,3 78,41.5 40,80 2,41.5" fill="#231F20"/><polygon points="40,10 71,41.5 40,73 9,41.5" fill="#fff"/><g class="lb-croc"><g class="lb-lower"><path d="M15 49 L64 47 C67 47 68 50 66 52 L20 57 Z" fill="#231F20"/><path d="M28 48 l3 -4 3 4z M38 47.6 l3 -4 3 4z M48 47.2 l3 -4 3 4z M57 46.8 l3 -4 3 4z" fill="#fff"/></g><g class="lb-upper"><path d="M10 44 C14 36 22 33 28 32 C30 27 36 26 38 31 L60 35 C66 36 71 39 72 42 C72 45 68 46 64 46 L14 49 Z" fill="#231F20"/><path d="M26 46 l3 4 3 -4z M36 45.6 l3 4 3 -4z M46 45.2 l3 4 3 -4z M56 44.8 l3 4 3 -4z" fill="#fff"/><circle cx="33" cy="33" r="1.8" fill="#F9C606"/></g><g class="lb-rope"><path d="M58 40 C40 10 30 -20 18 -60" fill="none" stroke="#C9A26B" stroke-width="2.4" stroke-linecap="round"/><ellipse cx="60" cy="45" rx="5" ry="9" fill="none" stroke="#C9A26B" stroke-width="2.6"/></g></g></g></svg></span></a>
<nav aria-label="Main"><ul class="menu" id="site-menu">{''.join(items)}</ul></nav>
<div class="nav-cta">
<a class="nav-phone" href="{TEL}">{PHONE}</a>
<a class="btn btn-gold" href="{root}contact.html" style="min-height:46px;padding:12px 22px">Enquire</a>
<button class="nav-toggle" type="button" aria-controls="site-menu" aria-expanded="false" aria-label="Open menu"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
</div>
</div>
</header>
'''

def footer(root):
    svc = ''.join(f'<li><a href="{root}services/{s["slug"]}.html">{html.escape(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer">
{TEETH}
<div class="wrap footer-grid">
<div><span class="logo-anim footer-logo" role="img" aria-label="Crocodile Safety Australia"><img class="logo-sign" src="{root}assets/logo-sign.png" alt="" width="80" height="83" loading="lazy"><img class="logo-words" src="{root}assets/logo-words.png" alt="" width="116" height="83" loading="lazy"></span>
<p>Specialist wildlife-risk management for government and industry across the NT, WA and QLD.</p>
<p><a class="btn btn-gold" href="{root}contact.html">Enquire now</a></p></div>
<div><h4>Navigation</h4><ul>{''.join(f'<li><a href="{root}{h}">{html.escape(l)}</a></li>' for l, h in NAV)}</ul></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Contact</h4><ul>
<li><a href="{TEL}">{PHONE}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>{POBOX}</li>
<li>Servicing NT · WA · QLD</li></ul></div>
</div>
<div class="wrap footer-base"><span>© <span id="year">2026</span> Crocodile Safety Australia · Licensed &amp; insured</span><span>If someone is in immediate danger, call 000.</span></div>
</footer>
<div class="callbar"><a class="btn btn-gold" href="{TEL}">Call now</a><a class="btn btn-ghost" href="{root}contact.html">Enquire</a></div>
<script src="{root}assets/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''

def service_options(selected=''):
    opts = [s['name'] for s in SERVICES] + ['Film & Television', 'Something else']
    return ''.join(f'<option{" selected" if o == selected else ""}>{html.escape(o)}</option>' for o in opts)

def enquiry_form(root, selected='', compact=False):
    extra = '' if compact else ('<label>Email<input type="email" name="Email" autocomplete="email"></label>'
                                '<label>Site location<input type="text" name="Location" placeholder="e.g. Adelaide River, NT"></label>')
    details = '' if compact else '<label class="full">Project details<textarea name="Details" placeholder="Dates, crew size, work near water, what you’ve seen…"></textarea></label>'
    return f'''<form class="form{' quick-form' if compact else ''}" data-enquiry action="https://formspree.io/f/YOUR-FORM-ID" method="POST">
<label>Name<input type="text" name="Name" autocomplete="name" required></label>
<label>Organisation<input type="text" name="Organisation" autocomplete="organization"></label>
<label>Phone<input type="tel" name="Phone" autocomplete="tel" required></label>
{extra}
<label{' class="full"' if compact else ''}>Service<select name="Service">{service_options(selected)}</select></label>
{details}
<button class="btn btn-gold" type="submit">{'Request a call back' if compact else 'Send enquiry'}</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form>'''

def cta_band(root, title='Working in croc country?', text='Tell us about your site and we’ll come back with a plan — or call now for an urgent call-out.'):
    return f'''<section class="cta-band"><div class="eye-deco" aria-hidden="true"></div><div class="wrap"><div class="inner reveal">
<p class="eyebrow">Get in touch</p><h2>{title}</h2>
<p class="lead" style="margin:22px 0 32px">{text}</p>
<div class="btn-row"><a class="btn btn-gold" href="{TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="{root}contact.html">Send an enquiry</a></div>
</div></div></section>'''

def service_cards(root, feature_first=True):
    out = []
    for i, s in enumerate(SERVICES):
        href = f'{root}services/{s["slug"]}.html'
        if i == 0 and feature_first:
            out.append(f'<a href="{href}" class="card card-feature span2 reveal">{CROC_SVG}<span class="num">0{i+1}</span><h3>{html.escape(s["name"])}</h3><p>{html.escape(s["short"])}</p><span class="more">Explore service →</span></a>')
        else:
            span = ' span2' if (feature_first and i == 5) else ''
            out.append(f'<a href="{href}" class="card{span} reveal"><span class="num">0{i+1}</span>{icon(s["icon"])}<h3>{html.escape(s["name"])}</h3><p>{html.escape(s["short"])}</p><span class="more">Explore →</span></a>')
    return '<div class="grid g3">' + ''.join(out) + '</div>'

STEPS = [('Assess', 'Site visit, habitat review and a clear read of the wildlife risk.'),
         ('Plan', 'SOPs and SWMS written for your site, your crew and your permits.'),
         ('Control', 'Overwatch, spotter catchers or capture — matched to the risk.'),
         ('Brief', 'Toolbox talks and training so crews stay croc-wise.')]
def steps_html():
    return '<div class="grid g4">' + ''.join(f'<div class="step reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in STEPS) + '</div>'

SECTORS = '''<div class="sectors"><div class="wrap"><strong>Trusted by</strong><span>Government agencies</span><span>Mining &amp; resources</span><span>Construction &amp; infrastructure</span><span>Environmental projects</span><span>Zoos &amp; wildlife parks</span><span>Film &amp; TV</span></div></div>'''

MARQUEE_ITEMS = ['Saltwater crocs grow up to 6 m', '~100,000 salties in the NT wild', '20+ years in the field', 'Licensed &amp; insured', 'NT · WA · QLD']
MARQUEE = ('<div class="marquee" aria-hidden="true"><div class="marquee-track">' +
           ''.join(f'<span>{m}</span><span>✦</span>' for m in MARQUEE_ITEMS * 2) + '</div></div>')

UPCOMING_VIDEOS = [('Night spotlight survey', 'Reading eyeshine'), ('King brown on a building site', 'Snake capture'),
                   ('Python &amp; monitor relocation', 'Mine site'), ('Freshie hand capture &amp; release', 'Capture')]

def page(path, title, desc, active, body, root='', solid=True, extra_head=''):
    out = head(title, desc, path, root, extra_head) + header(active, root, solid) + f'<main id="main">{body}</main>' + footer(root)
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(out)

def page_hero(eyebrow, title, lead, crumbs=None, eye=True):
    c = f'<p class="crumbs">{crumbs}</p>' if crumbs else ''
    return f'''<section class="page-hero scales">{'<div class="eye-deco" aria-hidden="true"></div>' if eye else ''}<div class="wrap" style="position:relative">{c}<p class="eyebrow">{eyebrow}</p><h1 style="max-width:860px">{title}</h1><p class="lead">{lead}</p></div></section>'''

# ---------------------------------------------------------------- pages
def build_home():
    root_img=''
    schema = {
        '@context': 'https://schema.org', '@type': 'LocalBusiness', 'name': 'Crocodile Safety Australia',
        'description': 'Specialist crocodile, snake and wildlife-risk management for government and industry across Northern Australia.',
        'url': SITE, 'telephone': '+61 409 326 307', 'email': EMAIL, 'image': SITE + '/assets/media/hero.jpg', 'logo': SITE + '/assets/logo.png',
        'address': {'@type': 'PostalAddress', 'postOfficeBoxNumber': '1546', 'addressLocality': 'Howard Springs', 'addressRegion': 'NT', 'postalCode': '0835', 'addressCountry': 'AU'},
        'areaServed': ['Northern Territory', 'Western Australia', 'Queensland'],
        'foundingDate': '2002',
        'makesOffer': [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['name']}} for s in SERVICES],
    }
    extra = f'<script type="application/ld+json">{json.dumps(schema)}</script>\n'
    vids = ''.join(f'<div class="card vid reveal"><div class="thumb">{icon("film", 34)}Coming soon</div><div class="vid-body"><strong>{t}</strong><span class="muted" style="font-size:13px">{s}</span></div></div>' for t, s in UPCOMING_VIDEOS)
    body = f'''
<section class="hero">
<div class="hero-media">
<video autoplay muted loop playsinline preload="metadata" poster="assets/media/night-hero.jpg" aria-hidden="true">
<source src="assets/media/night-hero.mp4" type="video/mp4">
</video>
<button class="video-toggle" type="button" aria-label="Pause background video"></button>
<span class="hero-note">Illustrative footage</span>
</div>
<div class="wrap hero-body">
<p class="eyebrow">Northern Australia · Since 2002</p>
<h1>We handle what<br><span>lurks below.</span></h1>
<p class="lead">Specialist crocodile, snake and wildlife-risk management for government and industry across the NT, WA and QLD — led by Chris Peberdy, in the field since 2002.</p>
<div class="btn-row"><a class="btn btn-gold hero-enquire" href="contact.html">Enquire now</a><a class="btn btn-ghost hero-watch" href="#capture-files" data-watch><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4l13 8-13 8z" fill="#E3B23C"/></svg><span class="m-hide">Watch the film with sound</span><span class="m-show">1-min video: keeping crews croc-safe</span></a></div>
</div>
</section>
{MARQUEE}
<section class="section" id="capture-files" style="background:var(--ink-2)">
<div class="wrap">
<div class="section-head"><div><p class="eyebrow">The capture files</p><h2>Six lines in 60 seconds</h2></div>
<p>See how each line of defence works on a real Top End project — from eyes on the water to the procedures behind them.</p></div>
{diagrams.explainer('')}
</div></section>
{story.chris_section(icon)}
{story.pod_section(icon)}
<section class="section scales" id="services">
<div class="wrap">
<div class="section-head"><div><p class="eyebrow">What we do</p><h2>Six lines of defence</h2></div>
<p>Every job starts with a site risk assessment. We choose the least invasive control that keeps your people safe — capture is the last resort, not the default.</p></div>
{diagrams.section_block(SERVICES, '')}
<div style="height:40px"></div>
{service_cards('')}
</div></section>
{SECTORS}

<section class="section scales">
<div class="wrap">
<p class="eyebrow">How we work</p><h2 style="margin-bottom:50px">Assess. Plan. Control. Brief.</h2>
{steps_html()}
</div></section>
<section class="section sand">
<div class="wrap split">
<div class="photo reveal"><img src="{root_img}assets/media/hero.jpg" alt="Wildlife ranger in a boat holding a catching pole as a saltwater crocodile approaches" loading="lazy">
<div class="photo-badge"><span class="display">20+</span><small>YEARS IN THE FIELD</small></div></div>
<div class="reveal">
<p class="eyebrow">About CSA</p><h2>Field-tested. Trusted by government &amp; industry.</h2>
<p style="font-size:18px;margin:26px 0">Founded by Chris Peberdy in Darwin in 2002, Crocodile Safety Australia delivers hands-on wildlife projects, research and safety services to government agencies, industry and non-government organisations across the Northern Territory, Western Australia and Queensland.</p>
<ul class="pills" style="margin-bottom:28px"><li>Licensed &amp; insured</li><li>Est. 2002</li><li>Howard Springs NT</li></ul>
<a class="btn btn-dark" href="about.html">Our story</a>
</div></div></section>
<section class="section" style="background:radial-gradient(circle at 80% 50%,#1A3F2F,var(--ink-2) 60%);position:relative;overflow:hidden">
<div class="eye-deco" aria-hidden="true"></div>
<div class="wrap" style="position:relative"><div style="max-width:640px" class="reveal">
<p class="eyebrow">Film &amp; Television</p><h2>Crocs on set. Crew safe.</h2>
<p class="lead" style="margin:24px 0 32px">Wildlife safety for productions filming in crocodile country — from location risk assessments to on-water overwatch.</p>
<a class="btn btn-gold" href="film-television.html">Film &amp; TV services</a></div></div></section>
<section class="section scales" id="contact">
<div class="wrap split" style="align-items:flex-start">
<div class="reveal"><p class="eyebrow">Contact</p><h2>Working in croc country?</h2>
<p class="lead" style="margin:24px 0 30px">Call for urgent call-outs, or send your site details and we’ll come back with a plan.</p>
<a class="contact-big" href="{TEL}">{PHONE}</a>
<div class="contact-list"><a href="mailto:{EMAIL}" style="color:#fff;font-weight:600">{EMAIL}</a><span>{POBOX}</span><span>Northern Territory · Western Australia · Queensland</span></div></div>
<div class="reveal">{enquiry_form('')}</div>
</div></section>
'''
    page('index.html', 'Crocodile Safety Australia | Crocodile, Snake & Wildlife-Risk Management',
         'Specialist crocodile, snake and wildlife-risk management for government and industry across the NT, WA and QLD. Licensed and insured, 20+ years in the field.',
         'Home', body, solid=False, extra_head=extra)

def build_about():
    root_img=''
    body = page_hero('About us', 'Field-tested since 2002', 'A Darwin-based wildlife-risk consultancy built on more than 20 years of hands-on work with crocodiles, snakes and the crews who share their habitat.') + f'''
<section class="section">
<div class="wrap split">
<div class="prose reveal">
<h2>Practical. Experienced. On site.</h2>
<p>Crocodile Safety Australia (CSA) helps government and industry work safely where crocodiles, snakes and other wildlife live. Our approach is practical and experience-driven: we read the site, understand the animals and design controls that fit the way your crew actually works.</p>
<p>We’re trusted by government agencies, mining and resources companies, construction and infrastructure contractors, environmental consultants, wildlife parks and film productions across the Northern Territory, Western Australia and Queensland.</p>
<p>[FOUNDER NAME AND SHORT BIO — background, years handling crocodiles, licences, notable projects]</p>
</div>
<div class="photo reveal"><img src="{root_img}assets/media/hero.jpg" alt="Wildlife ranger in a boat on a Top End river with a catching pole" loading="lazy"><div class="photo-badge"><span class="display">20+</span><small>YEARS IN THE FIELD</small></div></div>
</div></section>
<section class="section scales">
<div class="wrap">
<p class="eyebrow">What we stand for</p><h2 style="margin-bottom:44px">How we do the job</h2>
<div class="grid g3">
<div class="card reveal">{icon('shield')}<h3>People first</h3><p>Every decision starts with keeping your crew, contractors and the public safe.</p></div>
<div class="card reveal">{icon('eye')}<h3>Least invasive control</h3><p>We match the control to the risk. Capture is a last resort, not the default.</p></div>
<div class="card reveal">{icon('doc')}<h3>Done properly</h3><p>Licensed, insured and documented — so your HSE and approvals are covered.</p></div>
</div></div></section>
<section class="section" style="background:var(--ink-2)">
<div class="wrap">
<div class="grid g4">
<div class="stat reveal"><span class="display">20+</span><p>Years in the field</p></div>
<div class="stat reveal"><span class="display">2002</span><p>Established</p></div>
<div class="stat reveal"><span class="display">3</span><p>States &amp; territories served</p></div>
<div class="stat reveal"><span class="display">6</span><p>Specialist service lines</p></div>
</div></div></section>
<section class="section">
<div class="wrap split" style="align-items:flex-start">
<div class="prose reveal"><p class="eyebrow">Credentials</p><h2>Licensed &amp; insured</h2>
<p>Our operators are licensed and insured for crocodile, snake and fauna work. Details are available on request for your contractor pre-qualification.</p>
<ul class="ticks"><li>[ADD WILDLIFE / PERMIT LICENCE NUMBERS]</li><li>[ADD PUBLIC LIABILITY COVER AMOUNT]</li><li>[ADD FIRST AID / HSE QUALIFICATIONS]</li></ul></div>
<div class="prose reveal"><p class="eyebrow">Where we work</p><h2>Across the north</h2>
<p>Based in Howard Springs, just outside Darwin, we service projects throughout the Top End and beyond — including remote and fly-in sites.</p>
<ul class="pills light"><li>Northern Territory</li><li>Western Australia</li><li>Queensland</li></ul></div>
</div></section>
''' + cta_band('')
    page('about.html', 'About | Crocodile Safety Australia',
         'Darwin-based wildlife-risk consultancy with 20+ years in the field. Licensed and insured crocodile, snake and fauna specialists servicing the NT, WA and QLD.',
         'About', body)

def build_services():
    body = page_hero('Services', 'Six lines of defence', 'From eyes on the water to capture and relocation — wildlife-risk controls matched to your site, your crew and your approvals.') + f'''
<section class="section scales"><div class="wrap"><div class="section-head"><div><p class="eyebrow">On site</p><h2>Where each line works</h2></div><p>Six services, each covering a different part of the risk — from the water’s edge to the site office.</p></div>{diagrams.section_block(SERVICES, '')}<div style="height:40px"></div>{diagrams.explainer('')}<div style="height:56px"></div>{service_cards('')}</div></section>
<section class="section" style="background:var(--ink-2)"><div class="wrap">
<p class="eyebrow">Our approach</p><h2 style="margin-bottom:50px">Assess. Plan. Control. Brief.</h2>{steps_html()}</div></section>
{SECTORS}
''' + cta_band('', 'Not sure what you need?', 'Tell us about the site and the work. We’ll recommend the right mix of controls — no more, no less.')
    page('services.html', 'Services | Crocodile Safety Australia',
         'Crocodile capture and relocation, safety overwatch, fauna spotter catchers, feral animal management, awareness training and wildlife consulting across Northern Australia.',
         'Services', body)

def build_service(s):
    root = '../'
    others = ''.join(f'<a href="{o["slug"]}.html"><span>{html.escape(o["name"])}</span><span aria-hidden="true">→</span></a>' for o in SERVICES if o is not s)
    faqs = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in s['faqs'])
    body = page_hero('Service', html.escape(s['name']), html.escape(s['short']),
                     crumbs=f'<a href="../index.html">Home</a> / <a href="../services.html">Services</a> / {html.escape(s["name"])}') + f'''
<section class="section"><div class="wrap layout-aside">
<div class="main prose">
<p style="font-size:19px;color:var(--text)">{html.escape(s['intro'])}</p>
<h2 style="margin-top:44px">What’s included</h2>
<ul class="ticks">{''.join(f'<li>{html.escape(x)}</li>' for x in s['includes'])}</ul>
<h2 style="margin-top:52px">When you need it</h2>
<div class="grid g2">{''.join(f'<div class="card" style="padding:22px">{icon(s["icon"], 30)}<p style="color:var(--soft)">{html.escape(x)}</p></div>' for x in s['when'])}</div>
<h2 style="margin-top:52px">How it works</h2>
{diagrams.service_diagram(s['slug'])}
<h2 style="margin-top:52px">Questions</h2>
<div class="faq">{faqs}</div>
</div>
<aside><div class="aside-box">
<h3>Talk to a specialist</h3>
<p class="muted">Call for urgent jobs, or send an enquiry and we’ll come back with a plan.</p>
<p><a class="contact-big" style="font-size:40px" href="{TEL}">{PHONE}</a></p>
{enquiry_form(root, s['name'], compact=True)}
<div class="related" style="margin-top:28px"><h4 style="color:#fff;margin:0 0 6px">Other services</h4>{others}</div>
</div></aside>
</div></section>
''' + cta_band(root)
    page(f'services/{s["slug"]}.html', f'{s["name"]} | Crocodile Safety Australia',
         s['short'] + ' Servicing the NT, WA and QLD.', 'Services', body, root=root)

def build_film():
    body = page_hero('Film &amp; Television', 'Crocs on set.<br>Crew safe.', 'Specialist animal wrangling and on-set safety for major international productions — trusted by the BBC, National Geographic and Animal Planet.') + f'''
<section class="section"><div class="wrap split" style="align-items:flex-start">
<div class="prose reveal">
<h2>Get the shot. Keep everyone safe.</h2>
<p>Our expertise extends well beyond crocodile and reptile management. Crocodile Safety Australia has provided professional animal wrangling and safety officer services for major international television and wildlife productions across Australia.</p>
<p>We’re an established, trusted partner for film, television, documentary and wildlife productions that need specialist animal handling, risk management and on-site safety expertise.</p>
</div>
<div class="reveal"><ul class="ticks">
<li>Professional animal wrangling — crocodiles, venomous snakes and native fauna</li>
<li>Dedicated safety officer services for cast and crew</li>
<li>Underwater animal wrangling and aquatic site safety</li>
<li>Risk assessment and SWMS for wildlife-involved productions</li>
<li>Liaison with relevant wildlife authorities and permit management</li>
<li>Remote and regional location support across Northern Australia</li>
</ul></div>
</div></section>
<section class="section" style="background:var(--ink-2)"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Production credits</p><h2>Selected productions</h2></div><p>Animal wrangling, safety officer and on-site safety services for international film, television and photography projects.</p></div>
{story.credits_html()}
</div></section>
<section class="section scales"><div class="wrap">
<p class="eyebrow">For productions</p><h2 style="margin-bottom:44px">From recce to wrap</h2>
<div class="grid g4">
<div class="step reveal"><h3>Recce</h3><p>We assess locations and flag wildlife risk before you commit.</p></div>
<div class="step reveal"><h3>Plan</h3><p>Risk assessments and procedures your insurer and HSE will accept.</p></div>
<div class="step reveal"><h3>Shoot</h3><p>Dedicated overwatch and safety officers on set and on the water.</p></div>
<div class="step reveal"><h3>Wrap</h3><p>Records and reporting for your production files.</p></div>
</div></div></section>
''' + cta_band('', 'Shooting up north?', 'Tell us your locations and dates and we’ll put together a wildlife-safety plan for your production.')
    page('film-television.html', 'Film & Television | Crocodile Safety Australia',
         'Animal wrangling and on-set safety for film and TV in crocodile country — credits include BBC Top Gear, River Monsters and National Geographic\u2019s Dangerous Encounters.',
         'Film & Television', body)

def build_contact():
    body = page_hero('Contact', 'Working in croc country?', 'Call for urgent call-outs, or send your site details and we’ll come back with a plan.') + f'''
<section class="section scales"><div class="wrap split" style="align-items:flex-start">
<div class="reveal">
<a class="contact-big" href="{TEL}">{PHONE}</a>
<div class="grid" style="gap:18px;margin-top:10px">
<div class="card" style="flex-direction:row;align-items:center;padding:20px">{icon('phone', 30)}<div><strong style="color:#fff">Phone</strong><br><a href="{TEL}">{PHONE}</a></div></div>
<div class="card" style="flex-direction:row;align-items:center;padding:20px">{icon('doc', 30)}<div><strong style="color:#fff">Email</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="card" style="flex-direction:row;align-items:center;padding:20px">{icon('pin', 30)}<div><strong style="color:#fff">Postal</strong><br><span class="muted">{POBOX}</span></div></div>
</div>
<p class="muted" style="margin-top:22px">Servicing the Northern Territory, Western Australia and Queensland, including remote sites.<br>If someone is in immediate danger, call 000.</p>
</div>
<div class="reveal">{enquiry_form('')}</div>
</div></section>
<section class="section" style="background:var(--ink-2)"><div class="wrap" style="max-width:900px">
<p class="eyebrow">Before you call</p><h2 style="margin-bottom:24px">Helpful to know</h2>
<div class="faq">
<details><summary>What details should I send?</summary><p>Where the site is, what work is planned, dates, crew size, and anything you’ve seen — crocodile sightings, snake activity or other wildlife. Photos help.</p></details>
<details><summary>How quickly will you get back to me?</summary><p>Promptly. Tell us about your project or operational environment and Chris will be in touch — or call 0409 326 307 for anything urgent.</p></details>
<details><summary>Do you work on remote sites?</summary><p>Yes — we service projects across the NT, WA and QLD, including remote and fly-in sites.</p></details>
</div></div></section>
'''
    page('contact.html', 'Contact | Crocodile Safety Australia',
         f'Call {PHONE} or send an enquiry for crocodile, snake and wildlife-risk management across the NT, WA and QLD.',
         'Contact', body)

def build_404():
    body = page_hero('Error 404', 'Nothing lurking here', 'The page you were after has moved or doesn’t exist.') + '''
<section class="section"><div class="wrap btn-row"><a class="btn btn-gold" href="/index.html">Back to home</a><a class="btn btn-ghost" href="/services.html">View services</a></div></section>'''
    page('404.html', 'Page not found | Crocodile Safety Australia', 'Page not found.', '', body)

def build_misc():
    urls = ['', 'about.html', 'services.html', 'film-television.html', 'contact.html'] + [f'services/{s["slug"]}.html' for s in SERVICES]
    with open(os.path.join(DIST, 'sitemap.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                ''.join(f'  <url><loc>{SITE}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    with open(os.path.join(DIST, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    with open(os.path.join(DIST, 'assets', 'favicon.svg'), 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#07150F"/>'
                '<path d="M6 24c6-9 30-9 36 0-6 9-30 9-36 0z" fill="#E3B23C"/><rect x="22" y="15" width="4" height="18" rx="2" fill="#07150F"/></svg>')
    os.makedirs(os.path.join(DIST, 'assets', 'media'), exist_ok=True)

if __name__ == '__main__':
    if os.path.exists(DIST): shutil.rmtree(DIST)
    shutil.copytree(SRC, DIST)
    import about_page
    build_home(); about_page.build_about_page(globals()); build_services()
    for s in SERVICES: build_service(s)
    build_film(); build_contact(); build_404(); build_misc()
    print('\n'.join(sorted(os.path.relpath(os.path.join(dp, f), DIST) for dp, _, fs in os.walk(DIST) for f in fs)))
