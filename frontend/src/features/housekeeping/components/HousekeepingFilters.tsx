// src/features/housekeeping/components/HousekeepingFilters.tsx

import { Input } from "@/components/ui/input";

type Props = {
  search: string;
  onSearchChange: (value: string) => void;
};

export default function HousekeepingFilters({ search, onSearchChange }: Props) {
  return (
    <Input
      placeholder="Search room, staff or note..."
      value={search}
      onChange={(e) => onSearchChange(e.target.value)}
    />
  );
}
