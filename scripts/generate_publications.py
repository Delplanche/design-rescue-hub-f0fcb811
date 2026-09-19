from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
import subprocess

R=Path(__file__).resolve().parents[1]; OUT=R/'public/publicaties'; A=R/'src/assets'
def fm(n): return subprocess.check_output(['fc-match','-f','%{file}',n],text=True).strip()
for n,q in [('Serif','DejaVu Serif'),('SerifBold','DejaVu Serif:style=Bold'),('SerifItalic','DejaVu Serif:style=Italic'),('Sans','DejaVu Sans'),('SansBold','DejaVu Sans:style=Bold'),('Mono','DejaVu Sans Mono')]: pdfmetrics.registerFont(TTFont(n,fm(q)))
P=HexColor('#fcfbf9'); I=HexColor('#242325'); W=HexColor('#8b1e2d'); M=HexColor('#6e6965'); L=HexColor('#c9c2b8')
URL='https://id-preview--84584d8a-d5ba-4e77-9eb1-bbd28d3a0a8a.lovable.app/claims'

def lines(c,text,x,y,width,size=10,leading=15,font='Sans',color=I,max_lines=None):
 c.setFont(font,size); c.setFillColor(color); words=text.split(); line=''; n=0
 for word in words:
  trial=(line+' '+word).strip()
  if c.stringWidth(trial,font,size)>width and line:
   c.drawString(x,y,line); y-=leading; n+=1; line=word
   if max_lines and n>=max_lines:return y
  else: line=trial
 if line and (not max_lines or n<max_lines):c.drawString(x,y,line);y-=leading
 return y

def base(c,w,h,num,label='EDITIE 01'):
 c.setFillColor(P);c.rect(0,0,w,h,fill=1,stroke=0);c.setStrokeColor(L);c.line(38,30,w-38,30)
 c.setFillColor(M);c.setFont('Mono',6.5);c.drawString(38,18,'DE MARKTPLAATS VAN DE ZIEL');c.drawCentredString(w/2,18,label);c.drawRightString(w-38,18,f'{num:02}')
def art(c,name,w,h,x,y,s): c.drawImage(str(A/name),x,y,s,s,mask='auto',preserveAspectRatio=True,anchor='c')
def title(c,w,h,num,kicker,title,deck='',label='EDITIE 01'):
 base(c,w,h,num,label);c.setFillColor(W);c.setFont('Mono',7);c.drawString(42,h-52,kicker)
 y=lines(c,title,42,h-92,w-84,31,31,'Serif',I)
 if deck:lines(c,deck,42,y-18,w-95,11,17,'SerifItalic',M)
def qr(c,x,y,s=58):
 widget=QrCodeWidget(URL); bounds=widget.getBounds(); scale=s/(bounds[2]-bounds[0]); drawing=Drawing(s,s,transform=[scale,0,0,scale,0,0]); drawing.add(widget); renderPDF.draw(drawing,c,x,y)

def cover(c,w,h,title_,sub,artname):
 c.setFillColor(P);c.rect(0,0,w,h,fill=1,stroke=0);art(c,artname,w,h,w*.43,h*.20,min(w,h)*.66)
 c.setFillColor(W);c.setFont('Mono',7);c.drawString(42,h-48,'ONDERZOEK · ESSAY · ARCHIEF')
 y=lines(c,title_,42,h-108,w-84,34,34,'Serif',I);lines(c,sub,42,y-22,w-84,9,14,'Mono',W)
 c.setStrokeColor(W);c.setLineWidth(2);c.line(42,42,112,42)
 c.setFont('Sans',8);c.setFillColor(I);c.drawString(124,39,'Jona Zeno De Smet');c.drawRightString(w-42,39,'Editie 01 · 19 september 2026');c.showPage()

def divider(c,w,h,num,kicker,heading,deck,artname,dark=False,label='EDITIE 01'):
 bg=I if dark else P; fg=P if dark else I; muted=HexColor('#c9c2b8') if dark else M
 c.setFillColor(bg);c.rect(0,0,w,h,fill=1,stroke=0)
 c.setFillColor(W);c.rect(42,h-58,58,3,fill=1,stroke=0);c.setFont('Mono',7);c.drawString(42,h-78,kicker)
 y=lines(c,heading,42,h-120,w*.58,30,31,'Serif',fg)
 lines(c,deck,42,y-20,w*.52,10.5,16,'SerifItalic',muted)
 art(c,artname,w,h,w*.52,h*.10,min(w,h)*.47)
 c.setStrokeColor(muted);c.line(38,30,w-38,30);c.setFillColor(muted);c.setFont('Mono',6.5);c.drawString(38,18,'DE MARKTPLAATS VAN DE ZIEL');c.drawCentredString(w/2,18,label);c.drawRightString(w-38,18,f'{num:02}')

