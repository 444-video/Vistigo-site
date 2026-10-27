#!/usr/bin/env python3
"""
Builds the Vistigo site: a hub page plus one page per product.

Plain Python, no dependencies. Writes index.html, maritime/index.html,
broadcast/index.html and infra/index.html next to this file; GitHub Pages
serves them from the repo root. Edit the content below, run
`python3 build.py`, and commit the generated HTML with it.

Styling: the Tabler UI kit (assets/vendor/tabler, MIT, by codecalm) in its
dark theme, with assets/css/site.css on top for type, the industry palettes
and the diagram. Writing: UK English, hyphens rather than em dashes, client
figures attributed to "a UK multiplex operator".
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
PROTOTYPE = "noc.444.video"

LOGO = """<svg class="logo-mark" viewBox="0 0 404 204" role="img" aria-label="444Video">
<rect x="1" y="1" width="99" height="99" fill="#1200FE"/><rect x="102" y="1" width="99" height="99" fill="#00FEC8"/>
<rect x="203" y="1" width="99" height="99" fill="#FEA300"/><rect x="304" y="1" width="99" height="99" fill="#FE0000"/>
<rect x="1" y="102" width="99" height="99" fill="#B500FE"/><rect x="102" y="102" width="99" height="99" fill="#00FE05"/>
<rect x="203" y="102" width="99" height="99" fill="#FBFE00"/><rect x="304" y="102" width="99" height="99" fill="#FE009C"/></svg>"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E"
           "%3Crect width='8' height='8' fill='%230B151D'/%3E"
           "%3Crect x='0' y='2' width='2' height='2' fill='%231200FE'/%3E%3Crect x='2' y='2' width='2' height='2' fill='%2300FEC8'/%3E"
           "%3Crect x='4' y='2' width='2' height='2' fill='%23FEA300'/%3E%3Crect x='6' y='2' width='2' height='2' fill='%23FE0000'/%3E"
           "%3Crect x='0' y='4' width='2' height='2' fill='%23B500FE'/%3E%3Crect x='2' y='4' width='2' height='2' fill='%2300FE05'/%3E"
           "%3Crect x='4' y='4' width='2' height='2' fill='%23FBFE00'/%3E%3Crect x='6' y='4' width='2' height='2' fill='%23FE009C'/%3E%3C/svg%3E")

PRODUCTS = {
    "maritime": dict(name="Vistigo Maritime", colour="#6FE6F3", font="f-maritime",
                     who="For fleets", line="Know which ship is on which link, right now."),
    "broadcast": dict(name="Vistigo Broadcast", colour="#FFB54D", font="f-broadcast",
                      who="For broadcasters", line="Find stream errors before your viewers do."),
    "infra": dict(name="Vistigo Infra", colour="#6BEB8A", font="f-infra",
                  who="For the racks behind it all", line="Find the failing fan before the server does."),
}


# ------------------------------------------------------------------ frame
def page(*, rel, title, description, product, body, extra=""):
    links = []
    for key, p in PRODUCTS.items():
        active = " active" if key == product else ""
        current = ' aria-current="page"' if key == product else ""
        links.append(f'<li class="nav-item"><a class="nav-link{active}" href="{rel}{key}/"{current}>{p["name"].split()[1]}</a></li>')
    body_class = f"p-{product}" if product else "p-hub"
    return f"""<!doctype html>
<html lang="en-GB" data-bs-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{rel}assets/vendor/tabler/tabler.min.css">
<link rel="stylesheet" href="{rel}assets/vendor/tabler/tabler-marketing.min.css">
<link rel="stylesheet" href="{rel}assets/css/site.css">
</head>
<body class="{body_class}">
<div class="bars" role="presentation"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>

<header class="navbar navbar-expand-md">
  <div class="container-xl">
    <a class="navbar-brand" href="{rel or './'}">{LOGO}<span>Vistigo<small>by 444Video</small></span></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav" aria-controls="nav" aria-expanded="false" aria-label="Menu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nav">
      <ul class="navbar-nav ms-auto">
        {''.join(links)}
        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
      </ul>
    </div>
  </div>
</header>

<main>
{body}
</main>

<footer class="footer py-5">
  <div class="container-xl">
    <div class="row g-4">
      <div class="col-md-5">
        <p class="mb-2">Vistigo is a monitoring product from <a href="https://444video.com">444Video</a>,
        a broadcast engineering company in the UK. The name comes from <em>vista</em>, a view.</p>
        <p class="mb-0"><a href="mailto:info@444.video">info@444.video</a> &nbsp; <a href="https://www.linkedin.com/company/444video">LinkedIn</a></p>
      </div>
      <div class="col-md-3">
        <ul class="list-unstyled mb-0">
          {''.join(f'<li><a href="{rel}{k}/">{p["name"]}</a></li>' for k, p in PRODUCTS.items())}
        </ul>
      </div>
      <div class="col-md-4">
        <p class="legal">&copy; 2026 444Video. Built with the Tabler UI kit. Grafana is a trademark of Grafana Labs.
        Zabbix, Prometheus, VictoriaMetrics, Starlink, Peplink, Zixi, TAG Video Systems and Dell iDRAC belong to their owners.
        We use and integrate with them; we aren't endorsed by them.</p>
      </div>
    </div>
  </div>
</footer>
<script src="{rel}assets/vendor/tabler/tabler.min.js" defer></script>
{extra}
</body>
</html>
"""


