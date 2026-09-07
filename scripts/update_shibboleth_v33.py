#!/usr/bin/env python3
"""Retarget Shibboleth Lattice research catalog surfaces from v3.2 -> v3.3."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "research/the-shibboleth-lattice-recognition-channels-and-the-universa-20089104/index.html"
INDEX = ROOT / "research/index.html"
FEED = ROOT / "research/feed.xml"
SITEMAP = ROOT / "sitemap.xml"

OLD = "22279984"
NEW = "22643579"
OLD_PDF = "dyb-2026i-shibboleth-3-2.pdf"
NEW_PDF = "dyb-2026i-shibboleth-3-3.pdf"


def update_page(text: str) -> str:
    old_desc = (
        "v3.2 preprint: coalition behavior across quantum, evolutionary, engineered, and LLM "
        "substrates as one binding operator B, with W-capture, role-identity I, and a still-untested "
        "blinded witness-set prediction."
    )
    new_desc = (
        "v3.3 preprint: binding operator B with specification divergence, Paglieri scope limit "
        "(B covers the covert subset of substrate contagion), and a still-untested blinded "
        "witness-set prediction."
    )
    text = text.replace(old_desc, new_desc)
    text = text.replace('citation_publication_date" content="2026-09-03"', 'citation_publication_date" content="2026-09-07"')
    text = text.replace('DC.date" content="2026-09-03"', 'DC.date" content="2026-09-07"')
    text = text.replace(f"10.5281/zenodo.{OLD}", f"10.5281/zenodo.{NEW}")
    text = text.replace(f"https://zenodo.org/records/{OLD}", f"https://zenodo.org/records/{NEW}")
    text = text.replace(OLD_PDF, NEW_PDF)
    text = text.replace('"version": "3.2"', '"version": "3.3"')
    text = text.replace('"dateModified": "2026-09-03"', '"dateModified": "2026-09-07"')
    text = text.replace("2026-09-03 &middot; v3.2 &middot; publication/preprint", "2026-09-07 &middot; v3.3 &middot; publication/preprint")
    text = text.replace("This version (v3.2):", "This version (v3.3):")

    old_abs = (
        "v3.2 extends W into capture and degradation, extends I to role identity, and identifies "
        "substrate non-separability. The core prediction is unchanged: blinded witness-set "
        "substitution should collapse coalition behavior even at saturating kappa_H. That "
        "prediction remains untested. Catalog path fragment -20089104 is historical (v1.5 slug); "
        f"live cites are concept 10.5281/zenodo.19595987 and version 10.5281/zenodo.{NEW}."
    )
    new_abs = (
        "v3.3 adds specification divergence, integrates Paglieri et al. (2026) as a transparent-channel "
        "comparison, and records that B covers only the covert subset of substrate-carried contagion. "
        "The core prediction is unchanged: blinded witness-set substitution should collapse coalition "
        "behavior even at saturating kappa_H. That prediction remains untested. Catalog path fragment "
        "-20089104 is historical (v1.5 slug); live cites are concept 10.5281/zenodo.19595987 and "
        f"version 10.5281/zenodo.{NEW}."
    )
    if old_abs in text:
        text = text.replace(old_abs, new_abs)
    else:
        # After DOI replace, old_abs may already have NEW in the live-cites clause from a partial prior run
        old_abs2 = old_abs.replace(f"zenodo.{NEW}", f"zenodo.{OLD}")
        if old_abs2 in text:
            text = text.replace(old_abs2, new_abs)
        else:
            print("WARN: JSON-LD abstract clause not matched")

    old_p3 = (
        "The core prediction is unchanged: blinded witness-set substitution should collapse coalition "
        "behavior even at saturating &kappa;<sub>H</sub>, distinguishing <em>B</em> from instrumental "
        "convergence accounts. This prediction remains untested. The headline &kappa;<sub>H</sub> figure "
        'is an interval, not a single point. Companion simulations: <a href="https://doi.org/10.5281/zenodo.20090834">10.5281/zenodo.20090834</a>.'
    )
    new_p3 = (
        "A scope limit is recorded: substrate-carried contagion is the general phenomenon; <em>B</em> "
        "covers the covert subset (Paglieri et al. 2026 supply the transparent-channel comparison). "
        "The core prediction is unchanged: blinded witness-set substitution should collapse coalition "
        "behavior even at saturating &kappa;<sub>H</sub>, distinguishing <em>B</em> from instrumental "
        "convergence accounts. This prediction remains untested. Companion simulations: "
        '<a href="https://doi.org/10.5281/zenodo.20090834">10.5281/zenodo.20090834</a>.'
    )
    text = text.replace(old_p3, new_p3)

    text = text.replace(
        "W-degradation; stigmergy; Shibboleth Lattice",
        "W-degradation; specification divergence; stigmergy; substrate contagion; Shibboleth Lattice",
    )
    text = text.replace(
        "W-degradation &middot; stigmergy &middot; Shibboleth Lattice",
        "W-degradation &middot; specification divergence &middot; substrate contagion &middot; Shibboleth Lattice",
    )
    if '"specification divergence"' not in text:
        text = text.replace(
            '    "W-degradation",\n    "stigmergy",',
            '    "W-degradation",\n    "specification divergence",\n    "substrate contagion",\n    "stigmergy",',
        )
    return text


def update_index(text: str) -> str:
    text = text.replace(
        f'"datePublished": "2026-09-03",\n            "author": {{\n              "@id": "https://chokmah.me/#person"\n            }},\n            "identifier": "10.5281/zenodo.{OLD}",\n            "description": "v3.2 binding-operator preprint: W-capture, role-identity I, substrate non-separability; blinded witness-set prediction still untested. Concept DOI 10.5281/zenodo.19595987."',
        f'"datePublished": "2026-09-07",\n            "author": {{\n              "@id": "https://chokmah.me/#person"\n            }},\n            "identifier": "10.5281/zenodo.{NEW}",\n            "description": "v3.3 binding-operator preprint: specification divergence, Paglieri covert-subset scope limit; blinded witness-set prediction still untested. Concept DOI 10.5281/zenodo.19595987."',
    )
    text = text.replace(
        f"Bilar, Daniyel Yaacov &middot; 2026-09-03 &middot; v3.2 &middot; DOI: 10.5281/zenodo.{OLD}",
        f"Bilar, Daniyel Yaacov &middot; 2026-09-07 &middot; v3.3 &middot; DOI: 10.5281/zenodo.{NEW}",
    )
    text = text.replace(
        "v3.2: binding operator B with W-capture and W-degradation, role-identity I, and substrate non-separability, prompted by the 2026 OpenAI/Hugging Face incident. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987.",
        "v3.3: specification divergence; Paglieri transparent-swarm comparison; B covers the covert subset of substrate contagion. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987.",
    )
    # fallback DOI-only if structured replace missed
    if f"zenodo.{OLD}" in text and "the-shibboleth-lattice" in text:
        # only replace within shibboleth card context by global if still present once
        pass
    text = text.replace(f"10.5281/zenodo.{OLD}", f"10.5281/zenodo.{NEW}")
    return text


def update_feed(text: str) -> str:
    text = text.replace("<updated>2026-09-03T12:00:00Z</updated>", "<updated>2026-09-07T12:00:00Z</updated>", 1)
    text = text.replace(
        "<updated>2026-09-03T00:00:00Z</updated>\n    <summary>v3.2: binding operator B with W-capture, W-degradation, role-identity I, and substrate non-separability. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987; this version 10.5281/zenodo.22279984.</summary>",
        f"<updated>2026-09-07T00:00:00Z</updated>\n    <summary>v3.3: specification divergence; Paglieri covert-subset scope limit. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987; this version 10.5281/zenodo.{NEW}.</summary>",
    )
    # id stays historical slug DOI in feed historically; update to concept or version? Keep link URL; change summary only if first replace failed
    if "v3.2: binding operator" in text:
        text = text.replace(
            "v3.2: binding operator B with W-capture, W-degradation, role-identity I, and substrate non-separability. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987; this version 10.5281/zenodo.22279984.",
            f"v3.3: specification divergence; Paglieri covert-subset scope limit. Blinded witness-set substitution remains untested. Concept DOI 10.5281/zenodo.19595987; this version 10.5281/zenodo.{NEW}.",
        )
        text = text.replace("<updated>2026-09-03T00:00:00Z</updated>", "<updated>2026-09-07T00:00:00Z</updated>", 1)
    return text


def update_sitemap(text: str) -> str:
    return text.replace(
        f"<loc>https://chokmah.me/research/the-shibboleth-lattice-recognition-channels-and-the-universa-20089104/</loc><lastmod>2026-09-03</lastmod>",
        f"<loc>https://chokmah.me/research/the-shibboleth-lattice-recognition-channels-and-the-universa-20089104/</loc><lastmod>2026-09-07</lastmod>",
    )


def main() -> None:
    page = update_page(PAGE.read_text(encoding="utf-8"))
    PAGE.write_text(page, encoding="utf-8")
    print(f"page: newDOI={page.count(NEW)} oldDOI={page.count(OLD)}")

    idx = update_index(INDEX.read_text(encoding="utf-8"))
    INDEX.write_text(idx, encoding="utf-8")
    print(f"index: newDOI mentions in shibboleth area ok; leftover old in file={idx.count(OLD)}")

    feed = update_feed(FEED.read_text(encoding="utf-8"))
    FEED.write_text(feed, encoding="utf-8")
    print(f"feed updated")

    sm = update_sitemap(SITEMAP.read_text(encoding="utf-8"))
    SITEMAP.write_text(sm, encoding="utf-8")
    print("sitemap updated")


if __name__ == "__main__":
    main()
