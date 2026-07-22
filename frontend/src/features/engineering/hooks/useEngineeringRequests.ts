// src/features/engineering/hooks/useEngineeringRequests.ts

import { useQuery } from "@tanstack/react-query";

import { getEngineeringRequests } from "../api/getEngineeringRequests";
import type { EngineeringRequestFilters } from "../types";

export function useEngineeringRequests(filters: EngineeringRequestFilters) {
  return useQuery({
    queryKey: ["engineering-requests", filters],
    queryFn: () => getEngineeringRequests(filters),
  });
}
