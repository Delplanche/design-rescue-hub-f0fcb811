import { createFileRoute, redirect } from "@tanstack/react-router";
export const Route = createFileRoute("/ontkoppeling")({ beforeLoad: () => { throw redirect({ to: "/onderzoek/post-digitale-verzet", statusCode: 301 }); }, component: () => null });
