# Generates the static pages with a shared header/footer. Re-run: python3 build.py
ADDR_LINE1 = "7300 W. McNab Road, Suite 119"
ADDR_LINE2 = "Tamarac, FL 33321"
ADDR = f"{ADDR_LINE1}, {ADDR_LINE2}"
LICNAME = "Jeremy Esperant, Sales Associate | United Realty Group Inc."
PHONE = "954-643-4239"; TEL = "tel:+19546434239"
EMAIL = "jeremyesperant@gmail.com"
LICENSE = "FL License #: SL[pending — add number]"
CTA = "Book Your Opening Move"
MAPS = "https://www.google.com/maps/search/?api=1&query=7300+W+McNab+Rd+Suite+119+Tamarac+FL+33321"

def head(title, desc, page, extra=""):
    nav = [("index.html","Home"),("about.html","About"),("listings.html","Listings"),("contact.html","Contact")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==page else ""}>{t}</a>' for h,t in nav)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{extra}<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Jeremy Esperant","jobTitle":"Sales Associate","url":"https://thekingeffectinc-cloud.github.io/jeremyesperant-site/","image":"https://thekingeffectinc-cloud.github.io/jeremyesperant-site/img/jeremy-esperant.jpg","telephone":"+1-954-643-4239","email":"{EMAIL}","worksFor":{{"@type":"RealEstateOrganization","name":"United Realty Group Inc."}},"address":{{"@type":"PostalAddress","streetAddress":"{ADDR_LINE1}","addressLocality":"Tamarac","addressRegion":"FL","postalCode":"33321","addressCountry":"US"}},"areaServed":["Broward County, FL","Palm Beach County, FL","Plantation","Sunrise","Fort Lauderdale","Tamarac","Lauderhill","Davie","Weston","Pembroke Pines"]}}
</script>
</head>
<body>
<div class="topbar"><div class="wrap topbar-inner"><span>{LICNAME}</span><span><a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">♚</span><span><span class="brand-name">Jeremy Esperant</span><span class="brand-sub">Sales Associate | United Realty Group Inc.</span></span></a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">☰</button>
    <nav class="nav" aria-label="Primary">{links}<a class="btn btn-gold btn-sm" href="contact.html#book">{CTA}</a></nav>
  </div>
</header>
<main>
'''

def foot():
    return f'''</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-name">{LICNAME}</p>
      <p>Brokerage office: United Realty Group Inc.<br>{ADDR_LINE1}<br>{ADDR_LINE2}</p>
      <p><a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <p class="footer-head">Explore</p>
      <p><a href="index.html">Home</a> · <a href="about.html">About</a> · <a href="listings.html">Listings</a> · <a href="contact.html">Contact</a></p>
      <p class="footer-head">Areas</p>
      <p>Plantation · Sunrise · Fort Lauderdale · Tamarac · Lauderhill · Davie · Weston · Pembroke Pines · Broward &amp; Palm Beach Counties</p>
    </div>
    <div class="compliance">
      <p class="eho"><span class="eho-badge" aria-hidden="true">⌂</span> Equal Housing Opportunity</p>
      <p>{LICENSE}. Licensed in the State of Florida. Real estate services provided through United Realty Group Inc., {ADDR}.</p>
      <p>Information deemed reliable but not guaranteed. Featured properties are examples only and are not offered for sale by Jeremy Esperant unless stated. This is the personal website of a sales associate.</p>
    </div>
  </div>
  <div class="wrap footer-bottom">© <span id="yr">2026</span> Jeremy Esperant · thekingeffectinc-cloud.github.io/jeremyesperant-site</div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''

LEAFLET = '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">\n'
MAPJS = '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>\n<script src="js/counties.js"></script>\n<script src="js/map.js"></script>\n'

def map_block(heading=True):
    h = '<h2>Service area map</h2>\n<p class="section-lead">Centered on the United Realty Group office in Tamarac, right near the Broward–Palm Beach county line. Shaded: Broward County (teal) and Palm Beach County (gold).</p>' if heading else ''
    return f'''{h}
<div class="map-card">
  <div id="service-map" class="service-map" role="img" aria-label="Map of Broward and Palm Beach counties centered on {ADDR}">
    <noscript><p class="map-fallback">Map requires JavaScript. Office: {ADDR}.</p></noscript>
  </div>
  <div class="map-legend">
    <span><i class="sw sw-broward"></i>Broward County</span>
    <span><i class="sw sw-pb"></i>Palm Beach County</span>
    <span><i class="sw sw-pin"></i>URG office · {ADDR}</span>
    <a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps ↗</a>
  </div>
</div>
'''

