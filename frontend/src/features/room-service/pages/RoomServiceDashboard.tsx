// frontend/src/features/room-service/pages/RoomServiceDashboard.tsx

import { useState } from "react";

import PageHeader from "@/components/layout/PageHeader";
import OrderFilters from "@/features/room-service/components/OrderFilters";
import OrderList from "@/features/room-service/components/OrderList";
import { useOrder } from "@/features/room-service/hooks/useOrder";

export default function RoomServiceDashboard() {
  const [search, setSearch] = useState("");

  const { data, isLoading } = useOrder({
    search,
  });
  console.log("DEBUG: data ", data);

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="space-y-6 p-4">
      <PageHeader
        title="Room Service"
        description="Search a room service orders"
      />
      <OrderFilters search={search} onSearchChange={setSearch} />

      <OrderList requests={data ?? []} />
    </div>
  );
}
