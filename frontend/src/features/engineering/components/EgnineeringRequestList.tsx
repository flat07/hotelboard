// src/features/engineering/components/EngineeringRequestList.tsx

import type { EngineeringRequest } from "../types";
import EngineeringRequestCard from "./EngineeringRequestCard";

type Props = {
  requests: EngineeringRequest[];
};

export default function EngineeringRequestList({ requests }: Props) {
  return (
    <div className="space-y-4">
      {requests.map((request) => (
        <EngineeringRequestCard key={request.id} request={request} />
      ))}
    </div>
  );
}
