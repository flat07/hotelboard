// frontend/src/features/engineering/types.ts

export interface EngineeringService {
  id: number;
  name: string;
}

export interface EngineeringRequestPayload {
  service_ids: number[];
  note: string;
}

export interface EngineeringRequestItem {
  id: number;
  service: number;
  service_name: string;
}

export interface EngineeringRequest {
  id: number;
  room_number: string;
  status: string;
  note: string;
  assigned_to_name: string | null;
  completed_at: string | null;
  created_at: string;
  items: EngineeringRequestItem[];
}

export interface EngineeringRequestFilters {
  status?: string;
  room?: string;
  assigned_to?: string;
  search?: string;
  ordering?: string;
}
