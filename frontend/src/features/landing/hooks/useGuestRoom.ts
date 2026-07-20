// frontend/src/features/landing/hooks/useGuestRoom.ts

import { useQuery } from "@tanstack/react-query";

import { getGuestRoom } from "../api/getGuestRoom";

export function useGuestRoom(token: string) {
  return useQuery({
    queryKey: ["guest-room", token],
    queryFn: () => getGuestRoom(token),
    enabled: !!token,
  });
}
