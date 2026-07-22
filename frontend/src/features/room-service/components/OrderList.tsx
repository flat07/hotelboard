// src/features/room-service/components/OrderList.tsx

import type { RoomServiceOrder } from "../types";
import OrderCard from "./OrderCard";

type Props = {
  requests: RoomServiceOrder[];
};

export default function OrderList({ requests }: Props) {
  return (
    <div className="space-y-4">
      {requests.map((request) => (
        <OrderCard key={request.id} request={request} />
      ))}
    </div>
  );
}
