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
  menu_item: number;
  quantity: number;
}

export interface RoomServiceOrderPayload {
  items: RoomServiceOrderItem[];
  note: string;
}
