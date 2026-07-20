// frontend/src/features/room-service/api/createOrder.ts

import { api } from "@/lib/axios";

import type { RoomServiceOrderPayload } from "../types";

export async function createOrder(
  token: string,
  payload: RoomServiceOrderPayload,
) {
  const { data } = await api.post(`/room-service/orders/${token}/`, payload);

  return data;
}
