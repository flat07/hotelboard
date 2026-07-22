// frontend/src/features/housekeeping/types.ts

export interface HousekeepingService {
  id: number;
  name: string;
}

export interface HousekeepingRequestPayload {
  service_ids: number[];
  note: string;
}

export interface HousekeepingRequest {
  id: number;
  room_number: string;
  status: string;
  assigned_to: string | null;
  note: string;
  services: string[];
  created_at: string;
}

export interface HousekeepingRequestFilters {
  status?: string;
  room?: string;
  assigned_to?: string;
  search?: string;
}
