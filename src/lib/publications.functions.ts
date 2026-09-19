import { createServerFn } from "@tanstack/react-start";
import { createClient } from "@supabase/supabase-js";
import type { Database } from "@/integrations/supabase/types";

export type Publication = Pick<Database["public"]["Tables"]["publications"]["Row"],
  "id" | "sort_order" | "code" | "kind" | "title" | "description" | "format" | "audience" | "page_count" | "file_size" | "pdf_path"
>;

export const getPublications = createServerFn({ method: "GET" }).handler(async (): Promise<Publication[]> => {
  const url = process.env["SUPABASE_URL"];
  const key = process.env["SUPABASE_PUBLISHABLE_KEY"];
  if (!url || !key) throw new Error("De bibliotheekverbinding is niet beschikbaar.");
  const client = createClient<Database>(url, key, { auth: { persistSession: false, autoRefreshToken: false } });
  const { data, error } = await client
    .from("publications")
    .select("id,sort_order,code,kind,title,description,format,audience,page_count,file_size,pdf_path")
    .eq("is_published", true)
    .order("sort_order");
  if (error) throw new Error(`De bibliotheek kon niet worden geladen: ${error.message}`);
  return data;
});
