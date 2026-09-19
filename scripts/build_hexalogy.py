# -*- coding: utf-8 -*-
"""Bouwt de zes boeken van de hexalogie in vierkant formaat (21 × 21 cm).

    python3 scripts/build_hexalogy.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))

from artwork import Fineliner, GlassPanels, QRCode  # noqa: E402
from glossary import GLOSSARY  # noqa: E402
from hexalogy import BOOKS  # noqa: E402
from hexalogy.extra_sources import EXTRA_CLAIMS, EXTRA_SOURCES  # noqa: E402
from sources import CLAIMS, SOURCES  # noqa: E402
from typeset import (  # noqa: E402
    LINE,
    OUT,
    WINE,
    Book,
    Box,
    Rule,
    data_table,
    mark,
    register_fonts,
    styles,
)

SQUARE = (210 * mm, 210 * mm)
VERSION = "Editie 01 · 2026"
CLAIM_URL = "https://id-preview--73c9b015-931b-4472-a45c-d1bff8769711.lovable.app/claims"
REF_RE = re.compile(r"(BR-\d\d|CL-\d\d)")

ALL_SOURCES = list(SOURCES) + list(EXTRA_SOURCES)
ALL_CLAIMS = list(CLAIMS) + list(EXTRA_CLAIMS)


def render_blocks(blocks, st, width, story):
    """Zet de gedeelde hoofdstukblokken naar ReportLab-elementen."""
    for block in blocks:
        kind = block[0]
        if kind == "lead":
            story.append(Paragraph(block[1], st["lead"]))
        elif kind == "p":
            story.extend([Paragraph(block[1], st["body"]), Spacer(1, 4.2)])
        elif kind == "h2":
            story.append(Paragraph(block[1], st["h2"]))
        elif kind == "h3":
            story.append(Paragraph(block[1], st["h3"]))
        elif kind == "q":
            story.append(KeepTogether([Paragraph("“" + block[1] + "”", st["quote"]), Paragraph(block[2], st["quote_src"])]))
        elif kind == "ul":
            for item in block[1]:
                story.append(Paragraph(item, st["bullet"], bulletText="—"))
            story.append(Spacer(1, 5))
        elif kind == "box":
            story.extend([Spacer(1, 4), Box([Paragraph(block[1].upper(), st["box_title"]), Paragraph(block[2], st["box_body"])], width), Spacer(1, 9)])
        elif kind == "table":
            rows = [[cell for cell in row] for row in block[1]]
            widths = [width * part / 100.0 for part in block[2]]
            story.extend([Spacer(1, 4), data_table(rows, widths, st), Spacer(1, 10)])


def collect_refs(chapters) -> set[str]:
    found: set[str] = set()

    def scan(x):
        if isinstance(x, str):
            found.update(REF_RE.findall(x))
        elif isinstance(x, (list, tuple)):
            for i in x:
                scan(i)

    for ch in chapters:
        scan(ch["deck"])
        scan(ch["blocks"])
    return found


def glossary_terms(chapters) -> list[tuple[str, str]]:
    blob = " ".join(
        [ch["title"] + " " + ch["deck"] + " " + repr(ch["blocks"]) for ch in chapters]
    ).lower()
    picked = [(t, d) for t, d in GLOSSARY
              if t.lower().split(" /")[0].split(" (")[0] in blob or t.lower()[:6] in blob]
    return picked or list(GLOSSARY)


def cover(book, st, width, story):
    story.append(Spacer(1, 26))
    story.append(Paragraph("DE MARKTPLAATS VAN DE ZIEL · HEXALOGIE", st["cover_sub"]))
    story.append(Spacer(1, 10))
    story.append(GlassPanels(width, 150, variant=int(book["roman"].count("I") + len(book["roman"]))))
    story.append(Spacer(1, 18))
    story.append(Paragraph(f"BOEK {book['roman']}", st["chapter_num"]))
    story.append(Paragraph(book["title"], st["cover_title"]))
    story.append(Spacer(1, 10))
    story.append(Rule(width, 1.1, WINE, 8))
    story.append(Spacer(1, 6))
    story.append(Paragraph(book["subtitle"], st["lead"]))
    story.append(Spacer(1, 22))
    story.append(Fineliner(width, 60, variant=len(book["roman"]) % 3))
    story.append(Spacer(1, 14))
    story.append(Rule(width, 0.6, LINE, 6))
    story.append(Paragraph(
        f"Jona Zeno De Smet · {VERSION} · 21 × 21 cm<br/>"
        "Onafhankelijke onderzoeks- en essaypublicatie · vrij verspreidbaar voor "
        "educatieve en onderzoeksdoeleinden.", st["caption"]))
    story.append(PageBreak())


def title_page(book, st, width, story):
    story.append(Spacer(1, 40))
    story.append(Paragraph(f"BOEK {book['roman']} VAN ZES", st["chapter_num"]))
    story.append(Paragraph(book["title"], st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    story.append(Paragraph(book["deck"], st["lead"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Deze uitgave maakt deel uit van een reeks van zes boeken. Elk deel is zelfstandig leesbaar "
        "en draagt zijn eigen bronnen- en claimregister. Alles wat als feit wordt gepresenteerd, is "
        "terug te voeren op een genummerde bron achterin. Waar een bewering dat niveau niet haalt, "
        "staat zij als onbevestigd of als hypothese geregistreerd en wordt zij in de tekst zo genoemd.",
        st["body"]))
    story.append(Spacer(1, 8))
    story.append(Box([
        Paragraph("LEESWIJZER BIJ DE STATUSAANDUIDINGEN", st["box_title"]),
        Paragraph(
            "VASTGESTELD — meervoudig gedocumenteerd in primaire of onafhankelijke bronnen. "
            "GEDOCUMENTEERD — één degelijke bron, nog niet onafhankelijk bevestigd. "
            "BETWIST — partijen spreken elkaar tegen of de zaak is onder de rechter. "
            "ONBEVESTIGD — plausibel, maar zonder controleerbaar bewijs in dit dossier. "
            "HYPOTHESE — interpretatiekader van de auteur, uitdrukkelijk geen feit.",
            st["box_body"])], width))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "De zes delen: I De technologische deceptie · II De financiële schaduweconomie · "
        "III De neurobiologie van de verslaving · IV De sociologische implosie · "
        "V Het juridisch failliet &amp; modelwetgeving · VI Het post-digitale verzet.",
        st["caption"]))
    story.append(PageBreak())


def contents(book, st, width, story):
    story.append(Paragraph("INHOUD", st["chapter_num"]))
    story.append(Paragraph("Opbouw van dit deel", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    rows = [["", "HOOFDSTUK", "WAT HET VASTSTELT"]]
    for ch in book["chapters"]:
        rows.append([ch["num"], ch["title"], ch["deck"].split(".")[0] + "."])
    story.append(data_table(rows, [width * 0.07, width * 0.37, width * 0.56], st))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Achterin: begrippenlijst, claimregister, bronnenregister en colofon met QR-code naar "
        "het live claimregister.", st["caption"]))
    story.append(PageBreak())


def back_matter(book, st, width, story):
    refs = collect_refs(book["chapters"])

    story.append(Paragraph("REGISTER I", st["chapter_num"]))
    story.append(Paragraph("Begrippenlijst", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    for term, definition in glossary_terms(book["chapters"]):
        story.append(Paragraph(
            f'<font name="SansBold" size="7.4">{term}</font> — {definition}', st["note"]))
    story.append(PageBreak())

    story.append(Paragraph("REGISTER II", st["chapter_num"]))
    story.append(Paragraph("Claimregister", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Elke bewering van dit deel staat hieronder met haar status en haar bronnen. Wie het oneens "
        "is, hoeft niet het geheel te bestrijden: het volstaat één regel te weerleggen.", st["body"]))
    story.append(Spacer(1, 8))
    rows = [["CODE", "STATUS", "BEWERING", "BRONNEN"]]
    claims = [c for c in ALL_CLAIMS if c[0] in refs] or ALL_CLAIMS[:6]
    for code, status, claim, srcs, note in claims:
        rows.append([code, status,
                     f"{claim}<br/><font size='6.6' color='#6e6965'>{note}</font>", srcs])
    story.append(data_table(rows, [width * 0.08, width * 0.18, width * 0.56, width * 0.18], st))
    story.append(PageBreak())

    story.append(Paragraph("REGISTER III", st["chapter_num"]))
    story.append(Paragraph("Bronnenregister", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Alle bronnen zijn openbaar en zonder betaalmuur of via een bibliotheek raadpleegbaar. "
        "Bronnen van marktpartijen worden uitsluitend gebruikt als bewijs van wat die partij zelf "
        "beweert.", st["body"]))
    story.append(Spacer(1, 8))
    for code, kind, title, meta, url in ALL_SOURCES:
        if code not in refs:
            continue
        story.append(Paragraph(
            f'<font name="MonoBold" size="6.4" color="#8b1e2d">{code}</font>  '
            f"<b>{title}</b> · {meta} · <font color='#6e6965'>{kind}</font> · "
            f"<font name='Mono' size='6.2' color='#6e6965'>{url}</font>", st["note"]))
    story.append(PageBreak())

    story.append(Paragraph("COLOFON", st["chapter_num"]))
    story.append(Paragraph(f"Boek {book['roman']} — {book['title']}", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Auteur: Jona Zeno De Smet. Architectuur en platform: Delplanche "
        "(delplanche.com · delplanche.cloud). Formaat 21 × 21 cm. Zetwerk in DejaVu Serif en "
        "DejaVu Sans. Papierkleur #fcfbf9, inkt #242325, accent #8b1e2d.", st["body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Correcties met bronvermelding worden verwerkt in de online-editie en vermeld in de "
        "versiegeschiedenis. Het claimregister op de website is de actuele versie; de QR-code "
        "hiernaast verwijst ernaar.", st["body"]))
    story.append(Spacer(1, 14))
    story.append(QRCode(CLAIM_URL, 78))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"Live claimregister: {CLAIM_URL}", st["caption"]))
    story.append(Spacer(1, 16))
    story.append(Rule(width, 0.6, LINE, 6))
    story.append(Paragraph(
        "© 2026 — Publiek archief voor controle en debat; vrij verspreidbaar voor educatieve en "
        "onderzoeksdoeleinden.", st["caption"]))


def build_book(book) -> str:
    st = styles(9.2, 13.4)
    path = str(OUT / f"{book['slug']}.pdf")
    doc = Book(path, SQUARE, f"BOEK {book['roman']} · {book['title'].upper()}",
               margins=(44, 44, 50, 42))
    width = doc.width
    story: list = []
    cover(book, st, width, story)
    title_page(book, st, width, story)
    contents(book, st, width, story)

    part = None
    for i, ch in enumerate(book["chapters"]):
        if ch["part"] != part:
            part = ch["part"]
            story.append(Paragraph(part, st["chapter_num"]))
            story.append(Rule(width, 0.6, LINE, 4))
            story.append(Spacer(1, 2))
        head = Paragraph(f"HOOFDSTUK {ch['num']}", st["chapter_num"])
        story.append(mark(head, f"{ch['num']} · {ch['title']}"))
        story.append(Paragraph(ch["title"], st["chapter_title"]))
        story.append(Rule(width, 0.8, WINE, 7))
        story.append(Spacer(1, 3))
        story.append(Paragraph(ch["deck"], st["lead"]))
        story.append(Spacer(1, 2))
        story.append(Fineliner(width, 34, variant=i % 3))
        story.append(Spacer(1, 6))
        render_blocks(ch["blocks"], st, width, story)
        story.append(PageBreak())

    back_matter(book, st, width, story)
    doc.build(story)
    return path


if __name__ == "__main__":
    register_fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    for b in BOOKS:
        print("geschreven:", build_book(b))
