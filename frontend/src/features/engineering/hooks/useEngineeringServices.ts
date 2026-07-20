// frontend/src/features/engineering/hooks/useEngineeringServices.ts

import { useQuery } from "@tanstack/react-query";

import { getEngineeringServices } from "../api/getEngineeringServices";

export function useEngineeringServices(token: string) {
  return useQuery({
    queryKey: ["engineering-services", token],
    queryFn: () => getEngineeringServices(token),
    enabled: !!token,
  });
}
