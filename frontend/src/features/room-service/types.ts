// frontend/src/features/room-service/types.ts

export interface MenuItem {
  id: number;
  name: string;
  description: string;
  price: string;
}

export interface MenuCategory {
  id: number;
  name: string;
  items: MenuItem[];
}

export interface RoomServiceOrderItem {
  id: number;
  menu_item: number;
  menu_item_name: string;
  quantity: number;
  price: number;
}

export interface RoomServiceOrderPayload {
  items: RoomServiceOrderItem[];
  note: string;
}

export interface RoomServiceOrder {
  id: number;
  room: string;
  room_number: string;
  status: string;
  assigned_to: string | null;
  assigned_to_name: string | null;
  note: string;
  total_price: string;
  services: string[];
  created_at: string;
  items: RoomServiceOrderItem[];
}

export interface RoomServiceOrderFilters {
  status?: string;
  room?: string;
  assigned_to?: string;
  search?: string;
}
