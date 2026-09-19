CREATE TABLE public.publications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  sort_order INTEGER NOT NULL UNIQUE,
  code TEXT NOT NULL UNIQUE,
  kind TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  format TEXT NOT NULL,
  audience TEXT NOT NULL,
  page_count INTEGER NOT NULL CHECK (page_count > 0),
  file_size TEXT NOT NULL,
  pdf_path TEXT NOT NULL UNIQUE,
  is_published BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
GRANT SELECT ON public.publications TO anon;
GRANT SELECT ON public.publications TO authenticated;
GRANT ALL ON public.publications TO service_role;
ALTER TABLE public.publications ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Published publications are publicly readable"
ON public.publications FOR SELECT TO anon, authenticated
USING (is_published = true);
INSERT INTO public.publications (sort_order, code, kind, title, description, format, audience, page_count, file_size, pdf_path) VALUES
(1, 'WP', 'PERS-WHITEPAPER', 'Lex Humanitas Digitalis & Systeemanalyse', 'Een beknopte systeemanalyse voor pers, beleid en toezicht: kernbevindingen, het juridische gat en concrete modelwetgeving.', 'A4', 'Pers · beleid · toezicht', 2, '98 kB', '/publicaties/achter-het-profiel-whitepaper.pdf'),
(2, '01', 'BOEK I', 'De Technologische Deceptie', 'Infrastructuur, CRM-dossiers, chat-farms en de geautomatiseerde productie van persoonlijk contact.', '21 × 21 cm', 'Techniek · onderzoek', 26, '1,4 MB', '/publicaties/boek-i-de-technologische-deceptie.pdf'),
(3, '02', 'BOEK II', 'De Financiële Schaduweconomie', 'Carding, betaalstromen, witwasrisico’s en de verdeling van opbrengsten tussen platform, bureau en creator.', '21 × 21 cm', 'Financiën · toezicht', 18, '1,2 MB', '/publicaties/boek-ii-de-financiele-schaduweconomie.pdf'),
(4, '03', 'BOEK III', 'De Neurobiologie van de Verslaving', 'Variable-reward, gedragsmatige binding en de psychologische belasting van gebruikers en operators.', '21 × 21 cm', 'Gedrag · gezondheid', 15, '1,1 MB', '/publicaties/boek-iii-de-neurobiologie-van-de-afhankelijkheid.pdf'),
(5, '04', 'BOEK IV', 'De Sociologische Implosie', 'Harde demografische data en objectieve substitutie-effecten, met Korea en Japan als begrensd vergelijkingskader.', '21 × 21 cm', 'Demografie · sociologie', 14, '1,0 MB', '/publicaties/boek-iv-de-sociologische-implosie.pdf'),
(6, '05', 'BOEK V', 'Het Juridisch Failliet & Modelwetgeving', 'Het bestaande juridische kader, de handhavingskloof en Lex Humanitas Digitalis als toetsbaar modelvoorstel.', '21 × 21 cm', 'Recht · beleid', 17, '1,2 MB', '/publicaties/boek-v-het-juridisch-failliet.pdf'),
(7, '06', 'BOEK VI', 'Het Post-Digitale Verzet', 'Sanering, herstelprotocollen en analoge heropbouw voor gebruikers, makers en toezichthouders.', '21 × 21 cm', 'Herstel · praktijk', 18, '1,2 MB', '/publicaties/boek-vi-het-post-digitale-verzet.pdf');