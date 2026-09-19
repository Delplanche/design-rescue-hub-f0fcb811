import { Link } from "@tanstack/react-router";
import { ArrowRight } from "lucide-react";
import { SiteShell } from "@/components/site-shell";

export function EditorialPage({
  kind,
  title,
  deck,
  children,
  next,
}: {
  kind: "Onderzoek" | "Essay" | "Voorstel" | "Archief";
  title: string;
  deck: string;
  children: React.ReactNode;
  next?: { to: "/dossier" | "/boek" | "/filosofie" | "/juridisch" | "/ontkoppeling" | "/archief" | "/claims"; label: string };
}) {
  return (
    <SiteShell>
      <main>
        <header className="editorial-hero">
          <div className="editorial-hero-inner">
            <p className={`content-kind kind-${kind.toLowerCase()}`}>{kind}</p>
            <h1>{title}</h1>
            <p className="editorial-deck">{deck}</p>
          </div>
        </header>
        <div className="editorial-content">{children}</div>
        {next && <div className="editorial-next"><Link to={next.to}>{next.label}<ArrowRight /></Link></div>}
      </main>
    </SiteShell>
  );
}

export function SectionLabel({ children }: { children: React.ReactNode }) {
  return <p className="eyebrow text-alert">{children}</p>;
}