// frontend/src/features/engineering/schemas/requestSchema.ts

import { z } from "zod";

export const requestSchema = z.object({
  service_ids: z.array(z.number()).min(1),
  note: z.string().max(500),
});

export type RequestSchema = z.infer<typeof requestSchema>;
