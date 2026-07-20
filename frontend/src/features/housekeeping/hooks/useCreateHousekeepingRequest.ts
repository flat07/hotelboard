// frontend/src/features/housekeeping/hooks/useCreateHousekeepingRequest.ts
import { useMutation } from "@tanstack/react-query";
import axios from "axios";
import { toast } from "sonner";

import { createHousekeepingRequest } from "../api/createHousekeepingRequest";

export function useCreateHousekeepingRequest(token: string) {
  return useMutation({
    mutationFn: (payload: { service_ids: number[]; note: string }) =>
      createHousekeepingRequest(token, payload),

    onSuccess() {
      toast.success("Request submitted.");
    },

    onError(error) {
      console.log("========== ERROR ==========");
      console.log(error);

      if (axios.isAxiosError(error)) {
        console.log("Status:", error.response?.status);
        console.log("Data:", error.response?.data);
        console.log("Headers:", error.response?.headers);
      }

      toast.error("Something went wrong.");
    },
  });
}
