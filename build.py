#!/usr/bin/env python3
"""
Builds the Vistigo site: hub + one page per pillar.

Plain Python, no dependencies. Writes index.html, maritime/index.html,
broadcast/index.html and infra/index.html next to this file, which
GitHub Pages serves from the repo root. Run `python3 build.py` after
editing anything below, then commit the generated HTML too.

Look and voice come from the 444Video Marketing & Brand Guidelines and the
444video.com design system: assets/css/444.css is a straight copy of the main
site's stylesheet; assets/css/vistigo.css only adds the diagrams and
dashboard frames. UK English, hyphens not em dashes.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

AQUA, ORANGE, GREEN = "#00FEC8", "#FEA300", "#00FE05"

LOGO = """<svg class="logo-mark" viewBox="0 0 404 204" role="img" aria-label="444Video">
  <rect x="1" y="1" width="99" height="99" fill="#1200FE"/><rect x="102" y="1" width="99" height="99" fill="#00FEC8"/>
  <rect x="203" y="1" width="99" height="99" fill="#FEA300"/><rect x="304" y="1" width="99" height="99" fill="#FE0000"/>
  <rect x="1" y="102" width="99" height="99" fill="#B500FE"/><rect x="102" y="102" width="99" height="99" fill="#00FE05"/>
  <rect x="203" y="102" width="99" height="99" fill="#FBFE00"/><rect x="304" y="102" width="99" height="99" fill="#FE009C"/>
</svg>"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E"
           "%3Crect width='8' height='8' fill='%230A141C'/%3E"
           "%3Crect x='0' y='2' width='2' height='2' fill='%231200FE'/%3E%3Crect x='2' y='2' width='2' height='2' fill='%2300FEC8'/%3E"
           "%3Crect x='4' y='2' width='2' height='2' fill='%23FEA300'/%3E%3Crect x='6' y='2' width='2' height='2' fill='%23FE0000'/%3E"
           "%3Crect x='0' y='4' width='2' height='2' fill='%23B500FE'/%3E%3Crect x='2' y='4' width='2' height='2' fill='%2300FE05'/%3E"
           "%3Crect x='4' y='4' width='2' height='2' fill='%23FBFE00'/%3E%3Crect x='6' y='4' width='2' height='2' fill='%23FE009C'/%3E%3C/svg%3E")

NAV = [("maritime/", "Maritime"), ("broadcast/", "Broadcast"), ("infra/", "Infra"), ("#how", "How it works"), ("#contact", "Contact")]

PILLARS = {
    "maritime": dict(label="Vistigo Maritime", colour=AQUA, glow=4,
                     line="Every vessel, always connected."),
    "broadcast": dict(label="Vistigo Broadcast", colour=ORANGE, glow=3,
                      line="Catch the error before the viewer does."),
    "infra": dict(label="Vistigo Infra", colour=GREEN, glow=5,
                  line="Know your hardware before it fails."),
}


# ---------------------------------------------------------------- partials
def page(*, rel, title, description, glow, current, body, theme=""):
    nav = []
    for href, label in NAV:
        url = href if href.startswith("#") else rel + href
        cur = ' aria-current="page"' if href.rstrip("/") == current else ""
        nav.append(f'<a href="{url}"{cur}>{label}</a>')
    pillar_links = "".join(f'<a href="{rel}{k}/">{v["label"]}</a>' for k, v in PILLARS.items())
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#0A141C">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vistigo by 444Video">
<meta property="og:locale" content="en_GB">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{rel}assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/css/444.css">
<link rel="stylesheet" href="{rel}assets/css/vistigo.css">
<link rel="stylesheet" href="{rel}assets/css/themes.css">
</head>
<body class="glow glow-{glow}{" theme-" + theme if theme else ""}">

<div class="bars" role="presentation"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>

<header class="site-head">
  <a class="brand" href="{rel or './'}" aria-label="Vistigo home">
    {LOGO}
    <span class="brand-text"><b>Vistigo</b><i>by 444Video</i></span>
  </a>
  <nav class="site-nav" aria-label="Main">{''.join(nav)}</nav>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="foot-inner">
    <div class="foot-brand">
      {LOGO}
      <span class="brand-text"><b>Vistigo</b><i>by 444Video</i></span>
    </div>
    <div class="foot-links">
      <h4>Pillars</h4>
      {pillar_links}
    </div>
    <div class="foot-links">
      <h4>444Video</h4>
      <a href="https://444video.com">444video.com</a>
      <a href="mailto:info@444.video">info@444.video</a>
      <a href="https://www.linkedin.com/company/444video">LinkedIn</a>
    </div>
  </div>
  <p class="foot-legal">&copy; 2026 444Video. The Full Picture. Vistigo, from <i>vista</i> - the view.
  Grafana is a trademark of Grafana Labs; Zabbix, Prometheus, VictoriaMetrics, Starlink, Peplink, Zixi, TAG Video Systems
  and other names are trademarks of their respective owners.</p>
