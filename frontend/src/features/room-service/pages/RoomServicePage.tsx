// frontend/src/features/room-service/pages/RoomServicePage.tsx

import { useParams } from "react-router-dom";

import PageContainer from "@/components/layout/PageContainer";
import PageHeader from "@/components/layout/PageHeader";

import EmptyState from "@/components/shared/EmptyState";
import ErrorState from "@/components/shared/ErrorState";
import LoadingPage from "@/components/shared/LoadingPage";

import RoomServiceForm from "../components/RoomServiceForm";
import { useCreateOrder } from "../hooks/useCreateOrder";
import { useMenu } from "../hooks/useMenu";

export default function RoomServicePage() {
  const { token = "" } = useParams();

  const mutation = useCreateOrder(token);
  const { data, isLoading, isError, refetch } = useMenu(token);

  if (isLoading) return <LoadingPage />;

  if (isError) return <ErrorState onRetry={refetch} />;

  if (!data?.length)
    return (
      <EmptyState
        title="Menu unavailable"
        description="Please contact reception."
      />
    );

  return (
    <>
      <PageHeader
        title="Room Service"
        description="Order food and beverages."
      />

      <PageContainer>
        <RoomServiceForm
          menu={data}
          isPending={mutation.isPending}
          onSubmit={(values) => mutation.mutate(values)}
        />
      </PageContainer>
    </>
  );
}
