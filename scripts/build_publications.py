# -*- coding: utf-8 -*-
"""Bouwt de publicaties: integrale editie en whitepaper.

    python3 scripts/build_publications.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, NextPageTemplate, PageBreak, Paragraph, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapters import CHAPTERS  # noqa: E402
from sources import CLAIMS, SOURCES, TIMELINE  # noqa: E402
from typeset import (  # noqa: E402
    INK,
    LINE,
    MUTED,
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

VERSION = "Versie 2.0 — herziene en volledig gedocumenteerde uitgave"
BR_RE = re.compile(r"\[(BR-\d\d|CL-\d\d)\]")


def m(text: str) -> str:
    """Zet bronverwijzingen om in kleine mono-verwijzingen."""
    return BR_RE.sub(
        lambda x: f'<font name="Mono" size="6.2" color="#8b1e2d"> {x.group(1)}</font>', text
    )


def render_blocks(blocks, st, width, story):
    for b in blocks:
        kind = b[0]
        if kind == "lead":
            story.append(Paragraph(m(b[1]), st["lead"]))
        elif kind == "p":
            story.append(Paragraph(m(b[1]), st["body"]))
            story.append(Spacer(1, 4.2))
        elif kind == "h2":
            story.append(Paragraph(b[1], st["h2"]))
        elif kind == "h3":
            story.append(Paragraph(b[1], st["h3"]))
        elif kind == "q":
            story.append(Spacer(1, 3))
            story.append(
                KeepTogether([
                    Paragraph("“" + b[1] + "”", st["quote"]),
                    Paragraph(m(b[2]), st["quote_src"]),
                ])
            )
        elif kind == "ul":
            for item in b[1]:
                story.append(Paragraph(m(item), st["bullet"], bulletText="—"))
            story.append(Spacer(1, 5))
        elif kind == "box":
            inner = [Paragraph(b[1].upper(), st["box_title"]), Paragraph(m(b[2]), st["box_body"])]
            story.append(Spacer(1, 4))
            story.append(Box(inner, width))
            story.append(Spacer(1, 9))
        elif kind == "table":
            rows = [[m(c) for c in row] for row in b[1]]
            widths = [width * p / 100.0 for p in b[2]]
            story.append(Spacer(1, 4))
            story.append(data_table(rows, widths, st))
            story.append(Spacer(1, 10))


def front_matter(st, width, story):
    story.append(Spacer(1, 96))
    story.append(Paragraph("DOSSIER · OPENBARE UITGAVE", st["cover_sub"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("De Marktplaats<br/>van de Ziel", st["cover_title"]))
    story.append(Spacer(1, 12))
    story.append(Rule(width, 1.1, WINE, 8))
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Een onderzoek naar uitbestede intimiteit: de chat-industrie achter de "
            "makerseconomie, haar software, haar contracten en het gat in het recht.",
            st["lead"],
        )
    )
    story.append(Spacer(1, 150))
    story.append(Rule(width, 0.6, LINE, 6))
    story.append(
        Paragraph(
            f"{VERSION}<br/>39 genummerde bronnen · 20 geregistreerde claims · "
            "11 hoofdstukken<br/>Vrij te verspreiden voor onderwijs- en onderzoeksdoeleinden.",
            st["caption"],
        )
    )
    story.append(PageBreak())

    # Verantwoording
    story.append(Paragraph("VOORAF", st["chapter_num"]))
    story.append(Paragraph("Wat dit document is, en wat het niet is", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 4))
    for para in [
        "Dit is een documentanalyse. Alles wat hierin als feit wordt gepresenteerd, is terug te "
        "voeren op een genummerde bron in het register achterin: een jaarrekening, een wettekst, "
        "een processtuk, een publieke productpagina of een journalistiek onderzoek waarvan de "
        "werkwijze is beschreven. Waar een bewering dat niveau niet haalt, staat zij in het "
        "claimregister met de status onbevestigd of hypothese, en wordt zij in hoofdstuk 10 "
        "uitdrukkelijk afgebakend.",
        "De eerste versie van dit dossier leed aan het gebrek dat zij zelf aan de sector "
        "verweet: grote woorden met weinig onderbouwing. Hoofdstukken beloofden getuigenissen "
        "en leverden bulletpoints. Die versie is vervallen. In deze uitgave staan de "
        "getuigenissen er letterlijk in, met naam van de publicatie en datum, en zijn de "
        "beweringen die het bewijs niet dragen ingetrokken of gedegradeerd.",
        "Het onderwerp is niet seksualiteit en niet het oordeel over sekswerk. Het onderwerp is "
        "één specifieke vraag: mag iemand betalen voor persoonlijk contact met een bepaald mens, "
        "zonder te weten dat een ander mens schrijft? Die vraag raakt de betalende consument, en "
        "zij raakt de maker wier naam wordt gebruikt door een bureau dat haar wachtwoord heeft.",
        "Er is geen wederhoor gevraagd aan de genoemde bedrijven. Dat is een beperking van deze "
        "uitgave en wordt in hoofdstuk 11 samen met de overige methodische keuzes verantwoord. "
        "Feitelijke onjuistheden worden gecorrigeerd zodra zij met bron worden gemeld.",
    ]:
        story.append(Paragraph(para, st["body"]))
        story.append(Spacer(1, 5))

    story.append(Spacer(1, 6))
    story.append(
        Box(
            [
                Paragraph("LEESWIJZER BIJ DE STATUSAANDUIDINGEN", st["box_title"]),
                Paragraph(
                    "VASTGESTELD — meervoudig gedocumenteerd in primaire of onafhankelijke bronnen. "
                    "GEDOCUMENTEERD — één degelijke bron, nog niet onafhankelijk bevestigd. "
                    "BETWIST — partijen spreken elkaar tegen, of de zaak is onder de rechter. "
                    "ONBEVESTIGD — plausibel, maar zonder controleerbaar bewijs in dit dossier. "
                    "HYPOTHESE — interpretatiekader van de auteur, uitdrukkelijk geen feit.",
                    st["box_body"],
                ),
            ],
            width,
        )
    )
    story.append(PageBreak())

    # Inhoud
    story.append(Paragraph("INHOUD", st["chapter_num"]))
    story.append(Paragraph("Opbouw van het dossier", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    rows = [["", "HOOFDSTUK", "WAT HET VASTSTELT"]]
    for ch in CHAPTERS:
        rows.append([ch["num"], ch["title"], ch["deck"].split(".")[0] + "."])
    story.append(data_table(rows, [width * 0.06, width * 0.34, width * 0.60], st))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Achterin: chronologie, claimregister (20) en bronnenregister (39).", st["caption"]))
    story.append(PageBreak())

    # Chronologie
    story.append(Paragraph("CHRONOLOGIE", st["chapter_num"]))
    story.append(Paragraph("Vijf jaar documentatie", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 6))
    rows = [["DATUM", "GEBEURTENIS", "BRON"]]
    for d, e, s in TIMELINE:
        rows.append([d, e, s])
    story.append(data_table(rows, [width * 0.13, width * 0.72, width * 0.15], st))
    story.append(PageBreak())


def back_matter(st, width, story):
    story.append(Paragraph("REGISTER I", st["chapter_num"]))
    story.append(Paragraph("Claimregister", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "Elke bewering van dit dossier staat hieronder met haar status en haar bronnen. "
            "Wie het oneens is, hoeft niet het geheel te bestrijden: het volstaat één regel te "
            "weerleggen. Dat is het doel van dit register.",
            st["body"],
        )
    )
    story.append(Spacer(1, 8))
    rows = [["CODE", "STATUS", "BEWERING", "BRONNEN"]]
    for code, status, claim, srcs, note in CLAIMS:
        rows.append([code, status, f"{claim}<br/><font size='6.6' color='#6e6965'>{note}</font>", srcs])
    story.append(data_table(rows, [width * 0.07, width * 0.17, width * 0.59, width * 0.17], st))
    story.append(PageBreak())

    story.append(Paragraph("REGISTER II", st["chapter_num"]))
    story.append(Paragraph("Bronnenregister", st["chapter_title"]))
    story.append(Rule(width, 0.8, WINE, 7))
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "Alle bronnen zijn openbaar en zonder betaalmuur of via een bibliotheek raadpleegbaar. "
            "Waar een bron van een marktpartij afkomstig is, staat dat vermeld; zulke bronnen "
            "worden uitsluitend gebruikt als bewijs van wat die partij zelf beweert.",
            st["body"],
        )
    )
    story.append(Spacer(1, 8))
    for code, kind, title, meta, url in SOURCES:
        story.append(
            Paragraph(
                f'<font name="MonoBold" size="6.4" color="#8b1e2d">{code}</font>  '
                f"<b>{title}</b> · {meta} · <font color='#6e6965'>{kind}</font> · "
                f"<font name='Mono' size='6.2' color='#6e6965'>{url}</font>",
                st["note"],
            )
        )
    story.append(Spacer(1, 14))
    story.append(Rule(width, 0.6, LINE, 6))
    story.append(
        Paragraph(
            "Einde van het dossier. Correcties met bronvermelding worden verwerkt in de "
            "online-editie en vermeld in de versiegeschiedenis.",
            st["caption"],
        )
    )


def build_integral():
    st = styles(9.4, 13.8)
    path = str(OUT / "de-marktplaats-van-de-ziel-editie-01.pdf")
    doc = Book(path, A4, "DE MARKTPLAATS VAN DE ZIEL · EDITIE 2.0", margins=(46, 46, 52, 44))
    width = doc.width
    story: list = []
    front_matter(st, width, story)

    part = None
    for ch in CHAPTERS:
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
        story.append(Spacer(1, 3))
        render_blocks(ch["blocks"], st, width, story)
        story.append(PageBreak())

    back_matter(st, width, story)
    doc.build(story)
    return path


WP_SECTIONS = [
    ("De vaststelling", [
        ("p", "Betaalde chatters schrijven namens creators zonder dat abonnees dat weten. Dit is "
              "geen aantijging maar een journalistieke vaststelling: Reuters documenteerde de "
              "praktijk bij toppagina’s [BR-01]; WIRED, GQ en SRF lieten hun journalisten zelf als "
              "chatter aannemen en publiceerden het trainingsmateriaal [BR-07] [BR-15] [BR-16]; "
              "de BBC sprak chatters over hun diensten en loon [BR-06]."),
        ("p", "De software die dit mogelijk maakt, wordt openlijk verkocht. Infloww groepeert fans "
              "op abonnementsduur en bestedingsvermogen [BR-23]; Supercreator adverteert met een AI "
              "die “in your voice” met fans chat en automatisch verkoopt [BR-24]; OnlyMonster scoort "
              "fans van nul tot vijf op bestedingspotentieel [BR-25]. Deze teksten zijn aan bureaus "
              "gericht, niet aan de betalende consument."),
        ("p", "De keten is financieel scheef: het platform houdt twintig procent, het bureau volgens "
              "de BBC gemiddeld de helft [BR-05] en in sommige Duitse contracten tot twee derde "
              "[BR-14]. Fenix International rapporteerde over 2024 7,22 miljard dollar aan "
              "fanbetalingen en 684 miljoen dollar winst voor belasting [BR-35]."),
    ]),
    ("Het juridische gat", [
        ("p", "Artikel 50 van de AI-verordening verplicht vanaf 2 augustus 2026 tot de mededeling dat "
              "een gebruiker met een AI-systeem interageert [BR-34]. Voor een mens die onder andermans "
              "naam schrijft, bestaat geen vergelijkbare meldplicht. Wat rest is artikel 7 van "
              "richtlijn 2005/29/EG — de misleidende omissie — die per geval moet worden getoetst [BR-31]."),
        ("p", "Dat die toetsing kan slagen, blijkt: het Landgericht Hamburg verbood in december 2025 "
              "betaalde chats met vermeende influencers wegens misleiding [BR-38]. In de Verenigde "
              "Staten lopen twee collectieve procedures tegen het platform en acht bureaus [BR-03] [BR-04]."),
        ("p", "Daarnaast raakt de praktijk aan artikel 9 AVG, dat de verwerking van gegevens over "
              "seksueel gedrag en gezondheid in beginsel verbiedt [BR-32], en aan artikel 26 lid 3 DSA, "
              "dat reclame op basis van zulke profilering verbiedt [BR-33]."),
    ]),
    ("Aanbevelingen", [
        ("ul", [
            "Verplicht vóór de eerste betaalde uitwisseling de mededeling wie berichten opstelt: de "
            "genoemde persoon, een gemachtigde derde, of een geautomatiseerd systeem.",
            "Maak een onjuist antwoord op de directe vraag “schrijf jij dit?” expliciet een misleidende "
            "handeling in de zin van artikel 6 UCPD.",
            "Verbied het gebruik van in intieme context prijsgegeven gegevens over gezondheid, rouw, "
            "verslaving of financiële nood voor segmentatie en verkoopsturing.",
            "Verklaar contractbedingen nietig die makers permanente toegang tot eigen account, "
            "inkomsten en publiek ontzeggen.",
            "Verplicht platformen tot registratie en geaggregeerde openbaarmaking van door derden "
            "beheerde accounts, zodat toezicht meetbaar wordt.",
        ]),
        ("box", "Wat dit voorstel niet doet",
         "Het verbiedt geen ondersteuning, geen ghostwriting en geen fictie. Het verplicht uitsluitend "
         "tot mededeling van auteurschap tegenover de partij die betaalt, en tot een waarheidsgetrouw "
         "antwoord op de directe vraag."),
    ]),
    ("Grenzen van dit stuk", [
        ("p", "Niet vastgesteld is welk aandeel van alle gesprekken via derden verloopt; er bestaat "
              "geen controleerbare meting en elk circulerend percentage mist bron. Evenmin "
              "onderbouwd zijn beweringen over micro-transacties als witwaskanaal en over "
              "demografische effecten; beide staan als onbevestigd in het claimregister van de "
              "integrale editie. Er is geen wederhoor gevraagd aan de genoemde partijen."),
    ]),
]


def build_whitepaper():
    st = styles(9.6, 14.2)
    path = str(OUT / "achter-het-profiel-whitepaper.pdf")
    doc = Book(path, A4, "WHITEPAPER · UITBESTEDE INTIMITEIT", margins=(52, 52, 52, 44))
    width = doc.width
    story: list = []
    story.append(Spacer(1, 60))
    story.append(Paragraph("WHITEPAPER VOOR TOEZICHTHOUDERS, JURISTEN EN REDACTIES", st["cover_sub"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Uitbestede intimiteit", st["cover_title"]))
    story.append(Spacer(1, 10))
    story.append(Rule(width, 1.1, WINE, 8))
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Samenvatting van het dossier De Marktplaats van de Ziel: wat is vastgesteld, welke "
            "norm ontbreekt, en welke vijf maatregelen dat gat dichten.",
            st["lead"],
        )
    )
    story.append(Spacer(1, 16))
    for title, blocks in WP_SECTIONS:
        story.append(mark(Paragraph(title, st["chapter_title"]), title))
        story.append(Rule(width, 0.8, WINE, 7))
        story.append(Spacer(1, 3))
        render_blocks(blocks, st, width, story)
        story.append(Spacer(1, 6))
    story.append(Rule(width, 0.6, LINE, 6))
    story.append(
        Paragraph(
            "Volledige onderbouwing, 39 bronnen en het claimregister staan in de integrale editie. "
            + VERSION,
            st["caption"],
        )
    )
    doc.build(story)
    return path


if __name__ == "__main__":
    register_fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    for p in (build_integral(), build_whitepaper()):
        print("geschreven:", p)