</footer>
{TIMECODE if theme == "broadcast" else ""}
</body>
</html>
"""


def cta(text, subject):
    return f"""<section class="cta" id="contact">
  <div class="cta-inner">
    <p class="eyebrow">Get in touch</p>
    <h2>Tell us what you can't see.</h2>
    <p>{text}</p>
    <p class="actions"><a class="btn" href="mailto:info@444.video?subject={subject}">info@444.video</a></p>
  </div>
</section>"""


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


def flowmap(colour, rows, sink):
    """Equipment -> how we pull it -> where it lands, all feeding one Grafana box."""
    out = [f'<div class="flowmap" style="--c:{colour};--rows:{len(rows)}" role="list" aria-label="Data flow">',
           '<div class="fm-head" aria-hidden="true"><span>Equipment</span><span>How we pull it</span>'
           '<span>Where it lands</span><span>What you see</span></div>']
    for r in rows:
        out.append(f"""<div class="fm-row" role="listitem">
  <div class="fm-node fm-src"><b>{r['kit']}</b><span>{r['what']}</span></div>
  <div class="fm-node fm-via"><em class="proto">{r['proto']}</em><b>{r['via']}</b><span>{r['how']}</span></div>
  <div class="fm-node fm-store {r['db']}"><b>{r['store']}</b><span>{r.get('keep', '')}</span><i class="fm-out"></i></div>
</div>""")
    items = "".join(f"<li>{d}</li>" for d in sink["dashboards"])
    out.append(f"""<div class="fm-sink">
  <p class="eyebrow" style="--eyebrow-colour:{colour}">Grafana</p>
  <h3>{sink['title']}</h3>
  <ul>{items}</ul>
  <p class="fm-alert"><b>Alerts:</b> {sink['alerts']}</p>
</div>""")
    out.append("</div>")
    return "\n".join(out)


def shot(src, alt, caption, bar, rel, real=True, wide=False):
    tag = '<span class="tag-real">Live dashboard</span>' if real else '<span class="tag-mock">Illustrative</span>'
    cls = ' class="shot wide"' if wide else ' class="shot"'
    return f"""<figure{cls}>
  <div class="shot-frame">
    <div class="shot-bar">{LOGO}<span>{bar}</span><em>Grafana</em></div>
    <img src="{rel}assets/img/{src}" alt="{escape(alt)}" loading="lazy">
  </div>
  <figcaption>{tag}{caption}</figcaption>
</figure>"""


def mock(html, bar, caption, wide=False):
    cls = ' class="shot wide"' if wide else ' class="shot"'
    return f"""<figure{cls}>
  <div class="shot-frame">
    <div class="shot-bar">{LOGO}<span>{bar}</span><em>Grafana</em></div>
    {html}
  </div>
  <figcaption><span class="tag-mock">Illustrative</span>{caption}</figcaption>
</figure>"""


def dcards(colour, start, cards):
    out = [f'<div class="dcards" style="--dc:{colour}">',
           f'<div class="dcard start"><small>Start here</small><b>{start[0]}</b><p>{start[1]}</p></div>']
    for c, label, title, desc in cards:
        out.append(f'<div class="dcard" style="--dc:{c}"><small>{label}</small><b>{title}</b><p>{desc}</p></div>')
    out.append("</div>")
    return "\n".join(out)


def audience(colour, items):
    li = "".join(f'<li style="border-left-color:{colour}"><b>{a}</b><span>{b}</span></li>' for a, b in items)
    return f'<ul class="audience">{li}</ul>'


def others(rel, current):
    cards = []
    for k, v in PILLARS.items():
        if k == current:
            continue
        cards.append(f"""<a class="other" href="{rel}{k}/" style="--oc:{v['colour']}">
  <p class="eyebrow">{v['label']}</p><b>{v['line']}</b><span class="more">Explore {v['label'].split()[1]}</span></a>""")
    return f"""<section class="section-break"><div class="block">
  <header class="section-head"><p class="eyebrow">Same platform</p><h2>Add another pillar.</h2>
  <p class="lede">Every pillar lands in the same databases and the same Grafana, so a fault on one timeline sits next to its cause on another.</p></header>
  <div class="others">{''.join(cards)}</div>
