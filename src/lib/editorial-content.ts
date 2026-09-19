export type EditorialSection = {
  heading: string;
  body: string;
};

export type EssayChapter = {
  slug: string;
  nr: string;
  title: string;
  deck: string;
  sections: readonly EditorialSection[];
};

export const bookChapters: readonly EssayChapter[] = [
  {
    slug: "de-gecommercialiseerde-begroeting",
    nr: "01",
    title: "De gecommercialiseerde begroeting",
    deck: "Een essay over wat er verandert wanneer aandacht wordt gemeten, geprijsd en geoptimaliseerd.",
    sections: [
      { heading: "Voor het gesprek begint", body: "Een begroeting lijkt klein, maar draagt een belofte: iemand ziet iemand anders. Wanneer die opening deel wordt van een verkooptrechter, blijft de taal persoonlijk terwijl de context commercieel is geworden." },
      { heading: "Warmte en meetbaarheid", body: "Digitale systemen kunnen nabijheid organiseren en toegankelijk maken. Tegelijk kunnen meetpunten, scripts en omzetdoelen de betekenis van een gesprek verschuiven. Dit hoofdstuk leest die spanning als een filosofische vraag, niet als een bewezen eigenschap van ieder platform." },
      { heading: "De grens van het essay", body: "De observaties hier zijn auteursduiding. Waar feitelijke uitspraken nodig zijn, verwijst het boek naar het afzonderlijke onderzoeksdossier en zijn bronnenregister." },
      { heading: "Een dubbel register", body: "Wie persoonlijke taal commercieel organiseert, schrijft tegelijk in twee registers: dat van de ontmoeting en dat van de transactie. De woorden blijven warm, maar achter ieder woord kan een meetpunt staan. Het ongemak begint waar het ene register zich als het andere voordoet." },
    ],
  },
  {
    slug: "de-metriek-van-nabijheid",
    nr: "02",
    title: "De metriek van nabijheid",
    deck: "Over de taal van retentie, segmentatie en waarde in een domein dat zich als persoonlijk presenteert.",
    sections: [
      { heading: "Een taal van optimalisatie", body: "Een metriek beschrijft niet alleen; zij bepaalt ook waarop een organisatie let. Wanneer aandacht in conversie, retentie en besteding wordt vertaald, dreigt relationele taal een instrumentele functie te krijgen." },
      { heading: "Geen eenvoudige tegenstelling", body: "Betaalde intimiteit is niet per definitie onecht, evenmin is onbetaalde aandacht automatisch zuiver. De relevante spanning ligt tussen uitgesproken verwachtingen en de feitelijke organisatie achter een ontmoeting." },
      { heading: "Wat de meter niet ziet", body: "Een metriek kan duur, terugkeer en besteding zien, maar niet wat een stilte betekent. Zodra alleen meetbaar gedrag bestuurbaar wordt, dreigt de onmeetbare betekenis van terughoudendheid, twijfel en grensstelling uit beeld te verdwijnen." },
    ],
  },
  {
    slug: "de-geleende-stem", nr: "03", title: "De geleende stem", deck: "Wanneer een herkenbare toon kan worden doorgegeven, gescript en op schaal gereproduceerd.",
    sections: [
      { heading: "Stem zonder lichaam", body: "Schrift laat aanwezigheid altijd al reizen. De digitale infrastructuur voegt daar een nieuwe mogelijkheid aan toe: een stem kan operationeel worden verdeeld zonder haar herkenbare naam te verliezen. De vraag is niet of bemiddeling verboden is, maar wanneer zij bekend moet zijn." },
      { heading: "Continuïteit als product", body: "Een team kan dag en nacht dezelfde warmte leveren. Daarmee wordt continuïteit niet langer een gevolg van betrokkenheid, maar een dienstniveau. De lezer ontmoet een consistent personage, terwijl de arbeid erachter wisselt." },
      { heading: "De ethiek van bekendmaking", body: "Transparantie hoeft de verbeelding niet te vernietigen. Theater verliest zijn kracht niet doordat we acteurs kennen. Een eerlijke aanduiding kan juist ruimte scheppen voor instemming met de vorm van het contact." },
    ],
  },
  {
    slug: "het-geheugen-dat-verkoopt", nr: "04", title: "Het geheugen dat verkoopt", deck: "Over notities, herkenning en de overgang van herinnering naar commerciële infrastructuur.",
    sections: [
      { heading: "Herinnerd worden", body: "Herkenning is een van de kleinste vormen van intimiteit. Iemand weet nog wat je zei. In een CRM wordt dat geheugen duurzaam, overdraagbaar en doorzoekbaar — eigenschappen die zorg kunnen ondersteunen, maar ook verkoop kunnen verfijnen." },
      { heading: "Een archief zonder wederkerigheid", body: "De gebruiker onthult, het systeem onthoudt. Die asymmetrie groeit wanneer het archief aan de ene kant volledig is en aan de andere kant onzichtbaar blijft. Dan is herinnering geen gedeeld verleden meer, maar een operationeel voordeel." },
      { heading: "Recht op vergetelheid", body: "Vergeten is niet alleen verlies. Het is ook een menselijke grens: de mogelijkheid om niet voor altijd door een eerdere uiting te worden bepaald. Een humane infrastructuur behandelt wissen daarom niet als storing, maar als voorwaarde voor vrijheid." },
    ],
  },
  {
    slug: "de-prijs-van-beschikbaarheid", nr: "05", title: "De prijs van beschikbaarheid", deck: "Een essay over permanente bereikbaarheid, arbeid en de verwachting dat aandacht nooit sluit.",
    sections: [
      { heading: "Altijd open", body: "De digitale etalage kent geen avond. Permanente beschikbaarheid lijkt nabijheid, maar vraagt achter de schermen om roosters, overdracht en herhaling. Wat voor de één spontaniteit heet, kan voor de ander ploegendienst zijn." },
      { heading: "De arbeid in de warmte", body: "Affectieve arbeid is niet minder werkelijk omdat zij met taal en stemming werkt. Juist waar arbeid onzichtbaar blijft, wordt het moeilijk om verantwoordelijkheid, grenzen en een eerlijke verdeling van opbrengst te bespreken." },
      { heading: "Het recht om afwezig te zijn", body: "Een menselijke relatie verdraagt onderbreking. De machine leest afwezigheid als gemiste conversie. Ontkoppeling begint daarom bij het herstel van een eenvoudig recht: niet iedere stilte hoeft onmiddellijk te worden gerepareerd." },
    ],
  },
  {
    slug: "de-architectuur-van-verlangen", nr: "06", title: "De architectuur van verlangen", deck: "Hoe routes, signalen en frictie bepalen wat in een digitale ruimte waarschijnlijk wordt.",
    sections: [
      { heading: "Geen neutrale kamer", body: "Een interface is een gebouw van keuzes. Knoppen zijn deuren, meldingen zijn bellen en betaalmuren zijn poorten. Het ontwerp dwingt niet volledig, maar maakt sommige bewegingen eenvoudiger en andere bijna onzichtbaar." },
      { heading: "Frictie als bescherming", body: "Snelheid wordt vaak als dienst gezien. Toch kan een korte vertraging vóór een terugkerende betaling, een duidelijke identiteit bij een gesprek of een zichtbaar gegevensoverzicht een vorm van bescherming zijn." },
      { heading: "Ontwerpen voor tegenspraak", body: "Een eerlijke ruimte laat de gebruiker niet alleen instemmen, maar ook aarzelen, terugkeren en weigeren. Zij maakt de uitgang even zichtbaar als de ingang en behandelt keuzevrijheid niet als verlies van omzet." },
    ],
  },
  {
    slug: "ruimte-zonder-meter",
    nr: "07",
    title: "Ruimte zonder meter",
    deck: "Een slotessay over wederkerigheid, begrenzing en vormen van aandacht die niet onmiddellijk worden afgerekend.",
    sections: [
      { heading: "Niet alles hoeft product te worden", body: "Ontkoppeling begint niet bij een verbod, maar bij het terugvinden van onderscheid: tussen contact en consumptie, tussen verlangen en verkoop, tussen beschikbare aandacht en wederkerigheid." },
      { heading: "Een open einde", body: "Deze uitgave stelt geen universeel herstelprogramma voor. Zij nodigt uit tot traagheid, transparantie en publieke regels die mensen opnieuw ruimte geven om geïnformeerd te kiezen." },
      { heading: "Post-digitaal manifest", body: "Wij keren niet terug naar een wereld zonder techniek. Wij eisen een wereld waarin techniek haar tussenkomst toont; waarin een mens niet tot profiel, gesprek niet tot trechter en herinnering niet tot verkoopargument wordt gereduceerd. Niet alles wat meetbaar is verdient een meter. Niet alles wat waarde heeft behoeft een prijs." },
    ],
  },
] as const;

