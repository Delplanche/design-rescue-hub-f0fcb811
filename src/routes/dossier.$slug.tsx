import { createFileRoute, redirect } from "@tanstack/react-router";
export const Route = createFileRoute("/dossier/$slug")({ beforeLoad: () => { throw redirect({ to: "/onderzoek", statusCode: 301 }); }, component: () => null });
