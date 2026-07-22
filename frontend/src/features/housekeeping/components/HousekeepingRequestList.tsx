// src/features/housekeeping/components/HousekeepingRequestList.tsx

import type { HousekeepingRequest } from "../types";
import HousekeepingRequestCard from "./HousekeepingRequestCard";

type Props = {
  requests: HousekeepingRequest[];
};

export default function HousekeepingRequestList({ requests }: Props) {
  return (
    <div className="space-y-4">
      {requests.map((request) => (
        <HousekeepingRequestCard key={request.id} request={request} />
      ))}
    </div>
  );
}
