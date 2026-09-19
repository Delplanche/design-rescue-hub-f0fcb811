import { Link } from "@tanstack/react-router";
import { ArrowUpRight, Menu, X } from "lucide-react";
import { useState, type ReactNode } from "react";
import { Button } from "@/components/ui/button";

const navigation = [
  ["Manifest", "/"], ["Dossier", "/dossier"], ["Boek", "/boek"],
  ["Filosofie", "/filosofie"], ["Juridisch", "/juridisch"],
  ["Ontkoppeling", "/ontkoppeling"], ["Archief", "/archief"],
] as const;

export function SiteShell({ children }: { children: ReactNode }) {
  const [open, setOpen] = useState(false);
  return <div className="dossier-canvas min-h-screen text-foreground">
    <header className="site-header">
      <div className="header-inner">
        <Link to="/" className="site-wordmark" aria-label="De Marktplaats van de Ziel, voorpagina">
          <span>De Marktplaats</span><span>van de Ziel</span>
        </Link>
        <nav className="desktop-nav" aria-label="Hoofdnavigatie">
          {navigation.map(([label,to])=><Link key={to} to={to} className="nav-link" activeOptions={{exact:to==="/"}}>{label}</Link>)}
        </nav>
        <Button variant="ghost" size="icon" className="menu-button" onClick={() => setOpen(!open)} aria-label={open ? "Menu sluiten" : "Menu openen"}>{open ? <X/> : <Menu/>}</Button>
      </div>
      {open && <nav className="mobile-nav" aria-label="Mobiele navigatie">
        {navigation.map(([label,to])=><Link key={to} to={to} onClick={() => setOpen(false)}>{label}</Link>)}
      </nav>}
    </header>
    {children}
    <footer className="archive-footer">
      <div className="footer-inner">
        <section className="footer-project">
          <p className="footer-kicker">Onafhankelijke onderzoeks- en essaypublicatie</p>
          <p className="footer-title">De Marktplaats van de Ziel</p>
          <p>Feitelijk dossier: Achter het profiel · Editie 01.</p>
        </section>
        <nav className="footer-sitemap" aria-label="Sitemap">
          <p className="footer-kicker">Documentatie</p>
          <Link to="/">Manifest</Link><Link to="/dossier">Dossier</Link><Link to="/boek">Boek</Link>
          <Link to="/juridisch">Juridisch</Link><Link to="/archief">Archief</Link><Link to="/claims">Claimregister</Link>
          <Link to="/bronnen">Bronnen</Link><Link to="/methodologie">Methode & correcties</Link>
        </nav>
        <section className="footer-colophon">
          <p className="footer-kicker">Colofon</p>
          <dl><div><dt>Auteur</dt><dd>Jona Zeno De Smet</dd></div><div><dt>Architectuur & Platform</dt><dd><a href="https://delplanche.com" target="_blank" rel="noreferrer">Delplanche <ArrowUpRight/></a><a href="https://delplanche.cloud" target="_blank" rel="noreferrer">delplanche.cloud <ArrowUpRight/></a></dd></div></dl>
        </section>
      </div>
      <div className="footer-base"><span>© 2026 — Publiek archief voor controle en debat</span><span>Vrij verspreidbaar voor educatieve en onderzoeksdoeleinden</span></div>
    </footer>
  </div>;
}

export function StatusBadge({ status }: { status: string }) {
  const key = status.toLowerCase().replaceAll(" ", "-");
  return <span className={`status-badge status-${key}`}><i />{status}</span>;
}