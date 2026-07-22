// src/features/housekeeping/components/OrderCard.tsx

import { Card } from "@/components/ui/card";

import type { RoomServiceOrder } from "../types";

type Props = {
  request: RoomServiceOrder;
};

export default function OrderCard({ request }: Props) {
  return (
    <Card className="p-4 space-y-2">
      <div className="flex justify-between">
        <h3 className="font-semibold">Room {request.room_number}</h3>

        <span>{request.status}</span>
      </div>

      <p>Assigned: {request.assigned_to ?? "-"}</p>

      <p>{request.note || "No note"}</p>

      <div className="flex flex-wrap gap-2">
        {request.items.map((item) => (
          <span key={item.id} className="rounded px-2 py-1 text-sm">
            {item.menu_item_name}
          </span>
        ))}
      </div>

      <p className="text-sm text-muted-foreground">
        {new Date(request.created_at).toLocaleString()}
      </p>
    </Card>
  );
}
