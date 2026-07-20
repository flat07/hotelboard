// frontend/src/features/engineering/types.ts

export interface EngineeringService {
  id: number;
  name: string;
}

export interface EngineeringRequestPayload {
  service_ids: number[];
  note: string;
}
