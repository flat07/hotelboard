// frontend/src/features/landing/components/RoomCard.tsx

import { BedDouble } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";

interface Props {
  roomNumber: string;
  roomType: string;
}

export default function RoomCard({ roomNumber, roomType }: Props) {
  return (
    <Card>
      <CardContent className="flex items-center gap-4 p-5">
        <div className="rounded-xl bg-primary/10 p-3">
          <BedDouble className="h-7 w-7 text-primary" />
        </div>

        <div>
          <p className="text-sm text-muted-foreground">Your Room</p>

          <h2 className="text-2xl font-bold">{roomNumber}</h2>

          <p className="text-muted-foreground">{roomType}</p>
        </div>
      </CardContent>
    </Card>
  );
}
