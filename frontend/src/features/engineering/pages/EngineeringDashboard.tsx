// frontend/src/features/engineering/pages/EngineeringDashboard.tsx

import { useState } from "react";

import PageHeader from "@/components/layout/PageHeader";
import EngineeringRequestList from "@/features/engineering/components/EgnineeringRequestList";
import EngineeringFilters from "@/features/engineering/components/EngineeringFilters";
import { useEngineeringRequests } from "@/features/engineering/hooks/useEngineeringRequests";

export default function EngineeringDashboard() {
  const [search, setSearch] = useState("");

  const { data, isLoading } = useEngineeringRequests({
    search,
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="space-y-6 p-4">
      <PageHeader title="Engineering" description="Search a service" />
      <EngineeringFilters search={search} onSearchChange={setSearch} />

      <EngineeringRequestList requests={data ?? []} />
    </div>
  );
}