</div></section>"""


def figures(items, attribution=None):
    tiles = "".join(f'<div class="figure-tile"><b>{a}</b><span>{b}</span></div>' for a, b in items)
    attr = f'<p class="attribution">{attribution}</p>' if attribution else ""
    return f'<div class="figures">{tiles}</div>{attr}'


# ------------------------------------------------------------ illustrative panels
def spark(points, colour, fill=False):
    pts = " ".join(f"{i * 300 / (len(points) - 1):.1f},{96 - v:.1f}" for i, v in enumerate(points))
    area = f'<polygon fill="{colour}" fill-opacity=".18" points="0,96 {pts} 300,96"/>' if fill else ""
    return (f'{area}<polyline fill="none" stroke="{colour}" stroke-width="1.6" '
            f'vector-effect="non-scaling-stroke" stroke-linejoin="round" points="{pts}"/>')


GRID = '<path d="M0 24H300M0 48H300M0 72H300" stroke="#2c3235" stroke-width="1" vector-effect="non-scaling-stroke"/>'

BROADCAST_MOCK = f"""<div class="gpanels">
  <div class="gstats">
    <div class="gstat ok"><div class="k">TS sync</div><div class="v">Locked</div></div>
    <div class="gstat warn"><div class="k">CC errors (1 h)</div><div class="v">3</div></div>
    <div class="gstat"><div class="k">PCR accuracy</div><div class="v">OK</div></div>
    <div class="gstat nodata"><div class="k">Probe 07</div><div class="v">No data</div></div>
  </div>
  <div class="gpanel">
    <div class="gpanel-h"><span>CC errors against IP packet loss</span><i>last 6 h</i></div>
    <svg class="gchart" viewBox="0 0 300 96" preserveAspectRatio="none" aria-hidden="true">{GRID}
      <g fill="#FF9830"><rect x="148" y="60" width="4" height="36"/><rect x="154" y="38" width="4" height="58"/><rect x="160" y="70" width="4" height="26"/><rect x="232" y="82" width="4" height="14"/></g>
      {spark([4,3,4,3,5,4,3,4,6,30,44,28,5,4,3,4,3,4,12,3,4,3,4,3], '#73BF69')}
    </svg>
  </div>
  <div class="gpanel gscroll">
    <table class="gtable"><thead><tr><th>Service</th><th>Bitrate</th><th>CC</th><th>Path</th><th>State</th></tr></thead><tbody>
      <tr><td>Service 101</td><td>6.2 Mb/s</td><td>0</td><td>SRT</td><td><span class="pill ok">OK</span></td></tr>
      <tr><td>Service 214</td><td>4.1 Mb/s</td><td>3</td><td>Zixi</td><td><span class="pill warn">CC</span></td></tr>
      <tr><td>Service 330</td><td>12.0 Mb/s</td><td>0</td><td>Sat RX</td><td><span class="pill ok">OK</span></td></tr>
      <tr><td>Service 412</td><td>-</td><td>-</td><td>Probe 07</td><td><span class="pill nodata">NO DATA</span></td></tr>
    </tbody></table>
  </div>
</div>"""

INFRA_MOCK = f"""<div class="gpanels">
  <div class="gstats">
    <div class="gstat ok"><div class="k">Hosts up</div><div class="v">142<small>/142</small></div></div>
    <div class="gstat warn"><div class="k">PSU redundancy</div><div class="v">1 lost</div></div>
    <div class="gstat"><div class="k">Max inlet</div><div class="v">31<small> &deg;C</small></div></div>
    <div class="gstat crit"><div class="k">Fan 4, server 07</div><div class="v">0<small> rpm</small></div></div>
  </div>
  <div class="gpanel">
    <div class="gpanel-h"><span>Core uplink throughput</span><i>last 24 h</i></div>
    <svg class="gchart" viewBox="0 0 300 96" preserveAspectRatio="none" aria-hidden="true">{GRID}
      {spark([14,12,16,24,40,52,56,60,58,50,38,24,16], '#5794F2', fill=True)}
      {spark([8,7,9,16,26,32,36,74,38,30,20,12,9], '#FF9830')}
    </svg>
  </div>
  <div class="gpanel gscroll">
    <table class="gtable"><thead><tr><th>Device</th><th>Source</th><th>Reading</th><th>State</th></tr></thead><tbody>
      <tr><td>core-sw-01</td><td>SNMP</td><td>Gi1/0/48 78% out</td><td><span class="pill warn">HIGH</span></td></tr>
      <tr><td>server-07</td><td>iDRAC</td><td>PSU 2 lost</td><td><span class="pill warn">PSU</span></td></tr>
      <tr><td>pdu-a</td><td>SNMP v1</td><td>7.2 A</td><td><span class="pill ok">OK</span></td></tr>
      <tr><td>ups-01</td><td>SNMP</td><td>-</td><td><span class="pill nodata">NO DATA</span></td></tr>
    </tbody></table>
  </div>
</div>"""


# ------------------------------------------------------------ industry strips
# Each pillar gets an instrument strip under the hero in its own industry's idiom.
# The readings are illustrative, like the mock panels.
def _cells(cells):
    return "".join(f'<div class="ro"><small>{k}</small><b>{v}</b></div>' for k, v in cells)

STRIP_MARITIME = f"""<div class="strip strip-maritime" aria-label="Illustrative bridge readout">
  <div class="strip-inner">
    <div class="ro-lead"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M20 4 L24 20 L20 36 L16 20Z" fill="currentColor" opacity=".9"/><path d="M4 20 L20 17 L36 20 L20 23Z" fill="currentColor" opacity=".35"/></svg><span>Bridge</span></div>
    {_cells([("Position", "50°48.2′N 001°05.7′W"), ("Heading", "274°"), ("Speed", "11.2 kn"), ("Active link", "Starlink"), ("Ping", "34 ms"), ("Backup", "5G · 3 bars")])}
  </div>
