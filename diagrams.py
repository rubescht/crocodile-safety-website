"""Infographics and diagrams for the six lines of defence."""
import html

GOLD = '#E3B23C'

def marker(n, x, y):
    return (f'<g class="mk" transform="translate({x} {y})"><circle r="19" fill="{GOLD}" stroke="#07150F" stroke-width="3"/>'
            f'<text y="7" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="20" fill="#07150F">{n}</text></g>')

def person(x, y, vest=True, s=1.0):
    v = f'<rect x="-7" y="-46" width="14" height="16" fill="{GOLD}"/>' if vest else ''
    return (f'<g transform="translate({x} {y}) scale({s})" fill="#0B1611"><circle cx="0" cy="-58" r="7"/>'
            f'<path d="M-8 -50 h16 l3 26 h-5 l-2 24 h-4 l-1-18 h-2 l-1 18 h-4 l-2-24 h-5z"/>{v}</g>')

def site_section_svg(vb="0 70 1200 320", cls="xsec xsec-d", label=True):
    """Cross-section of a riverside work site with the six services marked."""
    return f'''<svg viewBox="{vb}" class="{cls}" role="img" aria-label="Cross-section of a riverside work site showing where each of the six services applies: 1 capture and relocation on the water, 2 overwatch spotter on the bank, 3 fauna spotter catcher beside clearing machinery, 4 feral animal management in the surrounding bush, 5 crew awareness training at the site, 6 consulting and documentation in the site office">
<defs>
<linearGradient id="xs-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E2E22"/><stop offset="1" stop-color="#16402F"/></linearGradient>
<linearGradient id="xs-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F3A2B"/><stop offset="1" stop-color="#05140E"/></linearGradient>
<linearGradient id="xs-cone" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="{GOLD}" stop-opacity=".45"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient>
</defs>
<rect width="1200" height="430" fill="url(#xs-sky)"/>
<path d="M600 250 C640 240 680 205 720 200 L1200 200 L1200 430 L600 430 Z" fill="#3A2F1E"/>
<path d="M720 200 L1200 200 L1200 214 L720 214 Z" fill="#4A6B3A"/>
<path d="M0 262 L640 262 L620 430 L0 430 Z" fill="url(#xs-water)"/>
<path d="M0 262 H640" stroke="#9DD4BE" stroke-opacity=".35" stroke-width="2"/>
<g stroke="#9DD4BE" stroke-opacity=".18" stroke-width="2"><line x1="40" y1="300" x2="160" y2="300"/><line x1="360" y1="330" x2="520" y2="330"/><line x1="120" y1="372" x2="260" y2="372"/></g>
<!-- bush and trees -->
<g fill="#1F4A36"><circle cx="1110" cy="150" r="46"/><circle cx="1160" cy="160" r="40"/><circle cx="1070" cy="170" r="32"/><rect x="1105" y="160" width="10" height="42"/>
<circle cx="860" cy="160" r="26" opacity=".7"/><rect x="856" y="170" width="7" height="32" opacity=".7"/></g>
<!-- 1 capture: croc + boat -->
<polygon points="672,170 210,248 270,300" fill="url(#xs-cone)"/>
<g transform="translate(-110 -106) scale(1.4)">
<path d="M120 266 C160 262 210 259 260 258 L286 258 C290 251 300 250 306 257 L330 259 C350 260 365 262 378 265 C360 270 330 272 300 272 L140 274 C120 273 110 270 120 266Z" fill="#6E8F5A" stroke="#0B1611" stroke-width="1.2"/><path d="M170 262 l5-6 5 6z M195 261 l5-7 5 7z M220 260 l5-7 5 7z M245 259 l5-6 5 6z" fill="#4C6B3D"/>
<circle cx="298" cy="255" r="3.5" fill="#FFC23A"/></g>
<path d="M420 262 L560 262 L548 286 L432 286 Z" fill="#5B6B63" stroke="#8FA39A" stroke-width="2"/>
{person(492, 262)}
<line x1="486" y1="212" x2="338" y2="248" stroke="#C9B98A" stroke-width="4" stroke-linecap="round"/>
<circle cx="330" cy="254" r="13" fill="none" stroke="#F1E6C2" stroke-width="3"/>
<!-- 2 overwatch: spotter on bank with sight cone -->
{person(680, 214)}
<rect x="668" y="157" width="18" height="6" rx="2" fill="#0B1611"/>
<!-- 5 training: crew + board -->
<rect x="760" y="138" width="70" height="46" rx="4" fill="#E9E1C8"/><line x1="772" y1="152" x2="816" y2="152" stroke="#07150F" stroke-width="3"/><line x1="772" y1="164" x2="806" y2="164" stroke="#07150F" stroke-width="3"/>
<line x1="780" y1="184" x2="776" y2="200" stroke="#E9E1C8" stroke-width="3"/><line x1="810" y1="184" x2="814" y2="200" stroke="#E9E1C8" stroke-width="3"/>
{person(752, 200, s=.85)}{person(844, 200, s=.85)}{person(872, 200, s=.85)}
<!-- 3 fauna spotter catcher: excavator + snake -->
<g transform="translate(930 200)"><rect x="0" y="-36" width="70" height="26" rx="4" fill="{GOLD}"/><rect x="40" y="-58" width="26" height="24" rx="3" fill="#C98F1C"/>
<rect x="-6" y="-12" width="84" height="12" rx="6" fill="#0B1611"/><path d="M6 -30 L-30 -70 L-56 -40" fill="none" stroke="#C98F1C" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M-56 -40 l-12 12 h16z" fill="#C98F1C"/></g>
<path d="M880 198 c6-8 12 4 18-2 s10-6 14 0" fill="none" stroke="#9BB86B" stroke-width="4" stroke-linecap="round"/>
{person(900, 200, s=.85)}
<!-- 6 consulting: site office with docs -->
<rect x="1010" y="150" width="76" height="50" fill="#5B6B63"/><path d="M1004 150 L1048 128 L1092 150Z" fill="#3E4A44"/><rect x="1024" y="164" width="20" height="16" fill="#E9E1C8"/><rect x="1056" y="170" width="16" height="30" fill="#2A3530"/>
<!-- 4 feral: pig in bush -->
<g transform="translate(1150 200)" fill="#2A1F14"><ellipse cx="0" cy="-14" rx="24" ry="13"/><path d="M20 -20 l14 4 -2 8 -14 0z"/><rect x="-16" y="-4" width="5" height="10"/><rect x="10" y="-4" width="5" height="10"/></g>
{marker(1, 250, 320)}{marker(2, 680, 120)}{marker(3, 960, 110)}{marker(4, 1150, 150)}{marker(5, 800, 108)}{marker(6, 1048, 100)}
<text x="30" y="300" fill="#9DD4BE" font-family="Inter,sans-serif" font-size="15" opacity=".8">WATER</text>
<text x="1170" y="236" fill="#C8B998" font-family="Inter,sans-serif" font-size="15" text-anchor="end" opacity=".8">WORK SITE</text>
</svg>'''

