// frontend/src/features/housekeeping/pages/HousekeepingPage.tsx

import { useParams } from "react-router-dom";

import PageContainer from "@/components/layout/PageContainer";
import PageHeader from "@/components/layout/PageHeader";
import EmptyState from "@/components/shared/EmptyState";
import ErrorState from "@/components/shared/ErrorState";
import LoadingPage from "@/components/shared/LoadingPage";

import HousekeepingForm from "../components/HousekeepingForm";
import { useCreateHousekeepingRequest } from "../hooks/useCreateHousekeepingRequest";
import { useHousekeepingServices } from "../hooks/useHousekeepingServices";

export default function HousekeepingPage() {
  const { token = "" } = useParams();

  const mutation = useCreateHousekeepingRequest(token);

  const { data, isLoading, isError, refetch } = useHousekeepingServices(token);

  if (isLoading) return <LoadingPage />;

  if (isError) return <ErrorState onRetry={refetch} />;

  if (!data?.length)
    return (
      <EmptyState
        title="No services available"
        description="Please contact reception."
      />
    );

  return (
    <>
      <PageHeader
        title="Housekeeping"
        description="Select the services you need."
      />

      <PageContainer>
        <HousekeepingForm
          services={data}
          isPending={mutation.isPending}
          onSubmit={(values) => mutation.mutate(values)}
        />
      </PageContainer>
    </>
  );
}