def contact_form(ctx):
    return f'''<form class="card form js-mailto-form" data-to="{EMAIL}" data-subject="{ctx}">
  <p class="form-agent">{LICNAME}</p>
  <div class="form-row"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" autocomplete="tel"></label></div>
  <label>Email<input name="email" type="email" required autocomplete="email"></label>
  <label>I want to…<select name="goal"><option>Sell my home</option><option>Buy a home</option><option>Get help selling by owner (FSBO)</option><option>Buy or sell a condo / 55+</option><option>Just get a home value</option></select></label>
  <label>Property address or area (optional)<input name="property"></label>
  <label>Message<textarea name="message" rows="4"></textarea></label>
  <button class="btn btn-primary" type="submit">Send to Jeremy</button>
  <p class="fine">Opens your email app addressed to {EMAIL}. Prefer to talk? Call or text <a href="{TEL}">{PHONE}</a>.</p>
</form>'''

AREAS = ["Plantation","Sunrise","Fort Lauderdale","Tamarac","Lauderhill","Davie","Weston","Pembroke Pines"]

# ---------------- HOME ----------------
home = head("Jeremy Esperant | Broward Realtor | Plantation, Sunrise & Fort Lauderdale",
  "Jeremy Esperant, Sales Associate with United Realty Group Inc. Buying, selling and by-owner (FSBO) help in Plantation, Sunrise, Fort Lauderdale and across Broward County, FL.",
  "index.html", LEAFLET) + f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Broward County Real Estate · United Realty Group Inc.</p>
      <h1>Your Broward Home Expert — Buying, Selling &amp; By-Owner Help in Plantation, Sunrise &amp; Fort Lauderdale</h1>
      <p class="slogan">Make your next move your best move!</p>
      <p class="slogan-sub">I plan three moves ahead so you don't have to.</p>
      <div class="hero-actions">
        <a class="btn btn-gold btn-lg" href="contact.html#book">♞ {CTA}</a>
        <a class="btn btn-ghost" href="#value">Get my home value</a>
      </div>
      <p class="hero-contact">{LICNAME}<br><a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <figure class="hero-photo"><img src="img/jeremy-esperant.jpg" alt="Jeremy Esperant, Sales Associate with United Realty Group Inc." width="852" height="1024"></figure>
  </div>
</section>

<section class="section">
  <div class="wrap intro">
    <h2>Local, strategic, and on your side</h2>
    <p>I'm Jeremy Esperant, a Florida-licensed Sales Associate with United Realty Group Inc. I help Broward families and investors buy, sell, and price homes with a game plan — from the first conversation to the closing table. Whether you're listing a single-family home in Plantation, downsizing into a Sunrise 55+ community, or trying to sell on your own, I'll map out your next moves before you make them.</p>
    <a href="about.html">More about Jeremy →</a>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <h2>How I can help</h2>
    <div class="cards-4">
      <article class="card svc"><span class="svc-icon">♜</span><h3>Sell</h3><p>Pricing backed by local comps, sharp marketing, and tough negotiation to net you more.</p><a href="contact.html">Plan my sale →</a></article>
      <article class="card svc"><span class="svc-icon">♝</span><h3>Buy</h3><p>First-time and move-up buyers: search, offers, inspections and closing, explained step by step.</p><a href="listings.html">Start searching →</a></article>
      <article class="card svc"><span class="svc-icon">♞</span><h3>By-Owner (FSBO) Help</h3><p>Selling on your own? Get a free pricing check and an honest look at when an agent pays for itself.</p><a href="contact.html">Get FSBO help →</a></article>
      <article class="card svc"><span class="svc-icon">♛</span><h3>Condos &amp; 55+</h3><p>Associations, assessments, insurance and inspections — know what you're buying in Broward's condo market.</p><a href="contact.html">Ask about condos →</a></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Featured properties</h2><a href="listings.html">See all listings →</a></div>
    <div class="cards-3">
      <article class="card listing"><div class="ph ph1"><span>Photo coming soon</span></div><div class="listing-body"><p class="tag">Sample</p><h3>Updated 2/2 Condo</h3><p class="muted">Plantation, FL</p><p class="price">Price on request</p></div></article>
      <article class="card listing"><div class="ph ph2"><span>Photo coming soon</span></div><div class="listing-body"><p class="tag">Sample</p><h3>3/2 Pool Home</h3><p class="muted">Sunrise, FL</p><p class="price">Price on request</p></div></article>
      <article class="card listing"><div class="ph ph3"><span>Photo coming soon</span></div><div class="listing-body"><p class="tag">Sample</p><h3>Lake-View Townhome</h3><p class="muted">Davie, FL</p><p class="price">Price on request</p></div></article>
    </div>
    <p class="fine">Placeholder cards — replace with Jeremy's active listings or an IDX feed.</p>
  </div>