# ------------------------------------------------------------------ pieces
def browser(src, alt, rel, path):
    return f"""<div class="browser">
  <div class="browser-header d-flex align-items-center">
    <div class="browser-dots"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span></div>
    <span class="browser-input">{PROTOTYPE}{path}</span>
  </div>
  <img src="{rel}assets/img/{src}" alt="{escape(alt)}" loading="lazy">
</div>"""


def shot(src, alt, note, rel, path):
    return f"""<figure class="m-0">
  {browser(src, alt, rel, path)}
  <figcaption class="shot-note"><span class="badge bg-green-lt">Screenshot</span>{note}</figcaption>
</figure>"""


def drawn(html, note, path):
    return f"""<figure class="m-0">
  <div class="browser">
    <div class="browser-header d-flex align-items-center">
      <div class="browser-dots"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span></div>
      <span class="browser-input">{PROTOTYPE}{path}</span>
    </div>
    {html}
  </div>
  <figcaption class="shot-note"><span class="badge bg-secondary-lt">Mock-up</span>{note}</figcaption>
</figure>"""


def section(title, intro, inner, *, id_="", alt=False):
    i = f'<p class="section-description">{intro}</p>' if intro else ""
    return f"""<section class="section{' section-alt' if alt else ''}"{f' id="{id_}"' if id_ else ''}>
  <div class="container-xl">
    <div class="section-header"><h2 class="section-title">{title}</h2>{i}</div>
    {inner}
  </div>
</section>"""


def flow(rows, out):
    """Equipment -> how we read it -> where it's kept, all feeding the dashboards column."""
    html = [f'<div class="flow" style="--rows:{len(rows)}">',
            '<div class="flow-head" aria-hidden="true"><span>The equipment</span><span>How we read it</span>'
            '<span>Where it\'s kept</span><span>What you open</span></div>']
    for r in rows:
        html.append(f"""<div class="flow-row">
  <div class="card flow-kit"><div class="card-body"><strong>{r[0]}</strong><p>{r[1]}</p></div></div>
  <div class="card flow-via"><div class="card-body"><span class="badge bg-primary-lt">{r[2]}</span><strong>{r[3]}</strong><p>{r[4]}</p></div></div>
  <div class="card flow-store"><div class="card-body d-flex flex-column justify-content-center"><strong><span class="db {r[5]}"></span>{r[6]}</strong></div></div>
</div>""")
    items = "".join(f'<li class="list-group-item">{d}</li>' for d in out["dashboards"])
    html.append(f"""<div class="flow-out"><div class="card">
  <div class="card-status-top bg-primary"></div>
  <div class="card-body d-flex flex-column">
    <h3 class="mb-1">{out['title']}</h3>
    <p class="text-secondary small mb-2">Grafana, in 444Video's house style</p>
    <ul class="list-group list-group-flush mb-3">{items}</ul>
    <p class="small text-secondary mt-auto mb-0"><strong class="text-reset">Alerts:</strong> {out['alerts']}</p>
  </div>
</div></div>""")
    html.append("</div>")
    return "\n".join(html)


def dash_cards(cards):
    cols = []
    for i, (colour, group, title, text) in enumerate(cards):
        width = "col-12" if i == 0 else "col-md-4"
        cols.append(f"""<div class="{width}"><div class="card dash-card h-100">
  <div class="card-status-top" style="background:{colour}"></div>
  <div class="card-body"><small style="color:{colour}">{group}</small><h3>{title}</h3><p>{text}</p></div>
</div></div>""")
    return f'<div class="row g-3 mb-4">{"".join(cols)}</div>'


def audience(items):
    cols = "".join(f'<div class="col-md-6"><div class="card"><div class="card-body"><h3>{a}</h3><p>{b}</p></div></div></div>'
                   for a, b in items)
    return f'<div class="row g-3 audience">{cols}</div>'


def figures(items, source=""):
    cols = "".join(f'<div class="col-md-4"><div class="card figure-card h-100"><div class="card-body"><div class="display">{a}</div><p>{b}</p></div></div></div>'
                   for a, b in items)
    s = f'<p class="source">{source}</p>' if source else ""
    return f'<div class="row g-3">{cols}</div>{s}'


def others(rel, current):
    cards = []
    for k, p in PRODUCTS.items():
        if k == current:
            continue
        cards.append(f"""<div class="col-md-6"><a class="card card-link pillar-card" href="{rel}{k}/" style="--pc:{p['colour']}">
  <div class="card-status-start"></div>
  <div class="card-body"><span class="who">{p['who']}</span><h3 class="{p['font']}">{p['name']}</h3><p class="text-secondary mb-0">{p['line']}</p></div>
</a></div>""")
    return section("It all runs on the same system",
                   "Add another product whenever you like. The data lands in the same place, so a dropped stream and the satellite link it was on show up on the same timeline.",
                   f'<div class="row g-3">{"".join(cards)}</div>', alt=True)


def contact(text, subject):
    return f"""<section class="section contact-band" id="contact">
  <div class="container-xl">
    <div class="row align-items-end g-4">
      <div class="col-lg-7"><h2 class="section-title mb-3">Tell us what you can't see.</h2>
        <p class="section-description mb-0">{text}</p></div>
      <div class="col-lg-5 text-lg-end"><a class="btn btn-primary btn-lg" href="mailto:info@444.video?subject={subject}">Email info@444.video</a></div>
    </div>
  </div>
</section>"""


