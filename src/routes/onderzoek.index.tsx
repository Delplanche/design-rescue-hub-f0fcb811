import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight } from "lucide-react";
import { EditorialPage, SectionLabel } from "@/components/editorial-page";
import { researchPillars } from "@/lib/research-content";

export const Route = createFileRoute("/onderzoek/")({
  head: () => ({ meta: [
    { title: "Onderzoek — De Marktplaats van de Ziel" },
    { name: "description", content: "Zes feitelijke onderzoekspijlers over techniek, financiën, neurobiologie, sociologie, recht en herstel." },
    { property: "og:title", content: "De zes onderzoekspijlers" },
    { property: "og:description", content: "De inhoudelijke kern van De Marktplaats van de Ziel, modulair en controleerbaar opgebouwd." },
    { property: "og:type", content: "website" }, { name: "twitter:card", content: "summary" },
  ] }),
  component: ResearchPage,
});

function ResearchPage() {
  return <EditorialPage kind="Onderzoek" title="Zes pijlers. Eén systeemanalyse." deck="De Hexalogie ontleedt de infrastructuur, geldstromen, gedragsmechanismen, demografie, rechtsorde en herstelroutes als afzonderlijke maar verbonden onderzoeksvelden." next={{ to: "/archief", label: "Open de Bibliotheek" }}>
    <aside className="evidence-note"><strong>Redactionele regel</strong><p>Vaststelling, interpretatie en voorstel blijven zichtbaar gescheiden. Iedere pijler benoemt ook de grens van het beschikbare bewijs.</p></aside>
    <section><SectionLabel>De inhoud · Boek I–VI</SectionLabel><div className="research-grid">{researchPillars.map((pillar) => <Link key={pillar.slug} to="/onderzoek/$slug" params={{ slug: pillar.slug }} className="research-card"><div><code>{pillar.number}</code><span>{pillar.book}</span></div><h2>{pillar.shortTitle}</h2><p>{pillar.deck}</p><span className="read-label">Open pijler <ArrowRight /></span></Link>)}</div></section>
  </EditorialPage>;
}
