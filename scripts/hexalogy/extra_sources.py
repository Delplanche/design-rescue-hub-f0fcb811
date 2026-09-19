# -*- coding: utf-8 -*-
"""Aanvullende bronnen en claims voor de hexalogie.

De nummering sluit aan op scripts/sources.py (BR-01 t/m BR-39, CL-01 t/m CL-20).
Alles hieronder is openbaar en primair: statistiekbureaus, wetteksten en
toezichtsdocumentatie. Waar een cijfer een voorlopig karakter heeft, staat dat
in de meta-regel.
"""

EXTRA_SOURCES = [
    ("BR-40", "Statistiek", "Statistics Korea (KOSTAT) — Birth Statistics, jaarcijfers",
     "totaal vruchtbaarheidscijfer 0,72 (2023) en 0,75 (2024); dieptepunt van alle OESO-landen",
     "kostat.go.kr/ansk/"),
    ("BR-41", "Statistiek", "Japans Ministerie van Volksgezondheid, Arbeid en Welzijn — Vital Statistics",
     "geboorten van Japanse staatsburgers onder de 700.000 in 2024, voor het eerst sinds de meting begon",
     "mhlw.go.jp/english/database/db-hw/"),
    ("BR-42", "Statistiek", "Eurostat — Fertility indicators (demo_find)",
     "totaal vruchtbaarheidscijfer EU-27 rond 1,38 in 2023: laagste waarde sinds de reeks bestaat",
     "ec.europa.eu/eurostat/databrowser/view/demo_find"),
    ("BR-43", "Statistiek", "OESO — Society at a Glance / Family Database, indicatoren over "
     "partnervorming, alleenwonenden en sociale contacten",
     "meerjarige reeksen per land", "oecd.org/social/family/database.htm"),
    ("BR-44", "Toezichtsdocumentatie", "Europese Bankautoriteit — richtsnoeren en opinies over "
     "witwasrisico bij e-geld, kaartacquiring en handelaren met hoog risico",
     "geconsolideerde richtsnoerenreeks", "eba.europa.eu/regulation-and-policy/anti-money-laundering"),
    ("BR-45", "Wetgeving", "Richtlijn (EU) 2015/2366 (PSD2), art. 64–74 over autorisatie, "
     "niet-toegestane transacties en terugbetaling",
     "geconsolideerde tekst", "eur-lex.europa.eu/eli/dir/2015/2366/oj"),
    ("BR-46", "Wetgeving", "Richtlijn 93/13/EEG oneerlijke bedingen in consumentenovereenkomsten",
     "geconsolideerde tekst", "eur-lex.europa.eu/eli/dir/1993/13/oj"),
    ("BR-47", "Wetenschappelijk", "Skinner e.a. — onderzoekstraditie rond intermitterende "
     "variabele bekrachtiging (variable-ratio reinforcement) in gedragspsychologie",
     "standaardliteratuur, samengevat in hedendaagse leerboeken gedragsanalyse", "—"),
    ("BR-48", "Wetenschappelijk", "Wereldgezondheidsorganisatie — ICD-11, gokstoornis (6C50) en "
     "gaming-stoornis (6C51) als erkende gedragsverslavingen",
     "ICD-11, versie 2024", "icd.who.int/browse11"),
]

EXTRA_CLAIMS = [
    ("CL-21", "VASTGESTELD",
     "Zuid-Korea en Japan tonen de laagste geregistreerde geboortecijfers ter wereld.",
     "BR-40, BR-41",
     "Koreaans vruchtbaarheidscijfer 0,72 (2023) en 0,75 (2024); Japanse geboorten onder 700.000 in 2024."),
    ("CL-22", "VASTGESTELD",
     "Het vruchtbaarheidscijfer van de EU-27 staat op het laagste niveau sinds de meting.",
     "BR-42",
     "Eurostat: circa 1,38 in 2023. Een vaststelling over de reeks, niet over de oorzaak."),
    ("CL-23", "HYPOTHESE",
     "Betaald digitaal contact verdringt in bepaalde groepen onbetaald offline contact.",
     "BR-43, BR-26",
     "Substitutie is plausibel en deels meetbaar in tijdsbestedingsonderzoek, maar er bestaat geen "
     "studie die het effect isoleert voor deze bedrijfstak. Uitdrukkelijk geen feitelijke vaststelling."),
    ("CL-24", "VASTGESTELD",
     "Variabele, onvoorspelbare beloning houdt gedrag langer in stand dan vaste beloning.",
     "BR-47, BR-48",
     "Standaardbevinding uit de gedragspsychologie; de WHO erkent gedragsverslavingen met dit patroon."),
    ("CL-25", "ONBEVESTIGD",
     "Chatgesprekken in deze sector worden doelbewust volgens verslavingsmodellen ontworpen.",
     "BR-07, BR-16, BR-24",
     "Trainingsmateriaal en software sturen aantoonbaar op timing en uitgestelde beloning. Dat een "
     "expliciet verslavingsmodel wordt toegepast, is niet aangetoond."),
    ("CL-26", "VASTGESTELD",
     "Betaaldienstverleners kennen een aparte categorie handelaren met hoog risico, met hogere "
     "tarieven, reserves en toezichtsverplichtingen.",
     "BR-44, BR-45",
     "Toezichtsdocumentatie en PSD2. Zegt niets over de intenties van individuele partijen in deze sector."),
    ("CL-27", "ONBEVESTIGD",
     "Deze sector functioneert op schaal als afzetkanaal voor gestolen kaartgegevens.",
     "—",
     "In dit dossier ontbreekt elke opsporings-, toezichts- of rechtbankbron. Blijft een onderzoeksvraag; "
     "in Boek II staat waar de bewijslast ligt en welk onderzoek haar zou kunnen beantwoorden."),
    ("CL-28", "VASTGESTELD",
     "Contractbedingen die een consument of maker de toegang tot eigen account, inkomsten en "
     "gegevens ontzeggen, zijn toetsbaar aan het Europese recht inzake oneerlijke bedingen.",
     "BR-46, BR-32",
     "Richtlijn 93/13/EEG en de AVG bieden bestaande, niet-hypothetische toetsingsgronden."),
]