def text_page(c,w,h,num,kicker,heading,paras,artname=None,label='EDITIE 01'):
 title(c,w,h,num,kicker,heading,label=label);y=h-145
 if artname:art(c,artname,w,h,w*.58,h*.39,min(w,h)*.42)
 for sh,body in paras:
  if y<125:c.showPage();num+=1;base(c,w,h,num,label);y=h-65
  c.setFillColor(W);c.setFont('Mono',7);c.drawString(42,y,sh.upper());y-=19
  y=lines(c,body,42,y,w-84,9.2,14.2,'Sans',I);y-=18
 return num

research=[
('01','De markt achter het profiel','Hoe agencies, verkoopsoftware en uitbesteed werk een tweede laag rond het zichtbare account vormen.',[
('De zichtbare etalage','Een profiel presenteert één naam, één gezicht en één stem. Achter die interface kan een netwerk functioneren van management, planning, promotie, chatondersteuning en software.'),('Een bedrijfstak achter de etalage','Publieke productpagina’s beloven segmentatie, geautomatiseerde opvolging en omzetsturing. De precieze omvang van die markt blijft ondoorzichtig.'),('De agency als tussenlaag','Een agency kan ondersteunen, maar ook een extra commercieel belang vormen tussen maker en abonnee. De feitelijke rol verschilt per overeenkomst.'),('De grens van de kaart','Ondersteuning bewijst op zichzelf geen misleiding. Doorslaggevend zijn verwachting, feitelijke gesprekspartner en informatie vóór betaling.')]),
('02','Wie voert het gesprek?','Betaalde chatters en hulpmiddelen kunnen uit naam van creators communiceren.',[
('De identiteit achter het venster','Reuters en BBC documenteerden medewerkers die vanuit accounts van creators berichten versturen. Dit zijn gedocumenteerde praktijken, geen universele regel.'),('Werk in ploegendienst','Notities en scripts kunnen een toon over diensten heen gelijk houden. Daardoor wordt de operationele uitvoering minder zichtbaar.'),('Automatisering als tussenvorm','Tekstsuggesties, vertaling en geautomatiseerde reacties worden aangeboden. Dat bewijst niet dat ieder gesprek door een bot wordt gevoerd.'),('Waarom transparantie telt','Een label voor creator, gemachtigde medewerker of automatisering vermindert informatie-asymmetrie.')]),
('03','Data, CRM en commerciële profilering','Gespreksnotities en segmentatie kunnen intimiteit omzetten in een verkoopinstrument.',[
('Van gesprek naar klantprofiel','CRM-producten adverteren met segmenten, notities, bestedingshistorie en massaberichten. Gesprekken worden zo commercieel ordenbaar.'),('De waarde van herinnering','Een notitie kan service verbeteren of verkoop sturen. Doel, omvang, bewaartermijn en transparantie bepalen het verschil.'),('Profilering en selectie','Bij herleidbare gegevens kan de AVG gelden, met eisen rond doelbinding, minimale verwerking, grondslag en rechten.'),('Geen bewezen psychologie-machine','Een sectorbrede classificatie van psychologische kwetsbaarheid is niet bewezen. CL-05 blijft onbevestigd.')]),
('04','Werk, contracten en afhankelijkheid','Accounttoegang en omzetverdeling kunnen creators afhankelijk maken.',[
('Operationele controle','Een agency kan planning, prijzen, chat, promotie en toegang beheren. Dat kan ondersteuning én afhankelijkheid creëren.'),('De sleutel tot het account','Controle over wachtwoorden, betaalstromen en klantgeschiedenis bepaalt wie werkelijk kan vertrekken.'),('Getuigenis en bewijs','Getuigenissen over druk rechtvaardigen onderzoek, maar bewijzen niet dat alle bureaus dwang toepassen.'),('Minimale waarborgen','Heldere opzegging, data-toegang, transparante verdeling en onafhankelijke bijstand kunnen de machtsbalans verbeteren.')]),
('05','Recht, privacy en platformen','Europese kaders zijn relevant, maar de toepassing vraagt feiten per geval.',[
('Consumenteninformatie','Of niet-gemelde ghost-chatting misleidend is, hangt af van presentatie, context en invloed op het aankoopbesluit.'),('Gegevensbescherming','Zonder zicht op datastromen, doelen en bewaartermijnen kan geen definitief AVG-oordeel worden gegeven.'),('Platformverantwoordelijkheid','De DSA versterkt zorgvuldigheid en transparantie, maar maakt een platform niet automatisch aansprakelijk voor iedere handeling.'),('Van beginsel naar toets','Lex Humanitas Digitalis is een model voor debat, geen geldend recht of individueel juridisch advies.')]),
('06','Open vragen en hervorming','Het sterkste dossier benoemt ook wat niet kan worden vastgesteld.',[
('Wat onbewezen blijft','Er is geen stevige basis voor een causaal verband met eenzaamheid, mensenhandel of systematisch witwassen.'),('Een transparantielabel','Een label voor creator, medewerker of automatisering moet controleerbaar, begrijpelijk en specifiek zijn.'),('Audit en tegenspraak','Audits, representatieve cijfers, inzage en wederhoor zijn nodig voor verdergaande conclusies.'),('Ruimte buiten de meter','Ontwerp kan vertragen, begrenzen en verwachtingen verduidelijken. Niet iedere stilte hoeft omzet te worden.')])]
essays=[('01','De gecommercialiseerde begroeting','Een begroeting draagt de belofte dat iemand iemand anders ziet. Zodra zij deel wordt van een verkooptrechter, blijft de taal persoonlijk terwijl de context commercieel wordt.'),('02','De metriek van nabijheid','Een metriek beschrijft niet alleen; zij bepaalt waarop een organisatie let. Wat niet meetbaar is — twijfel, stilte, grensstelling — dreigt uit beeld te verdwijnen.'),('03','De geleende stem','Een stem kan operationeel worden verdeeld zonder haar herkenbare naam te verliezen. Transparantie hoeft de verbeelding niet te vernietigen.'),('04','Het geheugen dat verkoopt','In een CRM wordt herinnering duurzaam, overdraagbaar en doorzoekbaar. De gebruiker onthult; het systeem onthoudt.'),('05','De prijs van beschikbaarheid','Permanente bereikbaarheid lijkt nabijheid, maar vraagt roosters, overdracht en herhaling. Een menselijke relatie verdraagt afwezigheid.'),('06','De architectuur van verlangen','Een interface is een gebouw van keuzes. Een eerlijke ruimte maakt de uitgang even zichtbaar als de ingang.'),('07','Ruimte zonder meter','Niet alles wat meetbaar is verdient een meter. Niet alles wat waarde heeft behoeft een prijs.')]
claims=[('CL-01','ONDERBOUWD','Betaalde chatters communiceren uit naam van creators','BR-01, BR-02'),('CL-02','ONDERBOUWD','Software biedt segmentatie en automatisering','BR-03'),('CL-03','AANTIJGING','Sommige contracten beperken autonomie','BR-01'),('CL-04','BETWIST','De gebruiker verwacht altijd exclusief de creator','BR-01'),('CL-05','ONBEVESTIGD','Sectorbrede kwetsbaarheidsclassificatie','Geen bevestigende bron'),('CL-06','ONBEVESTIGD','Diensten veroorzaken maatschappelijke eenzaamheid','Geen bevestigende bron')]
gloss=[('Agency','Organisatie die namens een creator commerciële of operationele taken uitvoert.'),('ARPU','Gemiddelde opbrengst per gebruiker in een bepaalde periode.'),('Chatter','Medewerker die vanuit of onder de identiteit van een creator gesprekken voert.'),('CRM','Software voor klantgegevens, notities, segmentatie en opvolging.'),('Ghost-chatting','Berichten van een ander dan de zichtbare persoon zonder duidelijke bekendmaking.'),('Profilering','Geautomatiseerde analyse of voorspelling van kenmerken en gedrag.'),('Retentie','Het vasthouden van bestaande gebruikers gedurende een periode.'),('Wederhoor','Gelegenheid voor betrokkenen om vóór publicatie te reageren.')]

