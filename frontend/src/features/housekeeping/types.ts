// frontend/src/features/housekeeping/types.ts

export interface HousekeepingService {
  id: number;
  name: string;
}

export interface HousekeepingRequestPayload {
  service_ids: number[];
  note: string;
}
