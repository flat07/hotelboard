// frontend/src/features/engineering/api/createEngineeringRequest.ts

import { api } from "@/lib/axios";

import type { EngineeringRequestPayload } from "../types";

export async function createEngineeringRequest(
  token: string,
  payload: EngineeringRequestPayload,
) {
  const requestBody = {
    note: payload.note,
    items: payload.service_ids.map((id) => ({
      service: id,
    })),
  };

  console.log(requestBody);
  const { data } = await api.post(
    `/engineering/requests/${token}/`,
    requestBody,
  );

  return data;
}
