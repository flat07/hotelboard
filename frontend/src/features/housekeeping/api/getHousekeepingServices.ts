// frontend/src/features/housekeeping/api/getHousekeepingServices.ts

import { api } from "@/lib/axios";

import type { HousekeepingService } from "../types";

export async function getHousekeepingServices(
  token: string,
): Promise<HousekeepingService[]> {
  const { data } = await api.get<HousekeepingService[]>(
    `/housekeeping/services/${token}/`,
  );

  return data;
}