</div>"""

STRIP_BROADCAST = f"""<div class="strip strip-broadcast" aria-label="Illustrative on-air readout">
  <div class="strip-inner">
    <div class="tally"><i></i>On air</div>
    <div class="ro"><small>Timecode</small><b class="tc" data-timecode>10:00:00:00</b></div>
    {_cells([("Programme", "PGM 1 · 1080i50"), ("Bitrate", "25.0 Mb/s"), ("CC errors", "0"), ("Path", "Zixi + SRT")])}
  </div>
  <div class="smpte" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
</div>"""

STRIP_INFRA = f"""<div class="strip strip-infra" aria-label="Illustrative rack readout">
  <div class="strip-inner">
    <div class="leds" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i class="amber"></i><i class="on"></i><i class="on"></i></div>
    {_cells([("Rack", "A04 · 42U"), ("PSU A / B", "OK / OK"), ("Inlet", "24 °C"), ("Load", "3.2 kW"), ("Uplink", "78%"), ("Problems", "1 warning")])}
  </div>
</div>"""

TIMECODE = """<script>
// Running timecode for the broadcast strip (25 fps). Stops if the user prefers reduced motion.
(function(){var el=document.querySelector('[data-timecode]');if(!el)return;
if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var p=function(n){return(n<10?'0':'')+n};
setInterval(function(){var d=new Date(),f=Math.floor(d.getMilliseconds()/40);
el.textContent=p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds())+':'+p(f);},40);})();
</script>"""


# ---------------------------------------------------------------- pages
def hub():
    rel = ""
    arch = [
        ("At the edge", AQUA, [("Vessels", "Peplink routers, cellular modems, Starlink dishes, SIMs"),
                               ("Galleries and playout", "Probes, receivers, encoders, Zixi and SRT gateways"),
                               ("Racks and rooms", "Switches, servers, PDUs, UPS and batteries")]),
        ("Collect", ORANGE, [("On-site collectors", "Starlink collector, vmagent and Telegraf, buffering to disk if the link drops"),
                             ("Agents and polling", "Zabbix agents, SNMP, iDRAC, node_exporter"),
                             ("Cloud API bridges", "Peplink InControl2, Geniox SIMs, Zixi, TAG")]),
        ("Secure ingest", "#FE009C", [("HTTPS, every site its own login", "Checked at the proxy before anything is written"),
                                      ("Nothing inbound on site", "Ships and customer networks only ever push out")]),
        ("Store", "#FBFE00", [("VictoriaMetrics", "Fast, compact time series for months of history"),
                              ("Zabbix", "Availability, triggers and device logs"),
                              ("Elasticsearch", "High-volume probe statistics and events")]),
        ("See and act", GREEN, [("Grafana, 444Video-styled", "A card home page per customer, then a dashboard per job"),
                                ("Alerts that reach a person", "Slack, email or your NOC, with the context attached")]),
    ]
    cols = []
    for name, col, nodes in arch:
        n = "".join(f'<div class="arch-node"><b>{a}</b><span>{b}</span></div>' for a, b in nodes)
        cols.append(f'<div class="arch-col" style="--col:{col}"><h4>{name}</h4>{n}</div>')

    pillar_rows = []
    rows = [
        ("maritime", "dash-maritime-home.png", "The Maritime home: Peplink overview, cellular, router health and Starlink.",
         "Starlink, cellular, failover and SIM data use, read from the dish, the router and the SIM provider, for every vessel.",
         ["Starlink", "RSRP · RSRQ · SINR", "per-WAN throughput", "SIM data and cost"]),
        ("broadcast", "dash-zixi.png", "Contribution: source bitrate, ARQ packet recovery and broadcaster load.",
         "Transport stream health from probes and receivers, next to the contribution links it travels over.",
         ["ETR 101 290", "CC errors", "Zixi ARQ", "SRT RTT", "PCR / PES"]),
        ("infra", None, None,
         "Switches, servers, power and the quiet housekeeping that causes loud outages - polled, tuned and alerted.",
         ["SNMP", "iDRAC", "PSU · fans · temps", "PDU · UPS", "sFlow"]),
    ]
    for i, (key, img, alt, text, ch) in enumerate(rows, 1):
        p = PILLARS[key]
        if img:
            fig = (f'<figure><div class="shot-frame"><img src="assets/img/{img}" alt="{escape(alt)}" loading="lazy"></div>'
                   f'<figcaption class="note"><span class="tag-real">Live dashboard</span>{alt}</figcaption></figure>')
        else:
            fig = f'<figure><div class="shot-frame">{INFRA_MOCK}</div><figcaption class="note"><span class="tag-mock">Illustrative</span>Sample data.</figcaption></figure>'
        pillar_rows.append(f"""<article class="pillar" style="--eyebrow-colour:{p['colour']}">
  {fig}
  <div class="pillar-body">
    <p class="eyebrow">{i:02d} · {p['label']}</p>
    <h3>{p['line']}</h3>
    <p class="pillar-standfirst">{text}</p>
    {chips(ch)}
    <a class="more" href="{key}/">How Vistigo {key.capitalize() if key != 'infra' else 'Infra'} works</a>
  </div>
