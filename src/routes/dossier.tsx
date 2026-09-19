import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/dossier")({
  component: () => <Outlet />,
});