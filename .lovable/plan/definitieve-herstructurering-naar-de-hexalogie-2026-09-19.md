# Definitieve herstructurering naar de Hexalogie

## Doel
De website wordt een rustige digitale bibliotheek met drie duidelijke lagen: een redactionele homepage, zes inhoudelijke onderzoekspijlers en één centrale bibliotheek. Alleen Boek I–VI en de pers-whitepaper blijven als download bestaan.

## 1. Eén officiële publicatiebron
- Lovable Cloud inschakelen en een publieke `publications`-collectie maken met precies zeven records, in vaste volgorde: de pers-whitepaper en Boek I–VI.
- Per record opslaan: officieel nummer/type, titel, korte beschrijving, feitelijke paginatelling, formaat, doelgroep, PDF-pad en publicatiestatus.
- De zeven bestaande definitieve PDF-bestanden koppelen; publieke bezoekers krijgen alleen leesrechten.
- De bibliotheek haalt deze zeven records uit Cloud. Beheer kan later via de Cloud-datatabel zonder codewijziging.

## 2. Eerlijke en consistente publicaties
- De zes vierkante boeken blijven de huidige lengte houden en worden met hun werkelijke paginatelling getoond: 26, 18, 15, 14, 17 en 18 pagina’s. Er wordt nergens meer “40–60 pagina’s” beweerd zolang dat niet werkelijk zo is.
- De pers-whitepaper wordt als A4-uitgave met de werkelijke 2 pagina’s vermeld.
- Titels, ondertitels en PDF-inhoud gelijkzetten met de officiële blauwdruk, waaronder “De Neurobiologie van de Verslaving” en “Het Juridisch Failliet & Modelwetgeving”.
- De zeven PDF’s opnieuw genereren na deze titel- en tekstcorrecties, zonder ze kunstmatig te verlengen.
- Alle pagina’s van alle zeven PDF’s als afbeeldingen controleren op afsnijding, overlap, foutieve fonts, lege pagina’s en verkeerde volgorde.

## 3. Oude publicaties volledig verwijderen
- De oude integrale editie, het oude dossier en de losse essay-reader uit de publieke map verwijderen.
- De verouderde drie-publicatiegegevens, directe downloadlinks en teksten als “Drie edities” verwijderen.
- De oude generator die opnieuw drie verouderde bestanden kan aanmaken verwijderen; alleen de Hexalogie- en whitepapergeneratie behouden.
- De roadmap bijwerken zodat die uitsluitend de zes boeken plus pers-whitepaper beschrijft.

## 4. Nieuwe sitestructuur
- **Homepage:** kernonderzoek prominent introduceren en uitsluitend doorverwijzen naar Onderzoek, Bibliotheek en het juridisch kader; geen directe PDF-download buiten de Bibliotheek.
- **Onderzoek:** de bestaande dossier- en essaystructuren vervangen door één overzicht van zes pijlers: Techniek/CRM, Financiën/Carding, Neurobiologie, Sociologie, Recht/Modelwetgeving en Post-Digitaal Herstel.
- Voor elke pijler een eigen inhoudelijke detailpagina maken, gevoed door de bestaande onderbouwde boekinhoud en zonder dubbele tekstblokken.
- **Bibliotheek:** de huidige archiefpagina omvormen tot de enige downloadplek, met exact zeven trapsgewijze items, volledige metadata en werkende downloadknoppen.
- Oude `/boek`- en onderliggende essaypagina’s verwijderen of gericht doorsturen naar de passende nieuwe onderzoekspagina; bestaande gedeelde registers voor claims, bronnen en methodologie behouden.

## 5. Menu en redactionele rust
- Hoofdmenu vereenvoudigen naar: Manifest, Onderzoek, Bibliotheek en Juridisch.
- Secundaire links naar claims, bronnen, methodologie en correcties in de voettekst behouden.
- Het bestaande antraciet/grafiet, pergament-wit en Instrument Serif-stramien handhaven; de nieuwe boeklijst krijgt een rustig redactioneel ritme zonder dubbele kaarten of knoppen.
- Mobiele en desktopweergave controleren op leesbaarheid, tekstoverlap en bruikbare navigatie.

## 6. VHEMT volledig uitsnijden
- De zichtbare VHEMT-sectie op de filosofiepagina verwijderen.
- Ook indirecte vermeldingen van vrijwillige uitsterving en toelichtingen dat dit kader “eerder verwijderd” is uit de boekbron schrappen; de term hoeft nergens meer te worden herhaald.
- Boek IV uitsluitend laten rusten op geregistreerde demografische cijfers, expliciet begrensde hypothesen en het Koreaans-Japanse vergelijkingskader.
- Na regeneratie de tekst van alle zeven PDF’s opnieuw doorzoeken om te bevestigen dat het label en equivalenten nergens voorkomen.

## 7. Eindcontrole
- Controleren dat de database exact zeven publicaties retourneert en de Bibliotheek exact zeven werkende downloads toont.
- Controleren dat geen bronbestand, pagina of knop nog naar de drie vervallen PDF’s verwijst.
- De centrale route van homepage → Onderzoek → Bibliotheek → download op mobiel en desktop doorlopen.
- Build-, browser- en foutlogcontrole uitvoeren en iedere inhoudspagina van unieke metadata voorzien.

## Technische notities
- De PDF-bestanden blijven als vaste publieke bestanden beschikbaar; Cloud beheert hun metadata en volgorde.
- De publieke tabel krijgt expliciete leesrechten en alleen een publieke SELECT-regel; er komt geen publieke schrijfroute.
- Oude openbare URL’s die nog betekenisvol verkeer kunnen hebben krijgen een gerichte doorverwijzing in plaats van een dode pagina.
