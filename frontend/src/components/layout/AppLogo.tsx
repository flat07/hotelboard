// frontend/src/components/layout/AppLogo.tsx

import { Hotel } from "lucide-react";

export default function AppLogo() {
  return (
    <div className="flex items-center gap-3">
      <div className="rounded-xl bg-primary p-3 text-primary-foreground">
        <Hotel className="h-6 w-6" />
      </div>

      <div>
        <h1 className="text-lg font-bold">HotelBoard</h1>

        <p className="text-xs text-muted-foreground">Guest Services</p>
      </div>
    </div>
  );
}
