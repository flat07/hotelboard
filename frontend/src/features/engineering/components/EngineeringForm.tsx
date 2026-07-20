// frontend/src/features/engineering/components/EngineeringForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

import SubmitButton from "@/components/shared/SubmitButton";
import { Checkbox } from "@/components/ui/checkbox";
import { Textarea } from "@/components/ui/textarea";

import { requestSchema, type RequestSchema } from "../schemas/requestSchema";

import type { EngineeringService } from "../types";

interface Props {
  services: EngineeringService[];
  isPending: boolean;
  onSubmit: (data: RequestSchema) => void;
}

export default function EngineeringForm({
  services,
  isPending,
  onSubmit,
}: Props) {
  const form = useForm<RequestSchema>({
    resolver: zodResolver(requestSchema),
    defaultValues: {
      service_ids: [],
      note: "",
    },
  });

  const selected = form.watch("service_ids");

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
      <div className="space-y-3">
        {services.map((service) => (
          <label
            key={service.id}
            className="flex items-center gap-3 rounded-lg border p-4"
          >
            <Checkbox
              checked={selected.includes(service.id)}
              onCheckedChange={(checked) => {
                if (checked) {
                  form.setValue("service_ids", [...selected, service.id]);
                } else {
                  form.setValue(
                    "service_ids",
                    selected.filter((id) => id !== service.id),
                  );
                }
              }}
            />

            <span>{service.name}</span>
          </label>
        ))}
      </div>

      <Textarea
        rows={5}
        placeholder="Describe the issue..."
        {...form.register("note")}
      />

      <SubmitButton isPending={isPending}>Submit Request</SubmitButton>
    </form>
  );
}
