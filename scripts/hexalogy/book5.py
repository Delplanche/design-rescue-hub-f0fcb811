# -*- coding: utf-8 -*-
"""Boek V — Het juridisch failliet & Lex Humanitas Digitalis."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chapters import CHAPTERS as BASE  # noqa: E402

_BY_NUM = {c["num"]: c for c in BASE}

EXTRA = [

{"num": "A1", "part": "DEEL II — DE BESTAANDE INSTRUMENTEN",
 "title": "De AVG: intimiteit als bijzondere categorie",
 "deck": "Voor gespreksdossiers over rouw, relaties en gezondheid bestaat al een strikt regime. Het probleem is niet het ontbreken van de regel, maar het ontbreken van toepassing.",
 "blocks": [
  ("p", "Gegevens over iemands seksuele leven of gezondheid vallen onder artikel 9 AVG: verwerking is in beginsel verboden, behoudens een beperkt aantal uitzonderingen waaronder uitdrukkelijke toestemming. [BR-32] Gespreksnotities waarin staat dat een abonnee net gescheiden is, met rouw kampt of medicatie gebruikt, raken deze categorie rechtstreeks."),
  ("p", "Boek I heeft vastgesteld dat zulke notitievelden bestaan, dat zij door de CRM-leveranciers als functie worden aangeboden en dat undercoververslagen het gebruik ervan beschrijven. [CL-09] Daarmee is de juridische vraag niet of het regime geldt, maar wie verwerkingsverantwoordelijke is: het platform, het bureau, of de creator op wiens naam het account staat."),
  ("box", "Definitie",
   "Verwerkingsverantwoordelijke: degene die doel en middelen van de verwerking bepaalt. Wie de segmentatievelden inricht, de scripts voorschrijft en de dossiers gebruikt om de verkoopstrategie te sturen, bepaalt doel en middelen — ongeacht wiens naam op het account staat."),
  ("h2", "Drie verplichtingen die nu al gelden"),
  ("ul", ["Informatieplicht (art. 13–14): de betrokkene moet weten wie zijn gegevens verwerkt en waarvoor. In deze keten weet hij niet eens dat het bureau bestaat.",
          "Inzagerecht (art. 15): de betrokkene heeft recht op een kopie van zijn gegevens, inclusief classificaties en ontvangers.",
          "Geautomatiseerde besluitvorming (art. 22): waar segmentatie en scoring bepalen welke prijs of welk aanbod iemand krijgt, komt dit artikel in beeld."]),
  ("p", "Geen van die drie vergt nieuwe wetgeving. Wat ontbreekt is een toezichtsonderzoek dat de keten in kaart brengt en de verantwoordelijke aanwijst. Boek VI adresseert dat verzoek expliciet aan de gegevensbeschermingsautoriteiten."),
 ]},

{"num": "A2", "part": "DEEL II — DE BESTAANDE INSTRUMENTEN",
 "title": "DSA, ketenaansprakelijkheid en de positie van het platform",
 "deck": "Het platform stelt dat de creator verantwoordelijk is. De risicoverplichtingen van de digitaledienstenverordening laten die positie niet onaangetast.",
 "blocks": [
  ("p", "De digitaledienstenverordening verplicht zeer grote platformen tot het inschatten en beperken van systeemrisico’s die uit het ontwerp van hun dienst voortvloeien. [BR-33] Een dienst die betaald persoonlijk contact als kernproduct verkoopt, en waarvan bekend is dat dat contact grootschalig door derden wordt gevoerd, heeft daarmee een te beoordelen risico."),
  ("p", "Het platform verwijst in geschillen naar zijn voorwaarden, die de creator verantwoordelijk maken voor wat onder haar account gebeurt. Twee Amerikaanse class actions en een Duits verbod betwisten die toerekening. [BR-03] [BR-04] [BR-38] De status van die stelling is in dit dossier geregistreerd als betwist. [CL-13]"),
  ("box", "Feit, interpretatie, voorstel",
   "Feit: het platform hanteert voorwaarden die de creator verantwoordelijk maken; rechters buigen zich over de houdbaarheid daarvan. Interpretatie: wie de infrastructuur levert, de betalingen verwerkt en twintig procent inhoudt, staat niet buiten de keten. Voorstel: ketenaansprakelijkheid voor niet-gemelde identiteitsvervanging, zoals uitgewerkt in het modelvoorstel."),
  ("h2", "Het Hamburgse verbod als precedent"),
  ("p", "Het Landgericht Hamburg verbood in december 2025 betaalde chats met ‘vermeende influencers’ wegens misleiding. [BR-38] Het belang van die uitspraak ligt niet in het bedrag maar in de kwalificatie: de rechter behandelde het niet-melden van wie schrijft als een misleidende handelspraktijk, en niet als een kwestie van smaak of van contractvrijheid."),
  ("p", "Daarmee bestaat er binnen de EU een eerste rechterlijke bevestiging dat het bestaande consumentenrecht op deze praktijk toepasbaar is. [CL-07] Dat verzwakt het argument dat handhaving op nieuwe wetgeving zou moeten wachten."),
 ]},

{"num": "A3", "part": "DEEL III — HANDHAVING",
 "title": "Waarom handhaving uitblijft",
 "deck": "De regels bestaan, de bevoegdheden bestaan, de zaken zijn gepubliceerd. Toch gebeurt er weinig. Dit hoofdstuk benoemt de vier oorzaken.",
 "blocks": [
  ("h3", "Oorzaak 1 — Het klachtentekort"),
  ("p", "Toezicht op consumentenrecht draait op meldingen. In deze markt is melden voor de gedupeerde persoonlijk beschamend; het aantal meldingen is daardoor structureel geen afspiegeling van de omvang. Boek II beschreef dit mechanisme in de context van terugboekingen."),
  ("h3", "Oorzaak 2 — De grensoverschrijdende keten"),
  ("p", "Platform, bureau, chatters en betaaldienstverlener bevinden zich vaak in verschillende rechtsgebieden. Elke autoriteit ziet een fragment en geen enkele het geheel. Dat is geen juridisch obstakel maar een coördinatieprobleem, en het is oplosbaar met bestaande samenwerkingsverbanden."),
  ("h3", "Oorzaak 3 — De onderwerpdrempel"),
  ("p", "Het onderwerp raakt seksualiteit, en dat verhoogt de politieke kosten van optreden. Het gevolg is dat een consumentenrechtelijk vraagstuk — wie schrijft, en mag dat verzwegen worden — wordt behandeld als een zedelijke kwestie waarover men liever zwijgt."),
  ("h3", "Oorzaak 4 — De bewijslast bij het individu"),
  ("p", "De koper moet aantonen wat hem is voorgesteld, terwijl de bewijsstukken op een platform staan waartoe hij na opzegging geen toegang meer heeft. Een omkering van de bewijslast op het punt van de mededeling zou dit in één keer verplaatsen naar de partij die de administratie voert."),
  ("box", "Bewijsgrens",
   "Deze vier oorzaken zijn een analyse van de auteur, gebaseerd op de in dit dossier verzamelde zaken en bronnen. Zij zijn niet ontleend aan een evaluatie van een toezichthouder; er is geen onderzoek dat de relatieve zwaarte ervan meet."),
 ]},
]

CHAPTERS = [_BY_NUM["07"], _BY_NUM["08"]] + EXTRA[:2] + [_BY_NUM["09"]] + EXTRA[2:]
