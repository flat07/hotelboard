// src/routes/staff.tsx

import GuestRoute from "@/routes/GuestRoute";
import ProtectedRoute from "@/routes/ProtectedRoute";

import DashboardPage from "@/features/auth/pages/DashboardPage";
import LoginPage from "@/features/auth/pages/LoginPage";
import EngineeringDashboard from "@/features/engineering/pages/EngineeringDashboard";
import HousekeepingDashboard from "@/features/housekeeping/pages/HousekeepingDashboard";
import RoomServiceDashboard from "@/features/room-service/pages/RoomServiceDashboard";

export const staffRoutes = [
  {
    element: <GuestRoute />,
    children: [
      {
        path: "/login",
        element: <LoginPage />,
      },
    ],
  },
  {
    element: <ProtectedRoute />,
    children: [
      {
        path: "/dashboard",
        element: <DashboardPage />,
      },
      {
        path: "/staff/housekeeping",
        element: <HousekeepingDashboard />,
      },
      {
        path: "/staff/engineering",
        element: <EngineeringDashboard />,
      },
      {
        path: "/staff/room-service",
        element: <RoomServiceDashboard />,
      },
    ],
  },
];
