// frontend/src/features/room-service/hooks/useCreateOrder.ts

import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";

import { createOrder } from "../api/createOrder";

export function useCreateOrder(token: string) {
  return useMutation({
    mutationFn: createOrder.bind(null, token),

    onSuccess() {
      toast.success("Order submitted.");
    },

    onError() {
      toast.error("Unable to submit order.");
    },
  });
}