</article>""")

    body = f"""<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">Vistigo by 444Video</p>
    <h1>One view of everything you run.</h1>
    <p class="standfirst">Vessels at sea, streams on air, racks in the server room. Vistigo pulls the numbers out of the
    kit you already own and puts them in one set of live dashboards - so you see the problem before your customers do.</p>
    <p class="actions"><a class="btn" href="#pillars">The three pillars</a><a class="btn btn-quiet" href="#how">How it works</a></p>
  </div>
  {shot('dash-maritime-home.png', 'Vistigo Maritime home dashboard in Grafana, with cards for Peplink Overview, Cellular, Router Health and Starlink.',
        'Every customer starts on a card home like this one, then drills into each dashboard.', 'Vistigo Maritime · Home', rel)}
</section>

<section class="pillars section-break" id="pillars">
  <header class="section-head">
    <p class="eyebrow">Three pillars, one platform</p>
    <h2>Start with the pillar you need. Add the others later.</h2>
    <p class="lede">Each pillar is a set of collectors, dashboards and alerts tuned to one industry. They share one data platform,
    so a broadcaster on a ship sees the stream and the satellite link on the same timeline.</p>
  </header>
  {''.join(pillar_rows)}
</section>

<section class="section-break" id="how"><div class="block">
  <header class="section-head">
    <p class="eyebrow">How it works</p>
    <h2>From the kit to the screen in five steps.</h2>
    <p class="lede">No black box. Vistigo is built on open, proven tooling - Zabbix, Prometheus, VictoriaMetrics and Grafana -
    with our own collectors filling the gaps where a device only talks its own language.</p>
  </header>
  <div class="arch">{''.join(cols)}</div>
  <p class="note"><b>House rule:</b> a tile with no data turns purple, never green. A dead feed can't pass for a healthy one.</p>
</div></section>

<section class="band"><div class="band-inner">
  <p class="eyebrow">Why 444Video</p>
  <h2>We built it for our own projects first.</h2>
  <p class="lede">444Video designs and runs bespoke broadcast and connectivity systems for organisations that can't afford
  downtime. Vistigo is the monitoring we built to run them, turned into a product.</p>
  {figures([("10 racks → 3", "infrastructure re-engineered, with remote proactive monitoring"),
            ("Zero", "live broadcast disruption during that migration"),
            ("10+ years", "complex broadcast networks for Tier 1 global customers")],
           "Rack and disruption figures from the 444Video case study for a UK multiplex operator.")}
</div></section>

{cta("A fleet that drops off the map, a stream that glitches at 9pm, a rack that runs hot. Tell us about it and we'll show you what Vistigo would put on screen.", "Vistigo")}"""
    return page(rel=rel, title="Vistigo by 444Video - one view of everything you run",
                description="Vistigo pulls live data from ships, broadcast chains and server rooms into one set of Grafana dashboards. Maritime, Broadcast and Infra monitoring from 444Video.",
                glow=1, current="", body=body)


def maritime():
    rel, c = "../", AQUA
    rows = [
        dict(kit="Starlink dish", what="Throughput, PoP latency, obstruction, GPS, pointing, dish alerts",
             proto="gRPC · every 60 s", via="On-board collector", how="Reads the dish directly on the ship's LAN, pushes out over HTTPS",
             store="VictoriaMetrics", db="db-vm", keep="Tagged by vessel and dish"),
        dict(kit="Peplink router", what="WAN status, which link is live, CPU and memory, multiple dishes per router",
             proto="REST API", via="InControl2 bridge", how="One request per router, split into system, WAN and Starlink series",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="Cellular modems", what="RSRP, RSRQ, SINR, RSSI, signal bars, band, operator",
             proto="REST API", via="InControl2 bridge", how="Read from the same router status block, per modem",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="Every WAN link", what="Live upload and download per link - Starlink, 4G/5G, Wi-Fi",
             proto="REST · every 15 s", via="Throughput collector", how="Realtime bandwidth per WAN, kept as its own service",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="SIM cards", what="Data used, cost and subscribers per SIM and per company",
             proto="REST API", via="Geniox bridge", how="Polls the SIM provider, so roaming spend is never a surprise",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="Router reachability", what="Up, down and how long for",
             proto="SNMP · ICMP", via="Zabbix", how="Triggers fire when a vessel goes dark or drops to backup",
             store="Zabbix", db="db-zbx"),
    ]
    sink = dict(title="Your fleet, one home page",
                dashboards=["Peplink Overview", "Cellular", "Router Health", "Starlink", "SIM Card Monitoring"],
                alerts="vessel offline, on backup link, obstruction rising, SIM spend - into Slack or email.")
    body = f"""<section class="hero">
  <div class="hero-text">
    <p class="eyebrow" style="--eyebrow-colour:{c}">Vistigo Maritime</p>
    <h1>Every vessel, always connected.</h1>
    <p class="standfirst">See which ships are online, which link they're on and how well it's performing - Starlink, cellular,
    failover and SIM spend across the whole fleet, on one screen.</p>
    <p class="actions"><a class="btn" href="#flow">How we pull the data</a><a class="btn btn-quiet" href="#contact">Tell us what you can't see</a></p>
  </div>
  {shot('dash-starlink.png', 'Starlink dashboard: alignment status Aligned, sky obstructed 7.18 percent, ping latency 64 ms, with an alignment bullseye and azimuth and elevation gauges.',
        'Starlink: alignment, obstruction, latency and a bullseye that guides the dish to centre.', 'Vistigo Maritime · Starlink', rel)}
