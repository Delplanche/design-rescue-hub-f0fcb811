import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { EditorialPage, SectionLabel } from "@/components/editorial-page";
import { researchPillars, researchPillarBySlug } from "@/lib/research-content";

export const Route = createFileRoute("/onderzoek/$slug")({
  loader: ({ params }) => { const pillar = researchPillarBySlug(params.slug); if (!pillar) throw notFound(); return pillar; },
  head: ({ loaderData }) => ({ meta: [
    { title: loaderData ? `${loaderData.title} — De Marktplaats van de Ziel` : "Onderzoek niet gevonden" },
    { name: "description", content: loaderData?.deck ?? "Deze onderzoekspijler bestaat niet." },
    { property: "og:title", content: loaderData?.title ?? "Onderzoek niet gevonden" },
    { property: "og:description", content: loaderData?.deck ?? "Deze onderzoekspijler bestaat niet." },
    { property: "og:type", content: "article" }, { name: "twitter:card", content: "summary" },
  ] }),
  component: ResearchDetail,
  notFoundComponent: () => <EditorialPage kind="Onderzoek" title="Pijler niet gevonden" deck="Deze onderzoekspijler bestaat niet of is verplaatst."><Link to="/onderzoek">Terug naar Onderzoek</Link></EditorialPage>,
});

function ResearchDetail() {
  const pillar = Route.useLoaderData();
  const index = researchPillars.findIndex((item) => item.slug === pillar.slug);
  const previous = researchPillars[index - 1];
  const next = researchPillars[index + 1];
  return <EditorialPage kind="Onderzoek" title={pillar.title} deck={pillar.deck}>
    <aside className="evidence-note"><strong>Bewijsbasis</strong><p>{pillar.evidence}</p></aside>
    <section className="prose-sections"><SectionLabel>{pillar.book} · Pijler {pillar.number}</SectionLabel>{pillar.sections.map((section, sectionIndex) => <div key={section.heading}><code>0{sectionIndex + 1}</code><h2>{section.heading}</h2><p>{section.body}</p></div>)}</section>
    <nav className="pillar-nav">{previous ? <Link to="/onderzoek/$slug" params={{ slug: previous.slug }}><ArrowLeft /><span><small>Vorige pijler</small>{previous.shortTitle}</span></Link> : <Link to="/onderzoek"><ArrowLeft /><span><small>Overzicht</small>Onderzoek</span></Link>}{next ? <Link to="/onderzoek/$slug" params={{ slug: next.slug }}><span><small>Volgende pijler</small>{next.shortTitle}</span><ArrowRight /></Link> : <Link to="/archief"><span><small>Verder</small>Bibliotheek</span><ArrowRight /></Link>}</nav>
  </EditorialPage>;
}