def readout(lead, cells, after=""):
    c = "".join(f'<div class="ro"><span>{k}</span><b>{v}</b></div>' for k, v in cells)
    return f"""<div class="readout" aria-label="Example readout">
  <div class="container-xl">{lead}{c}<span class="example">Example values</span></div>{after}
</div>"""


# ------------------------------------------------------------------ drawn panels
def spark(points, colour, fill=False):
    pts = " ".join(f"{i * 300 / (len(points) - 1):.1f},{92 - v:.1f}" for i, v in enumerate(points))
    area = f'<polygon fill="{colour}" fill-opacity=".18" points="0,92 {pts} 300,92"/>' if fill else ""
    return (f'{area}<polyline fill="none" stroke="{colour}" stroke-width="1.6" '
            f'vector-effect="non-scaling-stroke" stroke-linejoin="round" points="{pts}"/>')


GRID = '<path d="M0 23H300M0 46H300M0 69H300" stroke="#2c3235" stroke-width="1" vector-effect="non-scaling-stroke"/>'

BROADCAST_PANEL = f"""<div class="gp">
  <div class="gp-stats">
    <div class="gp-stat ok"><div class="k">TS sync</div><div class="v">Locked</div></div>
    <div class="gp-stat warn"><div class="k">CC errors, last hour</div><div class="v">3</div></div>
    <div class="gp-stat"><div class="k">PCR accuracy</div><div class="v">OK</div></div>
    <div class="gp-stat" style="background:linear-gradient(120deg,#6a1fb8,#8f3bb8)"><div class="k" style="color:#fff">Probe 07</div><div class="v">No data</div></div>
  </div>
  <div class="gp-panel"><div class="gp-h"><span>CC errors and IP packet loss</span><i>last 6 h</i></div>
    <svg class="gp-chart" viewBox="0 0 300 92" preserveAspectRatio="none" aria-hidden="true">{GRID}
      <g fill="#FF9830"><rect x="148" y="56" width="4" height="36"/><rect x="154" y="34" width="4" height="58"/><rect x="160" y="66" width="4" height="26"/><rect x="232" y="78" width="4" height="14"/></g>
      {spark([4,3,4,3,5,4,3,4,6,30,44,28,5,4,3,4,3,4,12,3,4,3,4,3], '#73BF69')}</svg></div>
  <div class="gp-panel gp-scroll"><table><thead><tr><th>Service</th><th>Bitrate</th><th>CC</th><th>Path</th><th>State</th></tr></thead><tbody>
    <tr><td>Service 101</td><td>6.2 Mb/s</td><td>0</td><td>SRT</td><td><span class="pill ok">OK</span></td></tr>
    <tr><td>Service 214</td><td>4.1 Mb/s</td><td>3</td><td>Zixi</td><td><span class="pill warn">CC</span></td></tr>
    <tr><td>Service 330</td><td>12.0 Mb/s</td><td>0</td><td>Satellite</td><td><span class="pill ok">OK</span></td></tr>
    <tr><td>Service 412</td><td>-</td><td>-</td><td>Probe 07</td><td><span class="pill nodata">NO DATA</span></td></tr>
  </tbody></table></div>
</div>"""

INFRA_PANEL = f"""<div class="gp">
  <div class="gp-stats">
    <div class="gp-stat ok"><div class="k">Hosts up</div><div class="v">142<small>/142</small></div></div>
    <div class="gp-stat warn"><div class="k">PSU redundancy</div><div class="v">1 lost</div></div>
    <div class="gp-stat"><div class="k">Hottest inlet</div><div class="v">31<small> &deg;C</small></div></div>
    <div class="gp-stat crit"><div class="k">Server 07, fan 4</div><div class="v">0<small> rpm</small></div></div>
  </div>
  <div class="gp-panel"><div class="gp-h"><span>Core uplink</span><i>last 24 h</i></div>
    <svg class="gp-chart" viewBox="0 0 300 92" preserveAspectRatio="none" aria-hidden="true">{GRID}
      {spark([14,12,16,24,40,52,56,60,58,50,38,24,16], '#5794F2', fill=True)}
      {spark([8,7,9,16,26,32,36,74,38,30,20,12,9], '#FF9830')}</svg></div>
  <div class="gp-panel gp-scroll"><table><thead><tr><th>Device</th><th>Read by</th><th>Reading</th><th>State</th></tr></thead><tbody>
    <tr><td>core-sw-01</td><td>SNMP</td><td>Gi1/0/48 at 78% out</td><td><span class="pill warn">HIGH</span></td></tr>
    <tr><td>server-07</td><td>iDRAC</td><td>PSU 2 lost</td><td><span class="pill warn">PSU</span></td></tr>
    <tr><td>pdu-a</td><td>SNMP v1</td><td>7.2 A</td><td><span class="pill ok">OK</span></td></tr>
    <tr><td>ups-01</td><td>SNMP</td><td>-</td><td><span class="pill nodata">NO DATA</span></td></tr>
  </tbody></table></div>
</div>"""

COMPASS = ('<svg class="compass" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/>'
           '<path d="M20 4L24 20L20 36L16 20Z" fill="currentColor"/><path d="M4 20L20 17L36 20L20 23Z" fill="currentColor" opacity=".35"/></svg>')