def section_block(services, root):
    items = ''.join(
        f'<li><a href="{root}services/{s["slug"]}.html"><span class="lg-n">{i+1}</span><span><strong>{html.escape(s["name"])}</strong>'
        f'<small>{html.escape(s["where"])}</small></span></a></li>' for i, s in enumerate(services))
    return f'''<div class="xsec-wrap reveal">
<figure class="info-card xsec-fig"><div class="xsec-scroll">{site_section_svg()}
<div class="xsec-m"><p class="xsec-m-h">On the water</p>{site_section_svg("10 168 640 180","xsec")}<p class="xsec-m-h">On the work site</p>{site_section_svg("625 72 575 150","xsec")}</div></div>
<figcaption>Where each line of defence works on a typical riverside project. Tap a service below to learn more.</figcaption></figure>
<ol class="xsec-legend">{items}</ol>
</div>'''

# ---------------------------------------------------------------- per-service diagrams
ARROW = '<span class="flow-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="#E3B23C" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'

def flow(steps):
    parts = [f'<li class="flow-step"><span class="flow-n">{i+1}</span><strong>{html.escape(t)}</strong><p>{html.escape(d)}</p></li>'
             for i, (t, d) in enumerate(steps)]
    return f'<ol class="flow" style="--n:{len(steps)}">' + ''.join(parts) + '</ol>'

