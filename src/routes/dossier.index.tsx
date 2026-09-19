import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight } from "lucide-react";
import { EditorialPage, SectionLabel } from "@/components/editorial-page";
import { StatusBadge } from "@/components/site-shell";
import { chapters, claims, glossary } from "@/lib/dossier-data";

export const Route = createFileRoute("/dossier/")({
  head: () => ({ meta: [
    { title: "Achter het profiel — Onderzoeksdossier" },
    { name: "description", content: "Het controleerbare onderzoeksdossier over de commerciële infrastructuur rond digitale intimiteit." },
    { property: "og:title", content: "Achter het profiel — Onderzoeksdossier" },
    { property: "og:description", content: "Vierentwintig onderzoeksdelen, een claimregister en een openbaar bronnenspoor." },
    { property: "og:type", content: "website" }, { name: "twitter:card", content: "summary" },
  ]}),
  component: DossierPage,
});

function DossierPage() {
  return <EditorialPage kind="Onderzoek" title="Achter het profiel" deck="Een feitelijk dossier over wie spreekt, welke gegevens meebewegen en waar commerciële verantwoordelijkheid begint." next={{to:"/claims",label:"Open het claimregister"}}>
    <aside className="evidence-note"><strong>Bewijsregel</strong><p>Onderzoek, getuigenis en onbevestigde hypothese krijgen elk een eigen status. De status is geen waarheidsscore.</p></aside>
    <section><SectionLabel>Zes hoofdstukken · vierentwintig onderzoeksdelen</SectionLabel><div className="chapter-list editorial-list">{chapters.map(c=><Link to="/dossier/$slug" params={{slug:c.slug}} className="chapter-item" key={c.slug}><span className="chapter-nr">{c.nr}</span><div><h2>{c.title}</h2><p>{c.deck}</p></div><span className="read-label">Lees <ArrowRight /></span></Link>)}</div></section>
    <section><SectionLabel>Stand van het bewijs</SectionLabel><div className="register-strip">{claims.map(c=><div key={c.id}><code>{c.id}</code><StatusBadge status={c.status}/><p>{c.title}</p></div>)}</div></section>
    <section><SectionLabel>Begrippenapparaat</SectionLabel><dl className="glossary-grid">{glossary.map(([term,definition])=><div key={term}><dt>{term}</dt><dd>{definition}</dd></div>)}</dl></section>
  </EditorialPage>;
}