def _ship():
    """An original line drawing of a container ship under way, with its satellite and cellular links."""
    import random
    rnd = random.Random(444)
    hues = ["#1200FE", "#00FEC8", "#FEA300", "#FE0000", "#B500FE", "#00FE05", "#FBFE00", "#FE009C"]
    boxes = []
    x = 372
    while x < 800:
        h = rnd.choice([2, 3, 3, 4]) if x < 760 else rnd.choice([1, 2])
        for k in range(h):
            c = rnd.choice(hues)
            boxes.append(f'<rect x="{x}" y="{136 - 13 * (k + 1)}" width="36" height="12" fill="{c}" fill-opacity=".42" stroke="#06182A" stroke-width="1"/>')
        x += 38
    waves = "".join(
        f'<path d="M0 {y} ' + " ".join(f"Q{i + 25} {y - a} {i + 50} {y} T{i + 100} {y}" for i in range(0, 1300, 100)) +
        f'" fill="none" stroke="#6FE6F3" stroke-opacity="{o}" stroke-width="1"/>'
        for y, a, o in [(176, 4, .5), (190, 3, .3), (204, 2, .18)])
    return f"""<div class="voyage" role="img" aria-label="Illustration of a container ship at sea, linked to a satellite overhead and a cell mast on the coast.">
<svg viewBox="0 0 1200 220" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs><linearGradient id="hull" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#123554"/><stop offset="1" stop-color="#081C30"/></linearGradient></defs>
  <g stroke="#6FE6F3" fill="none" stroke-linecap="round">
    <path d="M1080 34 l12 -8 l12 8 l-12 8z M1068 34 h12 M1104 34 h12" stroke-width="1.4"/>
    <path d="M318 52 Q 700 -10 1080 34" stroke-dasharray="3 7" stroke-opacity=".55"/>
    <path d="M318 52 Q 640 70 1010 120" stroke-dasharray="3 7" stroke-opacity=".35" stroke="#FFB54D"/>
  </g>
  <g stroke="#FFB54D" stroke-opacity=".7" fill="none">
    <path d="M1010 168 L1010 104 M1002 168 L1010 104 L1018 168 M1004 128 h12 M1006 116 h8"/>
    <path d="M1000 98 a14 14 0 0 1 20 0 M995 92 a22 22 0 0 1 30 0" stroke-opacity=".5"/>
  </g>
  <path d="M960 168 L990 150 L1040 146 L1110 158 L1200 150 L1200 172 L940 172Z" fill="#0A2238" stroke="#1A3A58"/>
  <g>
    <path d="M246 140 L842 140 L870 118 L870 140 L852 170 L262 170 L246 150Z" fill="url(#hull)" stroke="#6FE6F3" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M262 158 L858 158" stroke="#FE0000" stroke-opacity=".55" stroke-width="2"/>
    {''.join(boxes)}
    <rect x="262" y="78" width="74" height="62" fill="#0E2A44" stroke="#6FE6F3" stroke-width="1.2"/>
    <rect x="252" y="76" width="96" height="6" fill="#0E2A44" stroke="#6FE6F3" stroke-width="1.2"/>
    <g fill="#C9F6FB" fill-opacity=".85">{''.join(f'<rect x="{268 + i * 10}" y="{88 + r * 14}" width="6" height="4"/>' for r in range(4) for i in range(6))}</g>
    <rect x="270" y="58" width="18" height="18" fill="#0E2A44" stroke="#6FE6F3" stroke-width="1.2"/>
    <rect x="270" y="58" width="18" height="4" fill="#1200FE" fill-opacity=".7"/>
    <path d="M318 76 V44 M306 52 H330" stroke="#6FE6F3" stroke-width="1.3"/>
    <circle cx="318" cy="40" r="6" fill="#EAF7FA"/>
    <rect x="328" y="70" width="12" height="3" fill="#EAF7FA" transform="rotate(-12 334 71)"/>
    <path d="M846 124 V108 M840 112 h12" stroke="#6FE6F3" stroke-width="1.2"/>
  </g>
  <path d="M870 170 q 18 2 34 -4 M870 170 q 14 6 30 6" stroke="#C9F6FB" stroke-opacity=".5" fill="none"/>
  <path d="M0 170 H1200" stroke="#6FE6F3" stroke-opacity=".35"/>
  {waves}
</svg>
</div>"""


SHIP = _ship()

TIMECODE = """<script>
(function(){var el=document.querySelector('[data-timecode]');if(!el)return;
if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
function p(n){return(n<10?'0':'')+n}
setInterval(function(){var d=new Date();el.textContent=p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds())+':'+p(Math.floor(d.getMilliseconds()/40));},40);})();
</script>"""


