// frontend/src/features/housekeeping/api/createHousekeepingRequest.ts

import { api } from "@/lib/axios";

import type { HousekeepingRequestPayload } from "../types";

export async function createHousekeepingRequest(
  token: string,
  payload: HousekeepingRequestPayload,
) {
  const requestBody = {
    note: payload.note,
    items: payload.service_ids.map((id) => ({
      service: id,
    })),
  };

  console.log(requestBody);
  const { data } = await api.post(
    `/housekeeping/requests/${token}/`,
    requestBody,
  );
  console.log("createHousekeepingRequest data ", data);
  return data;
}
