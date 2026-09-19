import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/hoofdstuk/$slug")({
  beforeLoad: ({params}) => { throw redirect({to:"/dossier/$slug",params:{slug:params.slug},statusCode:301}); },
  component: () => null,
});