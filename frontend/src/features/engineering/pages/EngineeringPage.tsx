// frontend/src/features/engineering/pages/EngineeringPage.tsx

import { useParams } from "react-router-dom";

import PageContainer from "@/components/layout/PageContainer";
import PageHeader from "@/components/layout/PageHeader";

import EmptyState from "@/components/shared/EmptyState";
import ErrorState from "@/components/shared/ErrorState";
import LoadingPage from "@/components/shared/LoadingPage";

import EngineeringForm from "../components/EngineeringForm";
import { useCreateEngineeringRequest } from "../hooks/useCreateEngineeringRequest";
import { useEngineeringServices } from "../hooks/useEngineeringServices";

export default function EngineeringPage() {
  const { token = "" } = useParams();

  const mutation = useCreateEngineeringRequest(token);

  const { data, isLoading, isError, refetch } = useEngineeringServices(token);

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
        title="Engineering"
        description="Report a maintenance issue."
      />

      <PageContainer>
        <EngineeringForm
          services={data}
          isPending={mutation.isPending}
          onSubmit={(values) => mutation.mutate(values)}
        />
      </PageContainer>
    </>
  );
}
