# -*- coding: utf-8 -*-
"""Boek I — De technologische deceptie.

Kern: de zes reeds gedocumenteerde hoofdstukken over markt, chatters, bureau,
software, CRM en script, aangevuld met een afsluitende vaststellingenbalans.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chapters import CHAPTERS as BASE  # noqa: E402

_BY_NUM = {c["num"]: c for c in BASE}

EXTRA = [
{"num": "07", "part": "DEEL III — DE BALANS",
 "title": "De deceptie in één overzicht",
 "deck": "Zes hoofdstukken leverden een reeks vaststellingen op. Dit slothoofdstuk zet ze op een rij, met hun status en hun bron, zodat de rest van de hexalogie erop kan bouwen.",
 "blocks": [
  ("p", "De vaststellingen hieronder zijn de harde kern van dit dossier. Ze zijn afkomstig uit journalistiek onderzoek van benoemde redacties, uit publieke productdocumentatie en uit gedeponeerde jaarrekeningen. Geen van deze punten berust op anonieme bronnen die dit dossier zelf heeft gesproken."),
  ("table", [["Nr.", "Vaststelling", "Status"],
             ["CL-01", "Betaalde chatters schrijven namens creators, zonder mededeling", "Vastgesteld"],
             ["CL-02", "Software biedt segmentatie, massabericht en AI-antwoorden", "Vastgesteld"],
             ["CL-03", "Het werk is uitbesteed aan laagbetaalde arbeid buiten EU/VS", "Vastgesteld"],
             ["CL-04", "Bureaus nemen de helft tot twee derde van de opbrengst", "Vastgesteld"],
             ["CL-05", "Creators verliezen in bepaalde contracten de controle over hun account", "Vastgesteld"],
             ["CL-08", "AI genereert of suggereert als persoonlijk gepresenteerde antwoorden", "Vastgesteld"],
             ["CL-09", "Intieme gegevens van abonnees worden in gedeelde dossiers vastgelegd", "Gedocumenteerd"],
             ["CL-10", "Scripts sturen op emotionele binding vóór verkoop", "Gedocumenteerd"],
             ["CL-14", "Systematische classificatie op psychische kwetsbaarheid", "Onbevestigd"]],
   [12, 63, 25]),
  ("h2", "Wat de deceptie precies is"),
  ("p", "Het woord deceptie wordt in dit boek nauw gebruikt. Het gaat niet om bewerkte foto’s, niet om een artiestennaam en niet om het feit dat een commercieel motief bestaat. Het gaat om één ding: de koper krijgt de indruk dat hij met een specifieke persoon schrijft, en die indruk wordt beroepsmatig in stand gehouden terwijl iemand anders typt. Alle overige verwijten in dit dossier zijn afgeleid van die ene asymmetrie."),
  ("box", "Bewijsgrens van Boek I",
   "Wat vaststaat is dat de praktijk bestaat, hoe zij is georganiseerd en welk gereedschap ervoor wordt verkocht. Wat niet vaststaat is welk aandeel van alle gesprekken zo verloopt. Die meting vereist medewerking van de platformen en is nooit gepubliceerd. Boek I doet er geen uitspraak over."),
  ("p", "Boek II volgt het geld dat door deze structuur beweegt. Boek III onderzoekt waarom de gespreksvorm zo sterk bindt. Boek IV plaatst het geheel in de demografische context, met uitdrukkelijke terughoudendheid. Boek V behandelt het recht. Boek VI levert de protocollen."),
 ]},
]

CHAPTERS = [_BY_NUM[n] for n in ("01", "02", "03", "04", "05", "06")] + EXTRA
