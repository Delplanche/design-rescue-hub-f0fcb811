import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/boek")({
  component: () => <Outlet />,
});