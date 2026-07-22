// src/features/room-service/hooks/useOrder.ts

import { useQuery } from "@tanstack/react-query";

import { getOrders } from "../api/getOrders";
import type { RoomServiceOrderFilters } from "../types";

export function useOrder(filters: RoomServiceOrderFilters) {
  return useQuery({
    queryKey: ["roomservice-orders", filters],
    queryFn: () => getOrders(filters),
  });
}
