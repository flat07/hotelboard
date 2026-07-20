// frontend/src/features/dashboard/pages/DashboardPage.tsx

import { useAuth } from "@/contexts/AuthContext";

import { Button } from "@/components/ui/button";

export default function DashboardPage() {
  const { user, logout } = useAuth();

  return (
    <main className="p-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Dashboard</h1>

          <p className="text-muted-foreground">Welcome {user?.username}</p>
        </div>

        <Button variant="destructive" onClick={logout}>
          Logout
        </Button>
      </div>
    </main>
  );
}