def integral():
 w=h=595.28;c=canvas.Canvas(str(OUT/'de-marktplaats-van-de-ziel-editie-01.pdf'),pagesize=(w,h),pageCompression=1)
 cover(c,w,h,'De Marktplaats van de Ziel','ACHTER HET PROFIEL · INTEGRALE EDITIE','illustration-layered-archive.png');n=2
 title(c,w,h,n,'LEESWIJZER','Feit, duiding en voorstel blijven uit elkaar.','De website is leidend voor correcties. Onderzoek bevat controleerbare claims; essay bevat auteursduiding; voorstel bevat bespreekbare opties.');qr(c,w-105,55);c.showPage();n+=1
 for nr,head,deck,parts in research:
  artname=['illustration-layered-archive.png','illustration-conversation-layers.png','illustration-forensic-streams.png','illustration-boundaries-exit.png','illustration-layered-archive.png','illustration-boundaries-exit.png'][int(nr)-1]
  divider(c,w,h,n,f'HOOFDSTUK {nr}',head,deck,artname,dark=int(nr)%2==0);c.showPage();n+=1
  for i,(sh,body) in enumerate(parts,1):n=text_page(c,w,h,n,f'{nr}.{i:02} · ONDERZOEK',sh,[('Vaststelling en grens',body)],label='EDITIE 01');c.showPage();n+=1
 title(c,w,h,n,'BEGRIPPENAPPARAAT','Taal die controle mogelijk maakt.');y=h-145
 for term,desc in gloss:c.setFillColor(W);c.setFont('SerifBold',11);c.drawString(42,y,term);y=lines(c,desc,165,y,w-207,8.5,12,'Sans',I);y-=10
 c.showPage();n+=1
 title(c,w,h,n,'CLAIMREGISTER','Iedere centrale bewering draagt haar eigen gewicht.');y=h-145
 for cid,st,cl,src in claims:c.setFont('Mono',7);c.setFillColor(W);c.drawString(42,y,cid);c.drawString(95,y,st);y=lines(c,cl,190,y,w-232,8.5,12,'Sans',I);c.setFillColor(M);c.setFont('Mono',6);c.drawString(190,y+2,src);y-=18
 c.showPage();n+=1
 for nr,head,body in essays:
  n=text_page(c,w,h,n,f'ESSAY {nr}',head,[('Auteursduiding',body)],'illustration-conversation-layers.png' if nr=='03' else None);c.showPage();n+=1
 title(c,w,h,n,'MODELVOORSTEL','Lex Humanitas Digitalis','Identiteitstransparantie · dataminimalisatie · contractuele uitgang · controleerbaar toezicht. Concept, geen geldend recht.');qr(c,42,64);c.showPage();n+=1
 title(c,w,h,n,'COLOFON','Een vaste editie met een levend register.');lines(c,'Auteur: Jona Zeno De Smet\n',42,h-160,w-84,10,16,'Sans',I);lines(c,'Architectuur & Platform: Delplanche / delplanche.cloud',42,h-190,w-84,10,16,'Sans',I);lines(c,'© 2026 — Publiek archief voor controle en debat; vrij verspreidbaar voor educatieve en onderzoeksdoeleinden.',42,h-235,w-84,9,14,'Sans',M);qr(c,42,60);c.save()

