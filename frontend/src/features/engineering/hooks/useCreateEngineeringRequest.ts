// frontend/src/features/engineering/hooks/useCreateEngineeringRequest.ts

import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";

import { createEngineeringRequest } from "../api/createEngineeringRequest";

export function useCreateEngineeringRequest(token: string) {
  return useMutation({
    mutationFn: createEngineeringRequest.bind(null, token),

    onSuccess() {
      toast.success("Request submitted.");
    },

    onError() {
      toast.error("Unable to submit request.");
    },
  });
}