</section>
{STRIP_MARITIME}

<section class="section-break" id="flow"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">How we pull the data</p>
    <h2>From the dish and the router to your screen.</h2>
    <p class="lede">Each piece of kit is read the way it prefers to be read. The Starlink dish is asked directly on board;
    the router, modems and SIMs come through their cloud APIs. Everything lands in one place, tagged with the vessel it came from.</p>
  </header>
  {flowmap(c, rows, sink)}
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">What you see</p>
    <h2>A home page for the fleet, then a dashboard per job.</h2>
  </header>
  {dcards(c, ("Peplink Overview", "Every WAN interface, headline health, cellular signal and Starlink status on one screen."), [
      ("#FBFE00", "Signal", "Cellular", "RSRP, RSRQ, SINR, RSSI and signal bars, with trends and stability over time."),
      (GREEN, "System", "Router Health", "CPU load, memory, 24-hour peaks and stress detection for each router."),
      ("#5794F2", "Uplink", "Starlink", "Alignment bullseye, obstruction, throughput up and down, latency and pointing."),
  ])}
  <div class="gallery">
    {shot('dash-maritime-home.png', 'The Maritime home dashboard with cards for each view.', 'The home page your team opens first.', 'Vistigo Maritime · Home', rel)}
    {shot('dash-sim-usage.png', 'SIM Card Monitoring dashboard showing company data used 2.0 GB, cost 4.08 euros, 4 SIMs, and a table of data used per SIM.',
          'SIM Card Monitoring: data and cost per SIM, straight from the SIM provider.', 'Vistigo Maritime · SIM cards', rel)}
    {shot('dash-cellular-cost.png', 'Cellular dashboard with signal bars, RSRP and SINR gauges, data used in the last 24 hours, projected cost for the next 24 hours and 30 days, and cost per hour and per WAN.',
          'Cellular: live signal, then data used and what it will cost you this month, per WAN.', 'Vistigo Maritime · Cellular', rel, wide=True)}
    {shot('dash-cellular-history.png', 'Cellular dashboard history: throughput now and 24-hour peaks, throughput per WAN, and 24 hours of RSRP, RSSI, RSRQ and SINR.',
          'Cellular history: throughput per WAN, and 24 hours of signal strength and quality.', 'Vistigo Maritime · Cellular', rel, wide=True)}
  </div>
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head"><p class="eyebrow" style="--eyebrow-colour:{c}">Who it's for</p>
  <h2>Anyone who has to keep a moving network online.</h2></header>
  {audience(c, [("Ship operators and fleet managers", "One view of every vessel, without logging into each router."),
               ("Maritime IT and managed service providers", "A view per customer you can hand over, with alerts into your NOC."),
               ("Survey, offshore and research vessels", "Proof of when the link was up, and how well, for crews and clients."),
               ("Broadcast and events on the water", "Pair with Vistigo Broadcast: the stream and the link on one timeline.")])}
  {figures([("60 s", "Starlink read straight from the dish"), ("15 s", "per-WAN throughput, every link"),
            ("1,400 miles", "Belgium field test, bonded links measured on the road")])}
</div></section>

