"""Sort research/index.html cards and JSON-LD ItemList newest-first."""
from __future__ import annotations

import json
import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "research" / "index.html"
text = p.read_text(encoding="utf-8")

body_start = text.index('<h2 class="year-head">2026</h2>')
body_end = text.index("<footer>", body_start)
head = text[:body_start]
tail = text[body_end:]
cards_html = text[body_start:body_end]
cards = re.findall(r'<div class="card">.*?</div>\s*', cards_html, re.S)
if not cards:
    raise SystemExit("no cards found")

dated = []
for c in cards:
    m = re.search(r"&middot;\s*(\d{4}-\d{2}-\d{2})", c)
    if not m:
        raise SystemExit("card missing date: " + c[:160])
    dated.append((m.group(1), c))
dated.sort(key=lambda x: x[0], reverse=True)

y2026 = [c for dt, c in dated if dt.startswith("2026")]
y2025 = [c for dt, c in dated if dt.startswith("2025")]
new_cards = '<h2 class="year-head">2026</h2>\n' + "".join(y2026)
if y2025:
    new_cards += '    <h2 class="year-head">2025</h2>\n' + "".join(y2025)
text2 = head + new_cards + tail

m = re.search(
    r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', text2, re.S
)
if not m:
    raise SystemExit("json-ld not found")
js = json.loads(m.group(1))
itemlist = next(x for x in js["@graph"] if x.get("@type") == "ItemList")
elems = itemlist["itemListElement"]

url_date = {}
for dt, c in dated:
    um = re.search(r'href="(https://chokmah.me/research/[^"]+)/"', c)
    if um:
        url_date[um.group(1).rstrip("/")] = dt


def sort_key(e):
    url = e["item"]["url"].rstrip("/")
    return url_date.get(url, e["item"].get("datePublished", "0000-00-00"))


elems.sort(key=sort_key, reverse=True)
for i, e in enumerate(elems, 1):
    e["position"] = i
    url = e["item"]["url"].rstrip("/")
    if url in url_date:
        e["item"]["datePublished"] = url_date[url]
itemlist["itemListElement"] = elems
itemlist["numberOfItems"] = len(elems)

new_json = json.dumps(js, indent=2, ensure_ascii=False)
text3 = text2[: m.start(1)] + new_json + text2[m.end(1) :]
p.write_text(text3, encoding="utf-8", newline="\n")
print(f"cards={len(dated)} first={dated[0][0]} json_first={elems[0]['item']['datePublished']} {elems[0]['item']['name'][:60]}")
