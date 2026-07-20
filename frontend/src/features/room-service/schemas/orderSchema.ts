// frontend/src/features/room-service/schemas/orderSchema.ts

import { z } from "zod";

export const orderSchema = z.object({
  items: z
    .array(
      z.object({
        menu_item: z.number(),
        quantity: z.number().min(1),
      }),
    )
    .min(1),
  note: z.string().max(500),
});

export type OrderSchema = z.infer<typeof orderSchema>;