def whitepaper():
 w,h=A4;c=canvas.Canvas(str(OUT/'achter-het-profiel-whitepaper.pdf'),pagesize=A4,pageCompression=1)
 cover(c,w,h,'Achter het profiel','EXECUTIVE WHITEPAPER · ACHT BLADZIJDEN','illustration-boundaries-exit.png');n=2
 pages=[('SAMENVATTING','De infrastructuur achter het profiel',[('Kern','De zichtbare één-op-één-interface kan worden ondersteund door teams, scripts en CRM-software. De centrale beleidsvraag is niet of ondersteuning mag bestaan, maar of identiteit, gegevensgebruik en belangen voldoende zichtbaar zijn.'),('Bewijsgrens','De bronnen tonen gedocumenteerde praktijken en aangeboden functionaliteit. Ze dragen geen sectorbrede schuldtoewijzing.')]),('VIJF LAGEN','Van interface naar verantwoordelijkheid',[('1 · Identiteit','Wie voert het gesprek: creator, medewerker of automatisering?'),('2 · Arbeid','Welke teams, roosters en scripts dragen de permanente beschikbaarheid?'),('3 · Data','Welke notities, segmenten en bestedingshistorie worden bewaard?'),('4 · Afhankelijkheid','Wie beheert toegang, inkomsten en overdraagbare archieven?'),('5 · Recht','Welke informatie beïnvloedt aankoop, privacy en platformzorgvuldigheid?')]),('STAND VAN HET BEWIJS','Zes claims, vier statussen',[(x[0]+' · '+x[1],x[2]+' — '+x[3]) for x in claims]),('DATA & CRM','Het geheugen als infrastructuur',[('Wat zichtbaar is','Commerciële software biedt notities, segmentatie, bestedingshistorie en massaberichten.'),('Wat niet bewezen is','Een systematische sectorbrede kwetsbaarheidsclassificatie is niet aangetoond.'),('Beleidsvraag','Kunnen gebruikers begrijpen welke gegevens worden afgeleid, met wie ze worden gedeeld en hoe lang ze blijven bestaan?')]),('RECHT','Bestaande kaders, concrete feiten',[('Consumentenrecht','Essentiële informatie mag niet zodanig worden verhuld dat zij een aankoopbesluit misleidt.'),('AVG','Doelbinding, minimale verwerking, grondslag, transparantie en rechten kunnen relevant zijn.'),('DSA','Platformplichten zijn relevant, maar betekenen geen automatische aansprakelijkheid voor iedere handeling.')]),('MODELVOORSTEL','Lex Humanitas Digitalis',[('Identiteitstransparantie','Maak bekend wie of wat communiceert.'),('Dataminimalisatie','Beperk intieme notities en maak bewaartermijnen zichtbaar.'),('Contractuele uitgang','Borg toegang tot accounts, data en inkomsten.'),('Controleerbaar toezicht','Maak audits en klachtenroutes werkelijk toetsbaar.')]),('AANBEVELING','Van stelling naar toets', [('Nu nodig','Gericht wederhoor, representatieve cijfers, onafhankelijke audits en inzage in concrete datastromen.'),('Lees verder','Scan het register voor actuele claimstatussen, bronnen en correcties.')])]
 for kick,head,parts in pages:
  n=text_page(c,w,h,n,kick,head,parts,'illustration-forensic-streams.png' if n==3 else None,'WHITEPAPER');
  if n==8:qr(c,w-105,55)
  c.showPage();n+=1
 c.save()

