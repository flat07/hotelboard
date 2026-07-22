// src/features/engineering/components/EngineeringRequestCard.tsx

import { Card } from "@/components/ui/card";

import type { EngineeringRequest } from "../types";

type Props = {
  request: EngineeringRequest;
};

export default function EngineeringRequestCard({ request }: Props) {
  return (
    <Card className="p-4 space-y-2">
      <div className="flex justify-between">
        <h3 className="font-semibold">Room {request.room_number}</h3>

        <span className="rounded bg-secondary px-2 py-1 text-xs font-medium">
          {request.status}
        </span>
      </div>

      <p>Assigned: {request.assigned_to_name ?? "-"}</p>

      <p>{request.note || "No note"}</p>

      <div className="flex flex-wrap gap-2">
        {request.items.map((item) => (
          <span key={item.id} className="rounded bg-muted px-2 py-1 text-sm">
            {item.service_name}
          </span>
        ))}
      </div>

      <p className="text-sm text-muted-foreground">
        {new Date(request.created_at).toLocaleString()}
      </p>
    </Card>
  );
}