{others(rel, 'maritime')}
{cta("Tell us how many vessels you run and which links they use. We'll show you what your fleet looks like in Vistigo.", "Vistigo%20Maritime")}"""
    return page(rel=rel, title="Vistigo Maritime - every vessel, always connected",
                description="Starlink, cellular, failover and SIM data use for every vessel, pulled from the dish, the Peplink router and the SIM provider into Grafana.",
                glow=PILLARS['maritime']['glow'], current="maritime", body=body, theme="maritime")


def broadcast():
    rel, c = "../", ORANGE
    rows = [
        dict(kit="TAG probes and multiviewers", what="Channel statistics and events: CC errors, PCR, PES drops, SCTE-35, captions, NTP",
             proto="Redis → Logstash", via="Buffered pipeline", how="Every list the probes write is read, so nothing piles up in memory",
             store="Elasticsearch", db="db-es", keep="Retention sized to your channel count"),
        dict(kit="RF and TS probes", what="ETR 101 290 alarms, MER, SNR, signal level, active alarm count",
             proto="XML API · SNMP traps", via="Zabbix", how="Alarm counts and traps, with the raw alarm table kept for detail",
             store="Zabbix", db="db-zbx"),
        dict(kit="IP receivers and gateways", what="Input lock, RTP sequence and CC errors, effective bitrate, device logs",
             proto="SNMP · logs", via="Zabbix", how="Lock state per input, log lines tinted by device",
             store="Zabbix", db="db-zbx"),
        dict(kit="Zixi broadcasters", what="Source bitrate, ARQ and FEC recovery, RTT, broadcaster CPU, RAM and throughput",
             proto="REST API", via="Zixi bridge", how="Every stream and every broadcaster, on one timeline",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="SRT gateways and encoders", what="Bitrate, RTT, retransmits, packet loss, video quality",
             proto="SRT stats · exporters", via="Telegraf / Prometheus", how="Per-session statistics from the gateway itself",
             store="VictoriaMetrics", db="db-vm"),
    ]
    sink = dict(title="Every service on one wall",
                dashboards=["Transmission wall", "Stream PCR and PES", "Contribution (Zixi / SRT)", "Device logs", "Per-site view"],
                alerts="priority 1 errors at once; detail reports for your team, or the manufacturer when the fault is theirs.")
    body = f"""<section class="hero">
  <div class="hero-text">
    <p class="eyebrow" style="--eyebrow-colour:{c}">Vistigo Broadcast</p>
    <h1>Catch the error before the viewer does.</h1>
    <p class="standfirst">Transport stream and contribution health for every service you carry. Spot a CC error burst the
    moment it starts, then trace it to the link, the probe or the encoder that caused it.</p>
    <p class="actions"><a class="btn" href="#flow">How we pull the data</a><a class="btn btn-quiet" href="#contact">Tell us what you can't see</a></p>
  </div>
  {shot('dash-zixi.png', 'Contribution dashboard: source bitrate around 26 Mb/s per stream, packet recovery ARQ around 2.4 thousand packets per second, and broadcaster CPU, RAM and throughput.',
        'Contribution: source bitrate, ARQ recovery and broadcaster load, per stream.', 'Vistigo Broadcast · Contribution', rel)}
</section>
{STRIP_BROADCAST}

<section class="section-break" id="flow"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">How we pull the data</p>
    <h2>From the transport stream to the link it rides on.</h2>
    <p class="lede">Probes, receivers and contribution gateways each report in their own way. Vistigo collects all of them and lines
    them up on one timeline, so you can tell a source problem from a transport problem in seconds.</p>
  </header>
  {flowmap(c, rows, sink)}
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">What you see</p>
    <h2>A status wall first, then the detail behind every tile.</h2>
  </header>
  {dcards(c, ("Transmission wall", "Every site and service at a glance: bitrate gauges, input locks and probe alarms, purple when a feed goes quiet."), [
      ("#FBFE00", "Streams", "PCR and PES", "PCR accuracy and audio and video PES drops per stream, from the probes."),
      (AQUA, "Contribution", "Zixi and SRT", "Bitrate, ARQ recovery, RTT and loss per stream and per broadcaster."),
      ("#FE009C", "Logs", "Device logs", "Every device's log lines in one list, newest first, each device in its own tint."),
  ])}
  <div class="gallery">
    {shot('dash-zixi.png', 'Contribution dashboard with source bitrate and packet recovery.', 'Contribution, from the live 444Video stack.', 'Vistigo Broadcast · Contribution', rel, wide=True)}
    {mock(BROADCAST_MOCK, 'Vistigo Broadcast · Transport stream health', 'Sample data. Real screenshots of the transport stream wall to follow.', wide=True)}
  </div>
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head"><p class="eyebrow" style="--eyebrow-colour:{c}">Who it's for</p>
  <h2>Anyone responsible for what goes to air.</h2></header>
  {audience(c, [("Broadcasters and multiplex operators", "Every service on one wall, with priority 1 errors flagged before the phones ring."),
               ("Playout and distribution teams", "See whether a glitch came from the source, the encoder or the network."),
               ("Remote production and OB", "Contribution health from the field, alongside the bonded link it travels over."),
               ("Broadcast manufacturers", "Evidence-first reporting for product validation and standards compliance.")])}
  {figures([("Zero", "live broadcast disruption during the migration"), ("10 racks → 3", "~70% smaller infrastructure footprint"),
            ("3 months", "end to end, for a project of that complexity")],
           "Figures from the 444Video case study for a UK multiplex operator.")}
</div></section>