# ------------------------------------------------------------------ hub
def hub():
    rel = ""
    cards = []
    previews = {"maritime": ("dash-starlink.png", "Starlink dashboard", "/maritime/starlink"),
                "broadcast": ("dash-zixi.png", "Zixi contribution dashboard", "/broadcast/contribution"),
                "infra": None}
    blurbs = {
        "maritime": "Reads the Starlink dish, the Peplink router and the SIM account on every vessel. You see who's online, which link they're on and what it's costing.",
        "broadcast": "Pulls alarms and stats from your probes, IP receivers and Zixi or SRT links, so you can tell a bad source from a bad network in a minute, not an afternoon.",
        "infra": "Watches the switches, servers and power that everything else sits on, read from the management controllers rather than guessed from the operating system.",
    }
    for k, p in PRODUCTS.items():
        pv = previews[k]
        img = (browser(pv[0], pv[1], rel, pv[2]) if pv else
               f'<div class="browser"><div class="browser-header d-flex align-items-center"><div class="browser-dots"><span class="browser-dot"></span><span class="browser-dot"></span><span class="browser-dot"></span></div><span class="browser-input">{PROTOTYPE}/infra</span></div><div class="preview-drawn">{INFRA_PANEL}</div></div>')
        cards.append(f"""<div class="col-lg-4"><a class="card card-link pillar-card" href="{k}/" style="--pc:{p['colour']}">
  <div class="card-status-start"></div>
  <div class="card-body d-flex flex-column">
    {img}
    <span class="who">{p['who']}</span>
    <h3 class="{p['font']}">{p['name']}</h3>
    <p class="text-secondary">{blurbs[k]}</p>
    <span class="go mt-auto">See how it works</span>
  </div>
</a></div>""")

    stages = [
        ("Read it where it lives", [("On the ship", "a small collector asks the Starlink dish directly"),
                                    ("In the building", "Zabbix agents, SNMP and iDRAC"),
                                    ("In the cloud", "Peplink InControl2, the SIM provider, Zixi")]),
        ("Send it out safely", [("Outbound only", "nothing on a ship or customer network accepts connections"),
                                ("HTTPS, one login per site", "checked at our proxy before it's written"),
                                ("Buffered", "if the link drops, readings queue on disk and catch up")]),
        ("Keep the history", [("VictoriaMetrics", "most numbers, for months"),
                              ("Zabbix", "up/down, alarms and device logs"),
                              ("Elasticsearch", "the firehose from broadcast probes")]),
        ("Show it, and shout", [("Grafana", "a home page per customer, then one dashboard per job"),
                                ("Alerts", "to Slack, email or your NOC, with the device and reading attached"),
                                ("No data is purple", "a dead feed never shows green")]),
    ]
    steps = "".join(f'<li class="step-item">{s[0]}</li>' for s in stages)
    stage_cards = "".join(
        f'<div class="col-md-6 col-lg-3 stage"><div class="card"><div class="card-body"><h3 class="mb-2">{s[0]}</h3><ul>'
        + "".join(f"<li><strong>{a}</strong>: {b}</li>" for a, b in s[1]) + "</ul></div></div></div>"
        for s in stages)

    body = f"""<section class="hero">
  <div class="container-xl">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <h1 class="hero-title">We built this to watch our own kit. Now it can watch yours.</h1>
        <p class="hero-description mt-4">Vistigo is the monitoring 444Video runs on Starlink-equipped vehicles, live DTT
        transmission and the lab rack in our office. It reads the numbers straight from the equipment - the dish, the
        probe, the power supply - and puts them on dashboards your team will actually open.</p>
        <div class="btn-list"><a class="btn btn-primary btn-lg" href="#products">Pick your industry</a>
        <a class="btn btn-ghost-secondary btn-lg" href="#how">How it works</a></div>
      </div>
      <div class="col-lg-6">
        {shot('dash-cellular-cost.png', 'Cellular dashboard: signal bars, RSRP and SINR gauges, data used today and the projected cost for the next day and month.',
              'A live fleet dashboard: signal, data used, and what it will cost this month.', rel, '/maritime/cellular')}
      </div>
    </div>
  </div>
</section>

<section class="section section-alt" id="products">
  <div class="container-xl">
    <div class="section-header"><h2 class="section-title">Three products, one system underneath</h2>
    <p class="section-description">Start with the one that matches your work. They share the same collectors, database
    and dashboards, so adding a second later is a configuration change, not a new project.</p></div>
    <div class="row g-4">{''.join(cards)}</div>
  </div>
</section>

{section("From the kit to your screen", "No black box. It's Zabbix, Prometheus, VictoriaMetrics and Grafana, which half the internet already trusts, plus our own collectors for the equipment that only speaks its own language.",
         f'<ul class="steps steps-counter steps-primary my-4">{steps}</ul><div class="row g-3">{stage_cards}</div>', id_="how")}

{section("We run it before we sell it", "When we rebuilt a UK multiplex operator's transmission network, we replaced their manual checks with remote monitoring and kept every channel on air while we did it. The same tooling runs our own field tests and lab.",
         figures([("10 racks to 3", "after re-engineering the operator's infrastructure"),
                  ("Nothing off air", "during the whole migration"),
                  ("1,400 miles", "of bonded connectivity logged on our Belgium road test")],
                 "Rack and disruption figures from the 444Video case study for a UK multiplex operator."), alt=True)}

{contact("A fleet that drops off the map, a channel that glitches at 9pm, a server room that runs hot. Tell us about it and we'll show you what it looks like in Vistigo.", "Vistigo")}"""
    return page(rel=rel, title="Vistigo by 444Video",
                description="Monitoring for ships, broadcast chains and server rooms, built by the 444Video engineers who run it on their own kit.",
                product="", body=body)


