// frontend/src/features/housekeeping/hooks/useHousekeepingServices.ts

import { useQuery } from "@tanstack/react-query";

import { getHousekeepingServices } from "../api/getHousekeepingServices";

export function useHousekeepingServices(token: string) {
  return useQuery({
    queryKey: ["housekeeping-services", token],
    queryFn: () => getHousekeepingServices(token),
    enabled: !!token,
  });
}
