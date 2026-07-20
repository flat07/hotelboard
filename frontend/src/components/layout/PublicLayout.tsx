// frontend/src/components/layout/PublicLayout.tsx

import { Outlet } from "react-router-dom";

import AppLogo from "./AppLogo";
import PublicFooter from "./PublicFooter";

import ThemeToggle from "@/components/shared/ThemeToggle";

export default function PublicLayout() {
  return (
    <div className="min-h-screen bg-muted/30">
      <div className="mx-auto flex min-h-screen max-w-md flex-col">
        <header className="border-b bg-background px-5 py-4">
          <AppLogo />
          <ThemeToggle />
        </header>

        <div className="flex-1">
          <Outlet />
        </div>

        <PublicFooter />
      </div>
    </div>
  );
}