# ------------------------------------------------------------------ maritime
def maritime():
    rel = "../"
    rows = [
        ("Starlink dish", "Throughput, latency to the ground station, how much sky is blocked, GPS, where it's pointing, its own alerts",
         "gRPC, every 60 s", "Collector on board", "Sits behind the dish on the ship's network and pushes out over HTTPS", "db-vm", "VictoriaMetrics"),
        ("Peplink router", "Which WAN is live, CPU and memory, and every dish if there's more than one",
         "REST API", "InControl2", "One call per router, split into system, WAN and Starlink figures", "db-vm", "VictoriaMetrics"),
        ("4G and 5G modems", "RSRP, RSRQ, SINR, RSSI, signal bars, band and operator",
         "REST API", "InControl2", "Read from the same router status as above, one line per modem", "db-vm", "VictoriaMetrics"),
        ("Each WAN link", "Live upload and download on Starlink, cellular and Wi-Fi",
         "REST, every 15 s", "Throughput collector", "Runs as its own service, so a fault here can't stop the rest", "db-vm", "VictoriaMetrics"),
        ("SIM cards", "Data used, cost and subscribers, per SIM and for the company",
         "REST API", "Geniox", "Straight from the SIM provider's account, not estimated", "db-vm", "VictoriaMetrics"),
        ("Is the router there at all?", "Up or down, and for how long",
         "ICMP, SNMP", "Zabbix", "Raises the alarm when a vessel goes dark or drops to its backup link", "db-zbx", "Zabbix"),
    ]
    out = dict(title="Your fleet", dashboards=["Peplink Overview", "Cellular", "Router Health", "Starlink", "SIM Card Monitoring"],
               alerts="vessel offline, running on backup, obstruction climbing, SIM spend over budget.")

    body = f"""<section class="hero">
  <div class="container-xl">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <p class="kicker">Vistigo Maritime</p>
        <h1 class="hero-title">Know which ship is on which link, right now.</h1>
        <p class="hero-description mt-4">Vistigo Maritime reads the Starlink dish, the Peplink router and the SIM account
        on every vessel, every 15 to 60 seconds, and puts the whole fleet on one screen. No more logging into routers one
        at a time to find out who's offline.</p>
        <div class="btn-list"><a class="btn btn-primary btn-lg" href="#data">Where the numbers come from</a>
        <a class="btn btn-ghost-secondary btn-lg" href="#contact">Talk to us</a></div>
      </div>
      <div class="col-lg-6">
        {shot('dash-starlink.png', 'Starlink dashboard: aligned, 7.18 percent of sky obstructed, 64 ms latency, an alignment bullseye and azimuth and elevation gauges.',
              'Our Starlink dashboard. The bullseye shows which way to nudge the dish.', rel, '/maritime/starlink')}
      </div>
    </div>
  </div>
</section>
{SHIP}
{readout(f'<div class="d-flex align-items-center gap-2">{COMPASS}<strong class="kicker mb-0">Bridge</strong></div>',
         [("Position", "50°48.2′N 001°05.7′W"), ("Heading", "274°"), ("Speed", "11.2 kn"), ("Live link", "Starlink"), ("Latency", "34 ms"), ("Backup", "5G, 3 bars")])}

{section("Where the numbers come from", "We read each device the way it prefers. The dish only answers on the ship's own network, so a small collector on board asks it directly. The router, modems and SIMs already report to their makers' cloud services, so we collect from there. Everything is tagged with the vessel it came from.",
         flow(rows, out), id_="data")}

{section("What your team opens in the morning", "A home page for the fleet, with a card for each job. Click through for the detail.",
         dash_cards([("#6FE6F3", "Start here", "Peplink Overview", "Every WAN, the headline health figures, cellular signal and Starlink status on one screen."),
                     ("#FBFE00", "Signal", "Cellular", "RSRP, RSRQ, SINR, RSSI and bars, with the last 24 hours to show how stable it's been."),
                     ("#4ADE6E", "System", "Router Health", "CPU, memory and daily peaks, so you spot a router that's struggling."),
                     ("#5794F2", "Uplink", "Starlink", "Alignment, obstruction, throughput, latency and pointing.")])
         + f"""<div class="row g-4">
  <div class="col-lg-6">{shot('dash-sim-usage.png', 'SIM Card Monitoring: 2.0 GB used, 4.08 euros, 4 SIMs, with data used per SIM.', 'SIM spend per card, straight from the provider.', rel, '/maritime/sims')}</div>
  <div class="col-lg-6">{shot('dash-cellular-cost.png', 'Cellular dashboard: signal bars, RSRP and SINR gauges, data used today and the projected cost for the next day and month.', "What today's data use will cost you this month.", rel, '/maritime/cellular')}</div>
  <div class="col-12">{shot('dash-cellular-history.png', 'Throughput per WAN and 24 hours of signal strength and quality.', 'Throughput per link and a day of signal history. You can see exactly when the vessel moved out of 5G coverage.', rel, '/maritime/cellular')}</div>
</div>""", alt=True)}

{section("Who uses it", "",
         audience([("Ship operators and fleet managers", "One screen for every vessel, instead of a login per router."),
                   ("Maritime IT and managed service providers", "A view for each customer, with alerts going to your own NOC."),
                   ("Survey, offshore and research vessels", "A record of when the link was up and how good it was, for crew and clients."),
                   ("Broadcasting from the water", "Add Vistigo Broadcast and see the stream next to the link carrying it.")]))}

{others(rel, 'maritime')}
{contact("Tell us how many vessels you run and what's on board. We'll show you your fleet in Vistigo.", "Vistigo%20Maritime")}"""
    return page(rel=rel, title="Vistigo Maritime: fleet connectivity monitoring",
                description="Starlink, 4G/5G, failover and SIM spend for every vessel, read from the dish, the Peplink router and the SIM provider.",
                product="maritime", body=body)


