// frontend/src/features/auth/api/refresh.ts

import { api } from "@/lib/axios";

export async function refresh(refresh: string) {
  const { data } = await api.post<{
    access: string;
  }>("/staff/auth/refresh/", {
    refresh,
  });

  return data;
}