def cycle(steps, centre):
    n = len(steps)
    import math
    nodes, labels = [], []
    for i, (t, d) in enumerate(steps):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = 200 + 140 * math.cos(a), 200 + 140 * math.sin(a)
        nodes.append(f'<g transform="translate({x:.0f} {y:.0f})"><circle r="38" fill="#0D2219" stroke="{GOLD}" stroke-width="3"/>'
                     f'<text y="-2" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="22" fill="{GOLD}">{i+1}</text>'
                     f'<text y="18" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#E9E1C8">{html.escape(t.upper())}</text></g>')
        labels.append(f'<li><span class="flow-n">{i+1}</span><div><strong>{html.escape(t)}</strong><p>{html.escape(d)}</p></div></li>')
    svg = (f'<svg viewBox="0 0 400 400" class="cycle-svg" role="img" aria-label="Cycle: {html.escape(" then ".join(t for t, _ in steps))}, then repeat">'
           f'<defs><marker id="cy-ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="{GOLD}"/></marker></defs>'
           f'<circle cx="200" cy="200" r="140" fill="none" stroke="#2A4A3B" stroke-width="3" stroke-dasharray="6 8"/>'
           + ''.join(f'<path d="M{200+140*__import__("math").cos(-1.5708+(i+.5)*6.2832/n-.18):.0f} {200+140*__import__("math").sin(-1.5708+(i+.5)*6.2832/n-.18):.0f} A140 140 0 0 1 {200+140*__import__("math").cos(-1.5708+(i+.5)*6.2832/n+.18):.0f} {200+140*__import__("math").sin(-1.5708+(i+.5)*6.2832/n+.18):.0f}" fill="none" stroke="{GOLD}" stroke-width="3" marker-end="url(#cy-ar)"/>' for i in range(n))
           + f'<text x="200" y="196" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="26" fill="#fff">{html.escape(centre[0])}</text>'
           f'<text x="200" y="220" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" fill="#9DB1A4">{html.escape(centre[1])}</text>'
           + ''.join(nodes) + '</svg>')
    return f'<div class="cycle reveal"><figure class="info-card cycle-fig">{svg}</figure><ol class="cycle-list">{"".join(labels)}</ol></div>'

def overwatch_plan_svg():
    return f'''<svg viewBox="0 0 760 360" class="plan-svg" role="img" aria-label="Top-down plan of an overwatch set-up: two spotters on the bank cover the water with overlapping sight lines, an exclusion zone separates the crew work area from the water's edge, and a stop-work signal goes to the supervisor">
<defs><linearGradient id="ow-cone" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{GOLD}" stop-opacity=".5"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient></defs>
<rect width="760" height="360" fill="#3A2F1E"/>
<path d="M0 0 H760 V120 C640 140 520 110 380 128 C240 146 120 116 0 134Z" fill="#0F3A2B"/>
<path d="M0 134 C120 116 240 146 380 128 C520 110 640 140 760 120 V178 C640 196 520 168 380 186 C240 204 120 174 0 192Z" fill="#E3B23C" opacity=".18"/>
<path d="M0 192 C120 174 240 204 380 186 C520 168 640 196 760 178" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="8 8"/>
<polygon points="200,214 20,40 340,20" fill="url(#ow-cone)"/><polygon points="560,206 400,20 740,40" fill="url(#ow-cone)"/>
<g fill="#0B1611" stroke="#fff" stroke-width="2"><circle cx="200" cy="214" r="12"/><circle cx="560" cy="206" r="12"/></g>
<rect x="250" y="250" width="260" height="80" rx="10" fill="#4A6B3A" opacity=".8"/>
<g fill="#0B1611"><circle cx="300" cy="290" r="8"/><circle cx="340" cy="300" r="8"/><circle cx="420" cy="285" r="8"/><circle cx="460" cy="302" r="8"/></g>
<path d="M200 226 C230 260 260 270 286 282" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="4 5"/>
<path d="M20 60 C24 56 40 55 52 56 L60 56 C62 52 66 52 68 55 L76 56 C82 57 86 58 90 60 C84 62 76 63 68 63 L30 64 C24 64 18 63 20 60Z" fill="#33503D" transform="translate(140 10)"/>
<text x="20" y="104" fill="#9DD4BE" font-family="Inter,sans-serif" font-size="14" font-weight="700">WATER</text>
<text x="740" y="166" text-anchor="end" fill="{GOLD}" font-family="Inter,sans-serif" font-size="13" font-weight="700">EXCLUSION ZONE · distance set per site</text>
<text x="380" y="346" text-anchor="middle" fill="#E9E1C8" font-family="Inter,sans-serif" font-size="13" font-weight="700">CREW WORK AREA</text>
<text x="200" y="244" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="12" font-weight="700">SPOTTER A</text>
<text x="560" y="236" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="12" font-weight="700">SPOTTER B</text>
<text x="240" y="276" fill="#fff" font-family="Inter,sans-serif" font-size="11">stop-work call</text>
</svg>'''