def reader():
 w=h=595.28;c=canvas.Canvas(str(OUT/'de-commodificatie-van-de-ziel.pdf'),pagesize=(w,h),pageCompression=1)
 cover(c,w,h,'De Commodificatie van de Ziel','EEN POST-DIGITALE BOEK-READER','illustration-conversation-layers.png');n=2
 title(c,w,h,n,'VOORAF','Dit boek interpreteert. Het dossier controleert.','De essays lezen de spanning tussen nabijheid, marktlogica en techniek. Feitelijke beweringen blijven verantwoord in Achter het profiel.');c.showPage();n+=1
 for nr,head,body in essays:
  divider(c,w,h,n,f'ESSAY {nr}',head,'Een literaire laag binnen het onderzoek. Interpretatie blijft herkenbaar gescheiden van feitelijke vaststelling.','illustration-forensic-streams.png' if nr in ('02','04') else 'illustration-conversation-layers.png',dark=int(nr)%2==0,label='BOEK-READER');c.showPage();n+=1
  n=text_page(c,w,h,n,'AUTEURSDUIDING',head,[('I',body),('II','De woorden blijven menselijk terwijl de omgeving meetbaar wordt. De vraag is welke ruimte overblijft voor twijfel, afwezigheid en een ontmoeting die niet onmiddellijk hoeft te renderen.'),('III','Een humane digitale cultuur toont haar tussenkomst, bewaart grenzen en laat de uitgang even zichtbaar als de ingang.')]);c.showPage();n+=1
 title(c,w,h,n,'SLOTBESCHOUWING','Post-digitaal manifest');lines(c,'Wij keren niet terug naar een wereld zonder techniek. Wij eisen een wereld waarin techniek haar tussenkomst toont; waarin een mens niet tot profiel, gesprek niet tot trechter en herinnering niet tot verkoopargument wordt gereduceerd.',42,h-165,w-84,15,23,'Serif',I);c.setStrokeColor(W);c.setLineWidth(4);c.line(42,h-285,42,h-365);lines(c,'Niet alles wat meetbaar is verdient een meter. Niet alles wat waarde heeft behoeft een prijs.',62,h-300,w-120,20,28,'SerifItalic',W);qr(c,w-105,55);c.showPage();n+=1
 title(c,w,h,n,'COLOFON','De Commodificatie van de Ziel');lines(c,'Auteur: Jona Zeno De Smet\nArchitectuur & Platform: Delplanche',42,h-165,w-84,10,16,'Sans',I);lines(c,'© 2026 — Publiek archief voor controle en debat; vrij verspreidbaar voor educatieve en onderzoeksdoeleinden.',42,h-235,w-84,9,14,'Sans',M);c.save()

integral();whitepaper();reader()
for p in OUT.glob('*.pdf'):print(p.name,p.stat().st_size)