</section>

<section class="section section-alt" id="areas">
  <div class="wrap">
    <h2>Areas served</h2>
    <ul class="area-grid">{"".join(f"<li>{a}</li>" for a in AREAS)}<li>Broward County</li><li>Palm Beach County</li></ul>
    {map_block()}
  </div>
</section>

<section class="section" id="value">
  <div class="wrap grid-2">
    <div>
      <h2>What's your home worth?</h2>
      <p>Get a free, no-pressure price opinion based on recent Broward sales — not just an online estimate. Tell me about your property and I'll follow up within one business day.</p>
      <p><a class="btn btn-gold" href="contact.html#book">♞ {CTA}</a></p>
      <p class="muted">Or call/text <a href="{TEL}">{PHONE}</a></p>
    </div>
    {contact_form("Home value request")}
  </div>
</section>
''' + foot().replace('<script src="js/main.js"></script>', '<script src="js/main.js"></script>\n' + MAPJS)

# ---------------- ABOUT ----------------
about = head("About Jeremy Esperant | Sales Associate, United Realty Group Inc.",
  "Meet Jeremy Esperant, Florida-licensed Sales Associate with United Realty Group Inc. serving Plantation, Sunrise, Fort Lauderdale and Broward County.",
  "about.html") + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">About</p><h1>Meet Jeremy Esperant</h1><p class="lead">{LICNAME}</p></div></section>
<section class="section">
  <div class="wrap grid-2 about-grid">
    <figure class="about-photo"><img src="img/jeremy-esperant.jpg" alt="Jeremy Esperant headshot" width="852" height="1024"></figure>
    <div>
      <h2>Strategy first, every move</h2>
      <p>Jeremy Esperant is a South Florida local and a Florida-licensed Sales Associate with United Realty Group Inc., working out of the brokerage's office at {ADDR}. He serves buyers and sellers across Broward County — Plantation, Sunrise, Fort Lauderdale, Tamarac, Lauderhill, Davie, Weston and Pembroke Pines — and neighboring Palm Beach County.</p>
      <p>Before real estate, Jeremy spent years leading teams in customer-facing retail management, where he learned to listen first, explain clearly, and follow through. He brings that same approach to every transaction, along with a chess player's habit of thinking several moves ahead: anticipating inspection issues, appraisal gaps, condo-association questions and negotiation turns before they become problems.</p>
      <p>Jeremy also works closely with homeowners trying to sell by owner (FSBO), offering honest pricing guidance and a clear picture of what full representation adds.</p>
      <h3>What clients can expect</h3>
      <ul class="checks">
        <li>A written game plan for your sale or purchase</li>
        <li>Fast, direct communication — call or text <a href="{TEL}">{PHONE}</a></li>
        <li>Local pricing based on real Broward comps</li>
        <li>Condo, 55+ and first-time buyer know-how</li>
      </ul>
      <div class="card license-card">
        <h3>License &amp; brokerage</h3>
        <dl>
          <dt>Name</dt><dd>Jeremy Esperant</dd>
          <dt>Role</dt><dd>Sales Associate, State of Florida</dd>
          <dt>License</dt><dd>{LICENSE.replace("FL License #: ","")}</dd>
          <dt>Brokerage</dt><dd>United Realty Group Inc.</dd>
          <dt>Office</dt><dd>{ADDR}</dd>
        </dl>
      </div>
      <p><a class="btn btn-gold" href="contact.html#book">♞ {CTA}</a></p>
    </div>
  </div>
</section>
''' + foot()

