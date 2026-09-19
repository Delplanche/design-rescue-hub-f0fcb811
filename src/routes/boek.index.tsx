import { createFileRoute, redirect } from "@tanstack/react-router";
export const Route = createFileRoute("/boek/")({ beforeLoad: () => { throw redirect({ to: "/onderzoek", statusCode: 301 }); }, component: () => null });
