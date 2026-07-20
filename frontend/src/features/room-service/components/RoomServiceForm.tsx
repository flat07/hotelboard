// frontend/src/features/room-service/components/RoomServiceForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useState } from "react";
import { useForm } from "react-hook-form";

import SubmitButton from "@/components/shared/SubmitButton";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

import { orderSchema, type OrderSchema } from "../schemas/orderSchema";

import type { MenuCategory } from "../types";

interface Props {
  menu: MenuCategory[];
  isPending: boolean;
  onSubmit: (data: OrderSchema) => void;
}

export default function RoomServiceForm({ menu, isPending, onSubmit }: Props) {
  // console.log("RoomServiceForm menu ", menu);
  const [items, setItems] = useState<{ menu_item: number; quantity: number }[]>(
    [],
  );

  const form = useForm<OrderSchema>({
    resolver: zodResolver(orderSchema),
    defaultValues: {
      items: [],
      note: "",
    },
  });

  function updateItem(id: number, quantity: number) {
    const next = items.filter((i) => i.menu_item !== id);

    if (quantity > 0) {
      next.push({
        menu_item: id,
        quantity,
      });
    }

    setItems(next);
    form.setValue("items", next);
  }

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
      <div className="space-y-8">
        {menu.map((category) => (
          <div key={category.id}>
            <h2 className="mb-4 text-xl font-bold">{category.name}</h2>

            <div className="space-y-4">
              {category.items.map((item) => (
                <div key={item.id} className="rounded-lg border p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="font-semibold">{item.name}</h3>

                      <p className="text-sm text-muted-foreground">
                        {item.description}
                      </p>

                      <p className="mt-1 font-medium">${item.price}</p>
                    </div>

                    <Input
                      type="number"
                      min={0}
                      defaultValue={0}
                      className="w-20"
                      onChange={(e) =>
                        updateItem(item.id, Number(e.target.value))
                      }
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <Textarea
        rows={4}
        placeholder="Additional note..."
        {...form.register("note")}
      />

      <SubmitButton isPending={isPending}>Place Order</SubmitButton>
    </form>
  );
}