# ---------------- LISTINGS ----------------
samples = [
 ("Updated 2/2 Condo","Plantation, FL","2 bd · 2 ba · ~950 sq ft","Condo","ph1"),
 ("3/2 Pool Home","Sunrise, FL","3 bd · 2 ba · ~1,600 sq ft","Single-family","ph2"),
 ("Lake-View Townhome","Davie, FL","3 bd · 2.5 ba · ~1,700 sq ft","Townhome","ph3"),
 ("55+ Garden Condo","Sunrise Lakes, Sunrise, FL","2 bd · 2 ba · ~1,100 sq ft","55+ Condo","ph2"),
 ("Starter Villa","Tamarac, FL","2 bd · 2 ba · ~1,200 sq ft","Villa","ph1"),
 ("Family Home Near Parks","Pembroke Pines, FL","4 bd · 2 ba · ~2,000 sq ft","Single-family","ph3"),
]
cards = "".join(f'''<article class="card listing" data-type="{t}"><div class="ph {p}"><span>Photo coming soon</span></div><div class="listing-body"><p class="tag">Sample · {t}</p><h3>{n}</h3><p class="muted">{c}</p><p>{d}</p><p class="price">Price on request</p><a href="contact.html">Ask Jeremy about this home →</a></div></article>''' for n,c,d,t,p in samples)
listings = head("Listings & Home Search | Jeremy Esperant, Broward Realtor",
  "Featured Broward County homes and condos plus home search help from Jeremy Esperant, Sales Associate with United Realty Group Inc.",
  "listings.html") + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Listings</p><h1>Featured Homes &amp; Home Search</h1><p class="lead">{LICNAME} · <a href="{TEL}">{PHONE}</a></p></div></section>
<section class="section">
  <div class="wrap">
    <div class="notice">These are <strong>sample placeholder cards</strong> to show the layout. Replace with Jeremy's active listings or an IDX/MLS search widget (see README).</div>
    <div class="filters" role="group" aria-label="Filter listings">
      <button class="chip is-active" data-filter="all">All</button><button class="chip" data-filter="Single-family">Single-family</button><button class="chip" data-filter="Condo">Condo</button><button class="chip" data-filter="55+ Condo">55+</button><button class="chip" data-filter="Townhome">Townhome</button><button class="chip" data-filter="Villa">Villa</button>
    </div>
    <div class="cards-3 js-listings">{cards}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap grid-2">
    <div>
      <h2>Search all Broward homes</h2>
      <p>Full MLS search is coming soon. In the meantime, tell me your must-haves — area, budget, beds/baths, condo or house — and I'll send matching homes, including new by-owner (FSBO) listings, as they hit the market.</p>
      <div id="idx-search" class="idx-placeholder">IDX search widget placeholder</div>
    </div>
    {contact_form("Home search request")}
  </div>
</section>
''' + foot()

# ---------------- CONTACT ----------------
contact = head("Contact Jeremy Esperant | United Realty Group Inc., Tamarac, FL",
  f"Contact Jeremy Esperant, Sales Associate with United Realty Group Inc. Call {PHONE}. Office: {ADDR}.",
  "contact.html", LEAFLET) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Contact</p><h1>Let's plan your next move</h1><p class="lead">{LICNAME}</p></div></section>
<section class="section" id="book">
  <div class="wrap grid-2">
    <div>
      <div class="card cta-card">
        <h2>Free strategy session</h2>
        <p>A 20-minute call to map out your sale, purchase, or by-owner plan — no pressure, no obligation.</p>
        <p><a class="btn btn-gold btn-lg" href="{TEL}">♞ {CTA}</a></p>
        <p class="muted">Tap to call, or <a href="mailto:{EMAIL}?subject=Strategy%20session%20request">email to schedule</a>.</p>
      </div>
      <div class="card contact-details">
        <h3>Jeremy Esperant</h3>
        <p class="muted">Sales Associate | United Realty Group Inc.</p>
        <p><strong>Phone / text:</strong> <a href="{TEL}">{PHONE}</a></p>
        <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><strong>Office:</strong><br><span class="office-address">United Realty Group Inc.<br>{ADDR_LINE1}<br>{ADDR_LINE2}</span></p>
        <p><a href="{MAPS}" target="_blank" rel="noopener">Get directions ↗</a></p>
        <p><strong>Hours:</strong> Mon–Sat 9am–7pm · Sunday by appointment</p>
      </div>
    </div>
    {contact_form("Website inquiry")}
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    {map_block()}
  </div>
</section>
''' + foot().replace('<script src="js/main.js"></script>', '<script src="js/main.js"></script>\n' + MAPJS)

for name, html in [("index.html",home),("about.html",about),("listings.html",listings),("contact.html",contact)]:
    open(name,"w").write(html)
print("ok")
