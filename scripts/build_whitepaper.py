# -*- coding: utf-8 -*-
"""Bouwt uitsluitend de definitieve A4-pers-whitepaper."""
from pathlib import Path
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import PageBreak, Paragraph, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from typeset import OUT, WINE, LINE, Book, Rule, register_fonts, styles

SECTIONS = [
    ("De systeemanalyse", "Achter persoonlijk ogende profielen kan een professionele infrastructuur staan van operators, scripts, CRM-dossiers en automatisering. De centrale consumentenrechtelijke vraag is eenvoudig: weet de koper wie de betaalde berichten werkelijk opstelt?"),
    ("De juridische lacune", "De AI-verordening stelt transparantie-eisen aan geautomatiseerde interactie. Voor een mens die beroepsmatig onder andermans identiteit schrijft, bestaat geen even heldere algemene meldplicht. Consumentenrecht en gegevensbescherming bieden aanknopingspunten, maar vragen beoordeling per geval."),
    ("Lex Humanitas Digitalis", "Het modelvoorstel verplicht vóór de eerste betaalde uitwisseling tot een begrijpelijke mededeling: schrijft de genoemde persoon, een gemachtigde derde of een geautomatiseerd systeem? Het verbiedt geen ondersteuning of fictie; het maakt de prestatie kenbaar."),
    ("Zes onderzoeksvelden", "De Hexalogie behandelt achtereenvolgens technische deceptie, financiële schaduweconomie, neurobiologie van verslaving, sociologische effecten, juridisch kader en post-digitaal herstel. Feiten, hypothesen en voorstellen blijven in ieder deel zichtbaar gescheiden."),
]


def build_whitepaper():
    register_fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    path = str(OUT / "achter-het-profiel-whitepaper.pdf")
    st = styles(10.2, 15)
    doc = Book(path, A4, "WHITEPAPER · LEX HUMANITAS DIGITALIS", margins=(54, 54, 54, 46))
    width = doc.width
    story = [Spacer(1, 72), Paragraph("PERS-WHITEPAPER · 2026", st["cover_sub"]), Spacer(1, 14), Paragraph("Lex Humanitas Digitalis<br/>&amp; Systeemanalyse", st["cover_title"]), Spacer(1, 12), Rule(width, 1.1, WINE, 8), Spacer(1, 12), Paragraph("De kern van De Marktplaats van de Ziel voor pers, beleid en toezicht.", st["lead"]), Spacer(1, 190), Rule(width, 0.6, LINE, 6), Paragraph("Deel VII van het centrale publicatiearchief · A4 · openbare record-versie", st["caption"]), PageBreak()]
    for title, body in SECTIONS:
        story.extend([Paragraph(title, st["h2"]), Paragraph(body, st["body"]), Spacer(1, 12)])
    story.extend([Rule(width, 0.6, LINE, 6), Paragraph("De volledige onderbouwing staat in Boek I–VI en de openbare registers op de website.", st["caption"])])
    doc.build(story)
    return path


if __name__ == "__main__":
    print("geschreven:", build_whitepaper())
