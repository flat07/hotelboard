// frontend/src/features/engineering/api/getEngineeringServices.ts

import { api } from "@/lib/axios";

import type { EngineeringService } from "../types";

export async function getEngineeringServices(
  token: string,
): Promise<EngineeringService[]> {
  const { data } = await api.get<EngineeringService[]>(
    `public/engineering/services/${token}/`,
  );

  return data;
}
