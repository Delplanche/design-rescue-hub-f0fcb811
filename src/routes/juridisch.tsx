import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/juridisch")({
  component: () => <Outlet />,
});