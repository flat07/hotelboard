// frontend/src/features/landing/api/getGuestRoom.ts

import { api } from "@/lib/axios";

import type { GuestRoom } from "../types";

export async function getGuestRoom(token: string): Promise<GuestRoom> {
  const { data } = await api.get<GuestRoom>(`/rooms/guest/${token}/`);
  console.log("data ", data);
  return data;
}
