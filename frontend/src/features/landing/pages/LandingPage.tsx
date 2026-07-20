// frontend/src/features/landing/pages/LandingPage.tsx

import { useNavigate, useParams } from "react-router-dom";

import ErrorState from "@/components/shared/ErrorState";
import LoadingPage from "@/components/shared/LoadingPage";

import RoomCard from "../components/RoomCard";
import ServiceCard from "../components/ServiceCard";
import { services } from "../components/services";
import WelcomeCard from "../components/WelcomeCard";
import { useGuestRoom } from "../hooks/useGuestRoom";

export default function LandingPage() {
  const navigate = useNavigate();

  const { token = "" } = useParams();

  const { data, isLoading, isError, refetch } = useGuestRoom(token);

  if (isLoading) {
    return <LoadingPage />;
  }

  if (isError || !data) {
    return (
      <ErrorState
        title="Invalid QR Code"
        description="Please contact reception."
        onRetry={refetch}
      />
    );
  }

  return (
    <main className="space-y-6 p-4">
      <WelcomeCard />

      <RoomCard roomNumber={data.room_number} roomType={data.room_type} />

      <section className="space-y-3">
        {services.map((service) => {
          const Icon = service.icon;

          return (
            <ServiceCard
              key={service.id}
              title={service.title}
              description={service.description}
              icon={<Icon className="h-6 w-6" />}
              onClick={() => navigate(`/${token}/${service.id}`)}
            />
          );
        })}
      </section>
    </main>
  );
}
