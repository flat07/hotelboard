// src/features/housekeeping/hooks/useHousekeepingRequests.ts

import { useQuery } from "@tanstack/react-query";

import { getHousekeepingRequests } from "../api/getHousekeepingRequests";
import type { HousekeepingRequestFilters } from "../types";

export function useHousekeepingRequests(filters: HousekeepingRequestFilters) {
  return useQuery({
    queryKey: ["housekeeping-requests", filters],
    queryFn: () => getHousekeepingRequests(filters),
  });
}
