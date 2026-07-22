// src/features/housekeeping/api/getHousekeepingRequests.ts

import { api } from "@/lib/axios";

import type { HousekeepingRequest, HousekeepingRequestFilters } from "../types";

export async function getHousekeepingRequests(
  filters: HousekeepingRequestFilters,
) {
  const { data } = await api.get<HousekeepingRequest[]>(
    "/staff/housekeeping/requests-get/",
    {
      params: filters,
    },
  );

  return data;
}
