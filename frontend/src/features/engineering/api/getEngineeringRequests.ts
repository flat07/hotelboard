// src/features/engineering/api/getEngineeringRequests.ts

import { api } from "@/lib/axios";

import type { EngineeringRequest, EngineeringRequestFilters } from "../types";

export async function getEngineeringRequests(
  filters: EngineeringRequestFilters,
) {
  const { data } = await api.get<EngineeringRequest[]>(
    "/staff/engineering/requests-get/",
    {
      params: filters,
    },
  );

  return data;
}
