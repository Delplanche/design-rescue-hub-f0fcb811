export type ResearchSection = { heading: string; body: string };
export type ResearchPillar = {
  slug: string;
  number: string;
  book: string;
  title: string;
  shortTitle: string;
  deck: string;
  evidence: string;
  sections: readonly ResearchSection[];
};

export const researchPillars: readonly ResearchPillar[] = [
  { slug: "technologische-deceptie", number: "01", book: "Boek I", title: "De Technologische Deceptie", shortTitle: "Techniek & CRM", deck: "Hoe chat-farms, ghost-chatting, CRM-dossiers en automatisering persoonlijk contact op industriële schaal produceren.", evidence: "Gedocumenteerde infrastructuur, productpagina’s en journalistiek undercoveronderzoek.", sections: [
    { heading: "De persoon aan de andere kant", body: "Een profiel kan één herkenbare identiteit tonen terwijl berichten door meerdere operators, scripts of systemen worden opgesteld. De kernvraag is niet of ondersteuning bestaat, maar of de betalende gebruiker begrijpt met wie hij communiceert." },
    { heading: "CRM als overdraagbaar geheugen", body: "Gespreksnotities, bestedingssegmenten en voorkeuren maken persoonlijke continuïteit overdraagbaar tussen diensten. Daardoor kan herkenning authentiek aanvoelen terwijl zij operationeel uit een dossier wordt gereconstrueerd." },
    { heading: "Bewijsgrens", body: "Het onderzoek documenteert aangeboden softwarefuncties en concrete werkwijzen. Het trekt daaruit geen representatieve conclusie over ieder account of ieder platform." },
  ]},
  { slug: "financiele-schaduweconomie", number: "02", book: "Boek II", title: "De Financiële Schaduweconomie", shortTitle: "Financiën & Carding", deck: "De geldstroom achter microtransacties, carding-risico’s en de verdeling tussen platform, bureau, operator en creator.", evidence: "Jaarrekeningen, contractmateriaal, betaalstructuren en afgebakende risicoanalyse.", sections: [
    { heading: "Volg de betaling", body: "Een betaling passeert platformkosten, bureauvergoedingen, betaalverwerkers en uitbetalingsvoorwaarden voordat zij de geprofileerde maker bereikt. Die keten is voor de koper grotendeels onzichtbaar." },
    { heading: "Carding en witwasrisico", body: "Kleine, herhaalde transacties en digitale diensten kunnen aantrekkelijk zijn voor misbruik van betaalmiddelen. Waar concrete omvangsdata ontbreken, behandelt het onderzoek dit uitsluitend als toezichtsvraag en niet als vastgestelde sectorschaal." },
    { heading: "Economische asymmetrie", body: "De partij die aandacht koopt ziet een persoon; de financiële werkelijkheid bestaat uit meerdere contractuele schakels. Transparantie over die keten bepaalt wie aanspreekbaar is bij misleiding of schade." },
  ]},
  { slug: "neurobiologie-verslaving", number: "03", book: "Boek III", title: "De Neurobiologie van de Verslaving", shortTitle: "Neurobiologie", deck: "Variable-reward, gedragsmatige binding en de psychologische belasting van gebruiker én operator.", evidence: "Gedragswetenschappelijke mechanismen, met klinische claims strikt begrensd.", sections: [
    { heading: "Onvoorspelbare beloning", body: "Variabele timing en onvoorspelbare respons kunnen herhaald controleren en betalen versterken. Het mechanisme is bekend uit gedragswetenschap, maar stelt zonder individueel onderzoek geen diagnose vast." },
    { heading: "Operator-psychologie", body: "Operators verrichten affectieve arbeid: zij herkennen kwetsbaarheid, bewaken continuïteit en sturen gesprekken richting omzet. Die rol kan empathische belasting en morele spanning veroorzaken." },
    { heading: "Van mechanisme naar bescherming", body: "Heldere identiteit, bestedingsinformatie en uitstapmomenten verminderen informatie-asymmetrie zonder volwassen gebruikers hun keuzevrijheid te ontnemen." },
  ]},
  { slug: "sociologische-implosie", number: "04", book: "Boek IV", title: "De Sociologische Implosie", shortTitle: "Sociologie", deck: "Demografische data en digitale substitutie, met Korea en Japan als zorgvuldig begrensd vergelijkingskader.", evidence: "Geregistreerde statistiek; substitutie blijft een expliciet toetsbare hypothese.", sections: [
    { heading: "De cijfers vóór het verhaal", body: "Zuid-Korea, Japan en Europa tonen langdurige verschuivingen in vruchtbaarheid, huishoudens en partnervorming. Die reeksen zijn vaststellingen; zij vormen op zichzelf geen verklaring voor oorzaken." },
    { heading: "Het Koreaans-Japanse scenario", body: "Korea en Japan zijn geen voorspelling voor Europa, maar een meetlat voor samenlevingen waar uitgesteld partnerschap, hoge woonlasten, lange werktijden en eenpersoonshuishoudens sterk samenkomen." },
    { heading: "Substitutie als onderzoeksvraag", body: "Of betaald digitaal contact offline contact aanvult of verdringt, kan alleen met longitudinale gegevens over tijd, uitgaven en relaties worden getoetst. Die gegevens zijn nu niet publiek beschikbaar." },
  ]},
  { slug: "juridisch-failliet-modelwetgeving", number: "05", book: "Boek V", title: "Het Juridisch Failliet & Modelwetgeving", shortTitle: "Recht & Modelwetgeving", deck: "Van bestaande Europese regels naar Lex Humanitas Digitalis: een concrete meldplicht voor uitbesteed en geautomatiseerd contact.", evidence: "Wettekst, rechtspraak en een uitdrukkelijk als voorstel gemarkeerd model.", sections: [
    { heading: "Het bestaande gat", body: "Consumentenrecht kan misleidende omissies aanpakken en de AI-verordening kent transparantieregels voor systemen. Een even duidelijke algemene meldplicht voor menselijke identiteitsvervanging ontbreekt." },
    { heading: "Lex Humanitas Digitalis", body: "Het modelvoorstel verplicht vóór betaalde uitwisseling tot begrijpelijke mededeling of de genoemde persoon, een gemachtigde derde of automatisering schrijft." },
    { heading: "Proportioneel toezicht", body: "Het voorstel verbiedt geen ondersteuning, fictie of gedelegeerde arbeid. Het maakt de aard van de prestatie kenbaar en koppelt daar controleerbare rechten op inzage, correctie en herstel aan." },
  ]},
  { slug: "post-digitale-verzet", number: "06", book: "Boek VI", title: "Het Post-Digitale Verzet", shortTitle: "Post-Digitaal Herstel", deck: "Sanering, herstelprotocollen en analoge heropbouw na commerciële digitale afhankelijkheid.", evidence: "Praktische protocollen; geen vervanging voor medisch, juridisch of financieel advies.", sections: [
    { heading: "Maak de meter zichtbaar", body: "Breng abonnementen, losse betalingen en tijdsbesteding over een vaste periode bijeen. Feitelijk overzicht gaat vooraf aan oordeel of gedragsverandering." },
    { heading: "Herstel de uitgang", body: "Bewaar bewijs, beëindig terugkerende betalingen gecontroleerd, vraag gegevensinzage en leg betwiste transacties langs de voorwaarden van aanbieder en betaalinstelling." },
    { heading: "Analoge heropbouw", body: "Herstel vraagt niet om een wereld zonder techniek, maar om verbanden waarin aanwezigheid niet verdwijnt zodra de betaling stopt: vereniging, buurt, sport, kunst en wederkerige vriendschap." },
  ]},
] as const;

export function researchPillarBySlug(slug: string) {
  return researchPillars.find((pillar) => pillar.slug === slug);
}