{others(rel, 'broadcast')}
{cta("Tell us which probes, receivers and contribution paths you run. We'll show you what your services look like in Vistigo.", "Vistigo%20Broadcast")}"""
    return page(rel=rel, title="Vistigo Broadcast - catch the error before the viewer does",
                description="Transport stream and contribution monitoring: ETR 101 290, CC errors, PCR and PES from probes, Zixi ARQ and SRT stats, all in Grafana.",
                glow=PILLARS['broadcast']['glow'], current="broadcast", body=body, theme="broadcast")


def infra():
    rel, c = "../", GREEN
    rows = [
        dict(kit="Switches", what="Port throughput, errors, discards, optic levels, CPU, uptime and reboots",
             proto="SNMP", via="Zabbix / vmagent", how="Every port and uplink, with a trigger on unexpected reboots",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="Traffic flows", what="Top talkers and the traffic matrix between VLANs",
             proto="sFlow · NetFlow", via="Flow collector", how="Sampled flows from the switch, turned into per-host series",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="Servers", what="PSU status and redundancy, fan speeds, inlet and CPU temperatures, disk health",
             proto="iDRAC · SNMP · IPMI", via="Zabbix", how="Read from the management controller, not just the operating system",
             store="Zabbix", db="db-zbx"),
        dict(kit="Hosts and VMs", what="CPU, memory, disk space, network, services up",
             proto="agent · node_exporter", via="Zabbix / Prometheus", how="Scraped locally and buffered if the uplink drops",
             store="VictoriaMetrics", db="db-vm"),
        dict(kit="PDUs, UPS and batteries", what="Load per outlet, runtime, state of charge, watts in and out, temperature",
             proto="SNMP · BLE → MQTT", via="Telegraf", how="Even a battery with only Bluetooth gets a gateway",
             store="InfluxDB", db="db-influx"),
        dict(kit="Housekeeping", what="Certificate expiry, NTP drift, DHCP pool use, backup age",
             proto="agent · exporters", via="Zabbix / Prometheus", how="The quiet things that cause loud outages",
             store="Zabbix", db="db-zbx"),
    ]
    sink = dict(title="Rooms, racks and the kit inside",
                dashboards=["Infrastructure overview", "Server health", "Network", "Power", "Problems and alerts"],
                alerts="severity-tagged triggers into Slack, email or your NOC, so the right person gets woken up.")
    body = f"""<section class="hero">
  <div class="hero-text">
    <p class="eyebrow" style="--eyebrow-colour:{c}">Vistigo Infra</p>
    <h1>Know your hardware before it fails.</h1>
    <p class="standfirst">Switches, servers and power in one view. Catch the failing fan, the lost PSU and the saturated uplink
    while there's still time to fix them on your terms.</p>
    <p class="actions"><a class="btn" href="#flow">How we pull the data</a><a class="btn btn-quiet" href="#contact">Tell us what you can't see</a></p>
  </div>
  {mock(INFRA_MOCK, 'Vistigo Infra · Rack health', 'Sample data. Real screenshots of the infrastructure dashboards to follow.')}
</section>
{STRIP_INFRA}

<section class="section-break" id="flow"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">How we pull the data</p>
    <h2>The kit underneath everything else.</h2>
    <p class="lede">Zabbix and Prometheus are trusted everywhere because they work. What usually goes wrong is the setup -
    templates nobody tuned, alerts nobody reads. That's the part we do for you.</p>
  </header>
  {flowmap(c, rows, sink)}
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head">
    <p class="eyebrow" style="--eyebrow-colour:{c}">What you see</p>
    <h2>One home page per room, rack or customer.</h2>
  </header>
  {dcards(c, ("Infrastructure overview", "Every host, switch and power feed on one page, with problems sorted to the top."), [
      (AQUA, "Compute", "Server health", "PSU, fans and temperatures per server, from the management controller."),
      ("#5794F2", "Network", "Network", "Port throughput, errors, optics and top talkers across the estate."),
      ("#FBFE00", "Power", "Power", "PDU load per outlet, UPS runtime and battery state of charge."),
  ])}
</div></section>

<section class="section-break"><div class="block">
  <header class="section-head"><p class="eyebrow" style="--eyebrow-colour:{c}">Who it's for</p>
  <h2>Teams who look after racks they can't always stand in front of.</h2></header>
  {audience(c, [("NOC and IT operations", "A single view across rooms and sites, with alerts you can trust."),
               ("Broadcast engineering", "The servers and switches behind playout and contribution, next to the streams."),
               ("Managed service providers", "A view and alert routing per customer, from one platform."),
               ("Edge and remote sites", "Unattended racks, flyaway kits and portable systems, watched from anywhere.")])}
  {figures([("10 racks → 3", "infrastructure consolidated, with remote proactive monitoring"), ("~70%", "smaller footprint on the same project"),
            ("Purple", "the colour of no data - a dead feed never looks healthy")],
           "Rack and footprint figures from the 444Video case study for a UK multiplex operator.")}
</div></section>

{others(rel, 'infra')}
{cta("Tell us what's in your racks and where they are. We'll show you what Vistigo would put on screen.", "Vistigo%20Infra")}"""
    return page(rel=rel, title="Vistigo Infra - know your hardware before it fails",
                description="Switch, server and power monitoring: SNMP, iDRAC, sFlow, PDU, UPS and battery data in Zabbix, VictoriaMetrics and Grafana.",
                glow=PILLARS['infra']['glow'], current="infra", body=body, theme="infra")


def main():
    out = {"index.html": hub(), "maritime/index.html": maritime(),
           "broadcast/index.html": broadcast(), "infra/index.html": infra()}
    for path, html in out.items():
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
