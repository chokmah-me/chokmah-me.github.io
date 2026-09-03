"""Sort research/feed.xml entries newest-first by <updated>."""
from __future__ import annotations

import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "research" / "feed.xml"
text = p.read_text(encoding="utf-8")
head, rest = text.split("<entry>", 1)
entries = ["<entry>" + e for e in rest.split("<entry>") if e.strip()]
# last chunk includes closing feed
fixed = []
tail = ""
for e in entries:
    if "</feed>" in e:
        e, tail = e.split("</feed>", 1)
        fixed.append(e)
        tail = "</feed>" + tail
    else:
        fixed.append(e)


def key(e: str) -> str:
    m = re.search(r"<updated>([^<]+)</updated>", e)
    return m.group(1) if m else "0000"


fixed.sort(key=key, reverse=True)
out = head + "".join(fixed) + tail
p.write_text(out, encoding="utf-8", newline="\n")
print("entries", len(fixed), "first_updated", key(fixed[0]))
m = re.search(r"<title>([^<]+)</title>", fixed[0])
print("first_title", m.group(1) if m else "?")
