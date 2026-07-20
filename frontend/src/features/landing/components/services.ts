// frontend/src/features/landing/components/services.ts

import { Bed, UtensilsCrossed, Wrench } from "lucide-react";

export const services = [
  {
    id: "housekeeping",
    title: "Housekeeping",
    description: "Cleaning, towels and amenities",
    icon: Bed,
  },
  {
    id: "engineering",
    title: "Engineering",
    description: "Report maintenance issues",
    icon: Wrench,
  },
  {
    id: "room-service",
    title: "Room Service",
    description: "Food & beverages",
    icon: UtensilsCrossed,
  },
] as const;