def overwatch_plan_mobile_svg():
    return f'''<svg viewBox="0 0 400 560" class="plan-svg plan-m" role="img" aria-label="Top-down plan of an overwatch set-up: two spotters on the bank cover the water, an exclusion zone separates the crew work area from the water's edge">
<defs><linearGradient id="owm-cone" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{GOLD}" stop-opacity=".5"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient></defs>
<rect width="400" height="560" fill="#3A2F1E"/>
<path d="M0 0 H400 V190 C300 210 200 176 100 196 C60 204 30 200 0 196Z" fill="#0F3A2B"/>
<path d="M0 196 C30 200 60 204 100 196 C200 176 300 210 400 190 V270 C300 290 200 256 100 276 C60 284 30 280 0 276Z" fill="{GOLD}" opacity=".18"/>
<path d="M0 276 C30 280 60 284 100 276 C200 256 300 290 400 270" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 8"/>
<polygon points="110,300 0,40 200,20" fill="url(#owm-cone)"/><polygon points="290,296 200,20 400,40" fill="url(#owm-cone)"/>
<g fill="#0B1611" stroke="#fff" stroke-width="3"><circle cx="110" cy="300" r="16"/><circle cx="290" cy="296" r="16"/></g>
<rect x="70" y="380" width="260" height="110" rx="14" fill="#4A6B3A" opacity=".85"/>
<g fill="#0B1611"><circle cx="130" cy="430" r="11"/><circle cx="180" cy="450" r="11"/><circle cx="230" cy="425" r="11"/><circle cx="275" cy="452" r="11"/></g>
<path d="M120 316 C140 350 150 370 160 392" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/>
<path d="M40 100 C60 92 110 90 140 92 L156 92 C160 84 168 84 172 90 L190 92 C204 94 212 96 220 100 C206 104 190 106 172 106 L80 108 C60 108 34 106 40 100Z" fill="#6E8F5A" stroke="#0B1611" stroke-width="1.5"/>
<text x="20" y="34" fill="#9DD4BE" font-family="Inter,sans-serif" font-size="22" font-weight="700">WATER</text>
<text x="200" y="244" text-anchor="middle" fill="{GOLD}" font-family="Inter,sans-serif" font-size="20" font-weight="700">EXCLUSION ZONE</text>
<text x="110" y="344" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="18" font-weight="700">A</text>
<text x="290" y="340" text-anchor="middle" fill="#fff" font-family="Inter,sans-serif" font-size="18" font-weight="700">B</text>
<text x="200" y="520" text-anchor="middle" fill="#E9E1C8" font-family="Inter,sans-serif" font-size="20" font-weight="700">CREW WORK AREA</text>
</svg>'''

def decision_tree():
    rows = [('Can the work be planned away from the water?', 'Avoid: exclusion zones, timing, siting', 'awareness-training'),
            ('Must crews be near the water?', 'Watch: dedicated overwatch with stop-work authority', 'crocodile-spotting-overwatch'),
            ('Is the crew trained for crocodile country?', 'Train: toolbox talks and awareness training', 'awareness-training'),
            ('Is a specific crocodile still a risk the controls can’t manage?', 'Remove: permitted capture and relocation', None)]
    out = []
    for i, (q, a, link) in enumerate(rows):
        last = i == len(rows) - 1
        out.append(f'<li class="dt-row{" dt-last" if last else ""}"><div class="dt-q"><span class="flow-n">{i+1}</span>{html.escape(q)}</div>'
                   f'<div class="dt-a"><span class="dt-yes">{"YES →" if last else "YES →"}</span>{html.escape(a)}</div></li>')
    return ('<div class="dt reveal"><p class="dt-head">Do we need to capture? We work through these questions first.</p><ol class="dt-list">'
            + ''.join(out) + '</ol><p class="dt-foot">If an earlier control manages the risk, we stop there — capture is the last resort.</p></div>')

