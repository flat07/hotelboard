// src/features/room-service/components/OrderFilters.tsx

import { Input } from "@/components/ui/input";

type Props = {
  search: string;
  onSearchChange: (value: string) => void;
};

export default function OrderFilters({ search, onSearchChange }: Props) {
  return (
    <Input
      placeholder="Search room service order, room, status..."
      value={search}
      onChange={(e) => onSearchChange(e.target.value)}
    />
  );
}
