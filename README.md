# JeremyEsperant.com — personal real estate site (static)

Target domain: **JeremyEsperant.com** (not purchased/registered yet).

Static HTML/CSS + a little JS for Jeremy Esperant, Sales Associate | United Realty Group Inc.
Brokerage office used site-wide: **7300 W. McNab Road, Suite 119, Tamarac, FL 33321**.

## Open locally
- Double-click `index.html`, or
- `cd jeremyesperant-site && python3 -m http.server 8080` → http://localhost:8080

(The service-area map and fonts load from unpkg/OpenStreetMap/Google Fonts, so they need internet.)

## Files
- `index.html` home · `about.html` · `listings.html` · `contact.html`
- `css/styles.css` shared styles · `js/main.js` menu/forms/filters · `js/map.js` Leaflet map · `js/counties.js` Broward + Palm Beach county outlines
- `img/jeremy-esperant.jpg` headshot
- `build.py` regenerates all four pages from one template (edit shared header/footer/address there, then `python3 build.py`)

## Before launch (TODO)
- Replace `SL[pending — add number]` with Jeremy's FL license number (in `build.py`, `LICENSE`).
- Replace sample listing cards with real listings or an IDX widget (`#idx-search` on listings page).
- Contact forms currently open the visitor's email app (mailto). Swap for Formspree/Netlify Forms etc. when hosted.
- Confirm brokerage advertising rules with URG (Fla. Admin. Code 61J2-10.025).
- After hosting: Google Search Console, link Google Business Profile, Zillow, Realtor.com.