DIAGRAMS = {
 'crocodile-capture-relocation': lambda: decision_tree() + '<h3 class="sub-h">From call-out to relocation</h3>' + flow([
    ('Assess', 'Inspect the site, the animal and its behaviour.'),
    ('Approve', 'Confirm permits and directions with the relevant authority.'),
    ('Capture', 'Trap, noose or hand capture by experienced operators.'),
    ('Secure', 'Safe restraint for the animal and the team.'),
    ('Relocate', 'Transport and relocation or hand-over as directed.'),
    ('Report', 'Written job report for your records.')]),
 'crocodile-spotting-overwatch': lambda: f'<figure class="info-card reveal"><div class="plan-d">{overwatch_plan_svg()}</div>{overwatch_plan_mobile_svg()}<ul class="plan-key"><li><b>A · B</b> Spotters with overlapping sight lines</li><li><b>Dashed line</b> Edge of the exclusion zone — distance set per site</li><li><b>Crew work area</b> Kept clear of the water; stop-work call goes straight to the supervisor</li></ul><figcaption>Typical overwatch set-up (illustrative). Spotter numbers and exclusion distances are set for each site.</figcaption></figure><h3 class="sub-h">A shift on overwatch</h3>' + flow([
    ('Brief', 'Pre-start briefing on site rules and signals.'),
    ('Position', 'Spotters placed for clear sight lines.'),
    ('Scan &amp; log'.replace('&amp;', '&'), 'Continuous watch of water and banks, logged.'),
    ('Alert', 'Stop-work call the moment a threat appears.'),
    ('Resume', 'Work restarts only when the area is clear.')]),
 'fauna-spotter-catcher': lambda: flow([
    ('Survey', 'Pre-clearing check of hollows, logs and burrows.'),
    ('Lead', 'Spotter works ahead of and beside machinery.'),
    ('Capture', 'Safe capture of snakes and other fauna.'),
    ('Relocate', 'Release into suitable nearby habitat.'),
    ('Record', 'Encounter records for your approvals.')]),
 'feral-animal-management': lambda: cycle([
    ('Assess', 'Map activity, impacts and risks.'),
    ('Plan', 'Program matched to your goals and rules.'),
    ('Control', 'Licensed control to codes of practice.'),
    ('Monitor', 'Track results over time.'),
    ('Report', 'Clear reporting, then refine the plan.')], ('ONGOING', 'program cycle')),
 'awareness-training': lambda: flow([
    ('Know the animal', 'Crocodile and snake behaviour and habitat.'),
    ('Read the site', 'Where and when the risk is highest.'),
    ('Work safely', 'Distances, boats, vehicles and camps.'),
    ('Respond', 'Encounters, first-aid awareness, emergencies.')]),
 'wildlife-consulting': lambda: cycle([
    ('Assess', 'Wildlife risk assessment for the site.'),
    ('Write', 'SOPs and SWMS for your methods.'),
    ('Train', 'Teams trained on the procedures.'),
    ('Apply', 'Procedures used in the field.'),
    ('Review', 'Update after changes or incidents.')], ('SAFE SYSTEM', 'of work')),
}

def service_diagram(slug):
    return DIAGRAMS[slug]()

def explainer(root):
    """Autoplaying (muted) explainer film with captions and a tap-for-sound button."""
    return f'''<figure class="explainer reveal" data-explainer>
<video autoplay muted loop playsinline preload="metadata" poster="{root}assets/media/six-lines-poster.jpg" aria-label="Video: the six lines of defence explained">
<source src="{root}assets/media/six-lines.mp4" type="video/mp4">
<track kind="captions" src="{root}assets/media/six-lines.vtt" srclang="en" label="English" default>
</video>
<button type="button" class="sound-btn"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Tap for sound</span></button>
<figcaption><span><strong>The six lines of defence</strong> · 1:02 · narrated</span><span>Illustrative footage</span></figcaption>
</figure>'''
