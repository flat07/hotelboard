// src/features/room-service/api/getOrders.ts

import { api } from "@/lib/axios";

import type { RoomServiceOrder, RoomServiceOrderFilters } from "../types";

export async function getOrders(filters: RoomServiceOrderFilters) {
  const { data } = await api.get<RoomServiceOrder[]>(
    "/staff/room-service/orders-get/",
    {
      params: filters,
    },
  );
  console.log("DEBUG: getOrders data ", data);

  return data;
}
