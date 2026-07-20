// frontend/src/app/router.tsx
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import PublicLayout from "@/components/layout/PublicLayout";

import EngineeringPage from "@/features/engineering/pages/EngineeringPage";
import HousekeepingPage from "@/features/housekeeping/pages/HousekeepingPage";
import LandingPage from "@/features/landing/pages/LandingPage";
import RoomServicePage from "@/features/room-service/pages/RoomServicePage";

function Home() {
  return <h1>Scan the QR code</h1>;
}

const router = createBrowserRouter([
  {
    element: <PublicLayout />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/:token",
        element: <LandingPage />,
      },
      {
        path: "/:token/housekeeping",
        element: <HousekeepingPage />,
      },
      {
        path: "/:token/engineering",
        element: <EngineeringPage />,
      },
      {
        path: "/:token/room-service",
        element: <RoomServicePage />,
      },
    ],
  },
]);

export function AppRouter() {
  return <RouterProvider router={router} />;
}
