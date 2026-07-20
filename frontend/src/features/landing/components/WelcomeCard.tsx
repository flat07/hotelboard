// frontend/src/features/landing/components/WelcomeCard.tsx

import { Card, CardContent } from "@/components/ui/card";

export default function WelcomeCard() {
  return (
    <Card>
      <CardContent className="space-y-2 p-5">
        <h1 className="text-2xl font-bold">Welcome 👋</h1>

        <p className="text-sm text-muted-foreground">
          Select one of the hotel services below.
        </p>
      </CardContent>
    </Card>
  );
}
