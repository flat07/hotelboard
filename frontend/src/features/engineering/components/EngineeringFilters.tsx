// src/features/engineering/components/EngineeringFilters.tsx

import { Input } from "@/components/ui/input";

type Props = {
  search: string;
  onSearchChange: (value: string) => void;
};

export default function EngineeringFilters({ search, onSearchChange }: Props) {
  return (
    <Input
      placeholder="Search room, staff or note..."
      value={search}
      onChange={(e) => onSearchChange(e.target.value)}
    />
  );
}
