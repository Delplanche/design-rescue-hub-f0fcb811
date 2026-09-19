# -*- coding: utf-8 -*-
"""De hexalogie: zes boeken in vierkant formaat (21 × 21 cm)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chapters import CHAPTERS as BASE  # noqa: E402

from . import book1, book2, book3, book4, book5, book6  # noqa: E402

_BY_NUM = {c["num"]: c for c in BASE}

# Boek VI sluit af met de bestaande hoofdstukken over grenzen en methodologie,
# gevolgd door het adresseringshoofdstuk.
BOOK6_CHAPTERS = book6.CHAPTERS[:5] + [_BY_NUM["10"], _BY_NUM["11"]] + book6.CHAPTERS[5:]


def _renumber(chapters):
    out = []
    for i, ch in enumerate(chapters, start=1):
        c = dict(ch)
        c["num"] = f"{i:02d}"
        out.append(c)
    return out


BOOKS = [
    {"roman": "I", "slug": "boek-i-de-technologische-deceptie",
     "title": "De technologische deceptie",
     "subtitle": "Chat-farms, ghost-chatting, CRM-dossiers en de automatisering van het intieme gesprek",
     "deck": "Wie typt er werkelijk, met welk gereedschap, en waarom weet de betalende lezer dat niet? "
             "Het eerste deel legt de feitelijke basis waarop de hele hexalogie rust.",
     "chapters": _renumber(book1.CHAPTERS)},
    {"roman": "II", "slug": "boek-ii-de-financiele-schaduweconomie",
     "title": "De financiële schaduweconomie",
     "subtitle": "Geldstromen tussen platform, bureau en creator; betaalverkeer, hoog risico en micro-transacties",
     "deck": "Volg één betaling van kaart tot ontvanger. Elke schakel houdt iets in, en de belangrijkste "
             "schakel staat in geen enkel document dat de koper ooit ziet.",
     "chapters": _renumber(book2.CHAPTERS)},
    {"roman": "III", "slug": "boek-iii-de-neurobiologie-van-de-afhankelijkheid",
     "title": "De neurobiologie van de verslaving",
     "subtitle": "Variable-reward, operator-psychologie en de arbeid van het meeleven",
     "deck": "Eén gedragspsychologisch principe verklaart waarom onvoorspelbaar betaald contact zo sterk "
             "bindt — en waar de uitleg ophoudt en de speculatie zou beginnen.",
     "chapters": _renumber(book3.CHAPTERS)},
    {"roman": "IV", "slug": "boek-iv-de-sociologische-implosie",
     "title": "De sociologische implosie",
     "subtitle": "Demografische verschuivingen en het Koreaans-Japanse scenario, strikt op geregistreerde data",
     "deck": "Het deel waarin overdrijving het meest voor de hand ligt, en daarom het strengst is "
             "afgebakend: statistiek als vaststelling, substitutie als expliciete hypothese.",
     "chapters": _renumber(book4.CHAPTERS)},
    {"roman": "V", "slug": "boek-v-het-juridisch-failliet",
     "title": "Het juridisch failliet & modelwetgeving",
     "subtitle": "AVG, DSA en AI-verordening, ketenaansprakelijkheid en Lex Humanitas Digitalis",
     "deck": "Het recht kent de misleidende omissie, maar geen meldplicht over wie schrijft. Dit deel toont "
             "wat al geldt, wat niet wordt gehandhaafd en hoe één korte regel het gat dicht.",
     "chapters": _renumber(book5.CHAPTERS)},
    {"roman": "VI", "slug": "boek-vi-het-post-digitale-verzet",
     "title": "Het post-digitale verzet",
     "subtitle": "Protocollen voor kopers, creators en chatters, en het post-digitale manifest",
     "deck": "Van analyse naar handeling: bewijs veiligstellen, contracten toetsen, rechten uitoefenen — "
             "en de vraag beantwoorden die deze markt bedient.",
     "chapters": _renumber(BOOK6_CHAPTERS)},
]