# ------------------------------------------------------------------ broadcast
def broadcast():
    rel = "../"
    rows = [
        ("TAG probes and multiviewers", "Channel stats and events: CC errors, PCR, PES drops, SCTE-35, captions, NTP",
         "Redis, Logstash", "Buffered pipeline", "Reads every list the probes write, so nothing piles up in memory", "db-es", "Elasticsearch"),
        ("RF and TS probes", "ETR 101 290 alarms, MER, SNR, signal level, active alarm count",
         "XML API, SNMP traps", "Zabbix", "Keeps the alarm count and the raw alarm table behind it", "db-zbx", "Zabbix"),
        ("IP receivers", "Input lock per IP feed, RTP sequence and CC errors, effective bitrate, device logs",
         "SNMP, logs", "Zabbix", "Lock state for every input, and log lines tinted by device", "db-zbx", "Zabbix"),
        ("Zixi broadcasters", "Source bitrate, ARQ and FEC recovery, round-trip time, and the broadcaster's own CPU, RAM and throughput",
         "REST API", "Zixi collector", "Every stream and every broadcaster on one timeline", "db-vm", "VictoriaMetrics"),
        ("SRT gateways and encoders", "Bitrate, round-trip time, retransmits, packet loss, picture quality",
         "SRT stats, exporters", "Telegraf, Prometheus", "Per-session numbers from the gateway itself", "db-vm", "VictoriaMetrics"),
    ]
    out = dict(title="Every service you carry", dashboards=["Transmission wall", "PCR and PES by stream", "Zixi and SRT contribution", "Device logs", "One site at a time"],
               alerts="priority 1 errors straight away, plus detailed reports for your team, or for the manufacturer when it's their fault.")

    body = f"""<section class="hero">
  <div class="container-xl">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <p class="kicker">Vistigo Broadcast</p>
        <h1 class="hero-title">Find stream errors before your viewers do.</h1>
        <p class="hero-description mt-4">Vistigo Broadcast collects alarms and statistics from your probes, IP receivers and
        Zixi or SRT links and lines them up on one timeline. When a CC error burst starts, you can see whether it came from
        the source, the encoder or the network carrying it.</p>
        <div class="btn-list"><a class="btn btn-primary btn-lg" href="#data">Where the numbers come from</a>
        <a class="btn btn-ghost-secondary btn-lg" href="#contact">Talk to us</a></div>
      </div>
      <div class="col-lg-6">
        {shot('dash-zixi.png', 'Contribution dashboard: source bitrate around 26 Mb/s per stream, ARQ packet recovery around 2.4 thousand packets a second, and broadcaster CPU, RAM and throughput.',
              'Zixi contribution: how hard each link is working to keep the picture clean.', rel, '/broadcast/contribution')}
      </div>
    </div>
  </div>
</section>
{readout('<span class="tally"><i></i>ON AIR</span><div class="ro"><span>Timecode</span><b class="tc" data-timecode>10:00:00:00</b></div>',
         [("Programme", "PGM 1, 1080i50"), ("Bitrate", "25.0 Mb/s"), ("CC errors", "0"), ("Path", "Zixi and SRT")],
         '<div class="smpte" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>')}

{section("Where the numbers come from", "Probes, receivers and contribution gateways all report differently. We collect from each one in the way it supports, then put them on the same clock so cause and effect sit side by side.",
         flow(rows, out), id_="data")}

{section("What your team opens", "A status wall first, then the detail behind every tile.",
         dash_cards([("#FFB54D", "Start here", "Transmission wall", "Every site and service on one screen: bitrate gauges, input locks and probe alarms. A tile that stops reporting turns purple, never green."),
                     ("#FBFE00", "Streams", "PCR and PES", "PCR accuracy and audio and video PES drops per stream, from the probes."),
                     ("#6FE6F3", "Contribution", "Zixi and SRT", "Bitrate, ARQ recovery, round-trip time and loss per stream and per broadcaster."),
                     ("#FF6FB5", "Logs", "Device logs", "Every device's log lines in one list, newest first, each device in its own tint.")])
         + f'<div class="row g-4"><div class="col-12">{drawn(BROADCAST_PANEL, "Drawn with sample data. A screenshot of the transport stream wall will replace it.", "/broadcast/ts-health")}</div></div>', alt=True)}

{section("Who uses it", "",
         audience([("Broadcasters and multiplex operators", "Every service on one wall, with priority 1 errors flagged before the phones ring."),
                   ("Playout and distribution", "Tell a source fault from an encoder fault from a network fault."),
                   ("Remote production and OB", "Contribution health from the field, next to the bonded link it's travelling over."),
                   ("Broadcast manufacturers", "Evidence for product testing and standards compliance, not anecdotes.")])
         + '<div class="mt-4">' + figures([("Nothing off air", "during a UK multiplex operator's full infrastructure migration"),
                                         ("10 racks to 3", "about 70% less kit to power and maintain"),
                                         ("3 months", "start to finish")],
                                        "Figures from the 444Video case study for a UK multiplex operator.") + "</div>")}

{others(rel, 'broadcast')}
{contact("Tell us which probes, receivers and contribution links you use. We'll show you your services in Vistigo.", "Vistigo%20Broadcast")}"""
    return page(rel=rel, title="Vistigo Broadcast: transport stream and contribution monitoring",
                description="ETR 101 290, CC errors, PCR and PES from your probes, plus Zixi and SRT link health, on one timeline in Grafana.",
                product="broadcast", body=body, extra=TIMECODE)


