// frontend/src/features/room-service/api/getMenu.ts

import { api } from "@/lib/axios";

import type { MenuCategory } from "../types";

export async function getMenu(token: string): Promise<MenuCategory[]> {
  const { data } = await api.get<MenuCategory[]>(
    `/room-service/menu/${token}/`,
  );
  // console.log("getMenu data ", data);
  return data;
}