export const legalPillars = [
  ["01", "Identiteitstransparantie", "Maak begrijpelijk bekend of een gesprek door de geprofileerde persoon, een gemachtigde medewerker of automatisering wordt gevoerd."],
  ["02", "Dataminimalisatie", "Beperk intieme klantnotities tot aantoonbaar noodzakelijke gegevens, met heldere bewaartermijnen en inzagerechten."],
  ["03", "Contractuele uitgang", "Borg toegang tot eigen accounts, data en inkomsten bij het beëindigen van een samenwerking."],
  ["04", "Controleerbaar toezicht", "Maak onafhankelijke audits en een toegankelijke klachtenroute mogelijk zonder schuld vooraf vast te stellen."],
] as const;

export const legalTests = [
  ["Noodzaak", "Toon welk concreet probleem niet voldoende door bestaande regels wordt opgelost."],
  ["Proportionaliteit", "Beperk de maatregel tot wat nodig is en bescherm vrije expressie, arbeid en ondernemerschap."],
  ["Controleerbaarheid", "Maak labels, audits en klachtenroutes toetsbaar in plaats van louter symbolisch."],
  ["Herstel", "Bied een werkbare route voor inzage, correctie, beëindiging en overdracht van gegevens."],
] as const;

export const archivePublications = [
  { kind: "VOLLEDIGE EDITIE", title: "De Marktplaats van de Ziel", description: "Elf hoofdstukken dichte analyse met letterlijke citaten uit undercoveronderzoek, productpagina’s en rechtbankstukken, gevolgd door chronologie, claimregister (20) en bronnenregister (39).", format: "A4", audience: "Onderzoek · juristen · pers", pages: "29 pagina’s", size: "196 kB", href: "/publicaties/de-marktplaats-van-de-ziel-editie-01.pdf" },
  { kind: "EXECUTIVE WHITEPAPER", title: "Uitbestede intimiteit", description: "De vaststellingen, het juridische gat tussen art. 50 AI-verordening en art. 7 UCPD, en vijf concrete maatregelen — met bronverwijzingen.", format: "A4", audience: "Pers · beleid · toezicht", pages: "2 pagina’s", size: "98 kB", href: "/publicaties/achter-het-profiel-whitepaper.pdf" },
  { kind: "BOEK-READER", title: "De Commodificatie van de Ziel", description: "De zelfstandige literaire en filosofische leeseditie, afgesloten met het post-digitale manifest.", format: "21 × 21 cm", audience: "Essay · filosofie", pages: "18 pagina’s", size: "1,3 MB", href: "/publicaties/de-commodificatie-van-de-ziel.pdf" },
] as const;

export const archiveVersions = [
  { date: "19 september 2026", version: "Editie 02", note: "Volledige herschrijving: dichte hoofdstukken met verbatim citaten en primaire bronnen; vier te stellige beweringen ingetrokken of gedegradeerd tot onbevestigd." },
  { date: "19 september 2026", version: "Editie 01", note: "Eerste controleerbare onderzoeksuitgave met claim- en bronnenregister." },
] as const;