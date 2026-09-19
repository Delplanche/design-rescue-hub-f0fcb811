import { createFileRoute, redirect } from "@tanstack/react-router";
export const Route = createFileRoute("/ontkoppeling")({ beforeLoad: () => { throw redirect({ to: "/onderzoek/$slug", params: { slug: "post-digitale-verzet" }, statusCode: 301 }); }, component: () => null });
