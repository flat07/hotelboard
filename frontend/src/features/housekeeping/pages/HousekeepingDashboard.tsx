// frontend/src/features/housekeeping/pages/HousekeepingDashboard.tsx

import { useState } from "react";

import PageHeader from "@/components/layout/PageHeader";
import HousekeepingFilters from "@/features/housekeeping/components/HousekeepingFilters";
import HousekeepingRequestList from "@/features/housekeeping/components/HousekeepingRequestList";
import { useHousekeepingRequests } from "@/features/housekeeping/hooks/useHousekeepingRequests";

export default function DashboardPage() {
  const [search, setSearch] = useState("");

  const { data, isLoading } = useHousekeepingRequests({
    search,
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="space-y-6 p-4">
      <PageHeader title="Housekeeping" description="Search a service" />
      <HousekeepingFilters search={search} onSearchChange={setSearch} />

      <HousekeepingRequestList requests={data ?? []} />
    </div>
  );
}
