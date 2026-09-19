import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { SiteShell, StatusBadge } from "@/components/site-shell";
import { chapters, claims, sources } from "@/lib/dossier-data";

export const Route = createFileRoute("/dossier/$slug")({
  loader: ({ params }) => { const chapter = chapters.find(c => c.slug === params.slug); if (!chapter) throw notFound(); return chapter; },
  head: ({ loaderData }) => ({ meta: [
    { title: loaderData ? `${loaderData.title} — Achter het profiel` : "Hoofdstuk niet gevonden" },
    { name: "description", content: loaderData?.deck ?? "Dit hoofdstuk bestaat niet." },
    { property: "og:title", content: loaderData?.title ?? "Hoofdstuk niet gevonden" },
    { property: "og:description", content: loaderData?.deck ?? "Dit hoofdstuk bestaat niet." },
    { property: "og:type", content: "article" }, { name: "twitter:card", content: "summary" },
  ]}),
  component: DossierChapter,
  notFoundComponent: () => <SiteShell><main className="page-wrap"><h1>Dit hoofdstuk bestaat niet.</h1><Link to="/dossier">Naar het dossier</Link></main></SiteShell>,
});

function DossierChapter() {
  const chapter = Route.useLoaderData(); const index = chapters.findIndex(c => c.slug === chapter.slug);
  const previous = chapters[index - 1]; const following = chapters[index + 1];
  const chapterClaims = claims.filter(c => c.chapter === chapter.nr); const sourceIds = [...new Set(chapterClaims.flatMap(c => c.sources))];
  return <SiteShell><main><header className="chapter-hero paper-hero"><div className="mx-auto max-w-5xl"><div className="chapter-meta"><span>Onderzoek</span><span>{chapter.nr} / 06</span><span>Editie 01</span></div><p className="content-kind kind-onderzoek">Achter het profiel</p><h1>{chapter.title}</h1><p>{chapter.deck}</p></div></header>
    <div className="reader-layout"><aside className="reader-index"><p className="eyebrow">In dit hoofdstuk</p>{chapter.sections.map((s,i)=><a href={`#deel-${i+1}`} key={s[0]}><span>0{i+1}</span>{s[0]}</a>)}<Link to="/claims">Claimregister →</Link></aside>
      <article className="article-body">{chapter.sections.map((s,i)=><section id={`deel-${i+1}`} key={s[0]}><p className="section-number">0{i+1}</p><h2>{s[0]}</h2><p>{s[1]}</p>{i===0&&chapterClaims.map(c=><div className="inline-claim" key={c.id}><div><code>{c.id}</code><StatusBadge status={c.status}/></div><strong>{c.title}</strong></div>)}</section>)}
      {sourceIds.length>0&&<section className="chapter-sources"><p className="eyebrow">Geraadpleegde bronnen</p>{sourceIds.map(id=>{const s=sources.find(x=>x.id===id);return s?<a href={s.url} target="_blank" rel="noreferrer" key={id}><code>{id}</code><span>{s.publisher} — {s.title}</span>↗</a>:null})}</section>}</article></div>
    <nav className="chapter-nav">{previous?<Link to="/dossier/$slug" params={{slug:previous.slug}}><ArrowLeft/><span><small>Vorige</small>{previous.title}</span></Link>:<Link to="/dossier"><ArrowLeft/><span><small>Terug</small>Dossier</span></Link>}{following?<Link className="next" to="/dossier/$slug" params={{slug:following.slug}}><span><small>Volgende</small>{following.title}</span><ArrowRight/></Link>:<Link className="next" to="/archief"><span><small>Verder</small>Archief</span><ArrowRight/></Link>}</nav>
  </main></SiteShell>;
}