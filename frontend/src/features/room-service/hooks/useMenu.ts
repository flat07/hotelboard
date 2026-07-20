// frontend/src/features/room-service/hooks/useMenu.ts

import { useQuery } from "@tanstack/react-query";

import { getMenu } from "../api/getMenu";

export function useMenu(token: string) {
  return useQuery({
    queryKey: ["room-service-menu", token],
    queryFn: () => getMenu(token),
    enabled: !!token,
  });
}