# ------------------------------------------------------------------ infra
def infra():
    rel = "../"
    rows = [
        ("Switches", "Port throughput, errors, discards, optic levels, CPU, uptime and unexpected reboots",
         "SNMP", "Zabbix, vmagent", "Every port and uplink, with an alarm on any reboot nobody asked for", "db-vm", "VictoriaMetrics"),
        ("Traffic between VLANs", "Who's talking to whom, and how much",
         "sFlow, NetFlow", "Flow collector", "Sampled flows from the switch, turned into top talkers", "db-vm", "VictoriaMetrics"),
        ("Servers", "Power supply status and redundancy, fan speeds, inlet and CPU temperatures, disk health",
         "iDRAC, IPMI, SNMP", "Zabbix", "From the management controller, so it works even when the OS is down", "db-zbx", "Zabbix"),
        ("Hosts and VMs", "CPU, memory, disk space, network, whether services are running",
         "Zabbix agent, node_exporter", "Zabbix, Prometheus", "Collected on site and held on disk if the uplink drops", "db-vm", "VictoriaMetrics"),
        ("PDUs, UPS and batteries", "Load per outlet, runtime left, charge, watts in and out, temperature",
         "SNMP, Bluetooth", "Telegraf", "Even a battery that only speaks Bluetooth gets a small gateway", "db-influx", "InfluxDB"),
        ("The easy-to-forget things", "Certificates about to expire, clock drift, DHCP pools filling up, backups getting old",
         "Agent, exporters", "Zabbix, Prometheus", "The quiet problems that cause the loud outages", "db-zbx", "Zabbix"),
    ]
    out = dict(title="Rooms, racks and what's in them", dashboards=["Overview", "Server health", "Network", "Power", "Problems"],
               alerts="tagged by severity and sent to Slack, email or your NOC, so the right person gets woken up.")

    body = f"""<section class="hero">
  <div class="container-xl">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <p class="kicker">Vistigo Infra</p>
        <h1 class="hero-title">Find the failing fan before the server does.</h1>
        <p class="hero-description mt-4">Switches, servers and power, read from the management controllers and the network
        itself. When something starts to go, it turns up in Slack with the rack, the device and the reading attached,
        while the spare power supply is still running.</p>
        <div class="btn-list"><a class="btn btn-primary btn-lg" href="#data">Where the numbers come from</a>
        <a class="btn btn-ghost-secondary btn-lg" href="#contact">Talk to us</a></div>
      </div>
      <div class="col-lg-6">
        {drawn(INFRA_PANEL, 'Drawn with sample data. Screenshots of the live infrastructure dashboards will replace it.', '/infra/rack-a04')}
      </div>
    </div>
  </div>
</section>
{readout('<div class="leds" aria-hidden="true"><i></i><i></i><i></i><i class="amber"></i><i></i><i></i></div>',
         [("Rack", "A04, 42U"), ("PSU A / B", "OK / OK"), ("Inlet", "24 °C"), ("Load", "3.2 kW"), ("Uplink", "78%"), ("Problems", "1 warning")])}

{section("Where the numbers come from", "Zabbix and Prometheus are trusted everywhere because they work. What usually goes wrong is the setup: templates nobody tuned and alerts nobody reads. That's the part we do.",
         flow(rows, out), id_="data")}

{section("What your team opens", "One home page per room, rack or customer.",
         dash_cards([("#6BEB8A", "Start here", "Overview", "Every host, switch and power feed on one page, with problems sorted to the top."),
                     ("#6FE6F3", "Compute", "Server health", "Power supplies, fans and temperatures for each server."),
                     ("#5794F2", "Network", "Network", "Port throughput, errors, optics and the top talkers."),
                     ("#FBFE00", "Power", "Power", "PDU load per outlet, UPS runtime and battery charge.")]), alt=True)}

{section("Who uses it", "",
         audience([("NOC and IT operations", "One view across rooms and sites, and alerts you can trust."),
                   ("Broadcast engineering", "The servers and switches behind playout, next to the streams they carry."),
                   ("Managed service providers", "A view and alert routing for each customer, from one system."),
                   ("Edge and remote sites", "Unattended racks and flyaway kits, watched from anywhere.")])
         + '<div class="mt-4">' + figures([("10 racks to 3", "for a UK multiplex operator, with remote monitoring replacing manual checks"),
                                         ("About 70%", "less space taken by kit on that project"),
                                         ("Purple", "is what no data looks like here. A silent device never passes for a healthy one.")],
                                        "Rack and footprint figures from the 444Video case study for a UK multiplex operator.") + "</div>")}

{others(rel, 'infra')}
{contact("Tell us what's in your racks and where they are. We'll show you what Vistigo would put on screen.", "Vistigo%20Infra")}"""
    return page(rel=rel, title="Vistigo Infra: server, network and power monitoring",
                description="Switches, servers, PDUs, UPS and batteries, read over SNMP, iDRAC and sFlow, with alerts to Slack.",
                product="infra", body=body)


def main():
    for path, html in {"index.html": hub(), "maritime/index.html": maritime(),
                       "broadcast/index.html": broadcast(), "infra/index.html": infra()}.items():
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
