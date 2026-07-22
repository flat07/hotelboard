// src/features/housekeeping/components/HousekeepingRequestCard.tsx

import { Card } from "@/components/ui/card";

import type { HousekeepingRequest } from "../types";

type Props = {
  request: HousekeepingRequest;
};

export default function HousekeepingRequestCard({ request }: Props) {
  return (
    <Card className="p-4 space-y-2">
      <div className="flex justify-between">
        <h3 className="font-semibold">Room {request.room_number}</h3>

        <span>{request.status}</span>
      </div>

      <p>Assigned: {request.assigned_to ?? "-"}</p>

      <p>{request.note || "No note"}</p>

      <div className="flex flex-wrap gap-2">
        {request.services.map((service) => (
          <span key={service} className="rounded px-2 py-1 text-sm">
            {service}
          </span>
        ))}
      </div>

      <p className="text-sm text-muted-foreground">
        {new Date(request.created_at).toLocaleString()}
      </p>
    </Card>
  );
}
