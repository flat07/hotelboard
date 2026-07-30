// frontend/src/features/engineering/pages/EngineeringPage.test.tsx

import { screen } from "@testing-library/react";
import { http, HttpResponse } from "msw";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { expect, it } from "vitest";

import { renderWithProviders } from "@/test/render";
import { server } from "@/test/server";
import EngineeringPage from "./EngineeringPage";

function renderPage() {
  return renderWithProviders(
    <MemoryRouter initialEntries={["/guest/abc123/engineering"]}>
      <Routes>
        <Route path="/guest/:token/engineering" element={<EngineeringPage />} />
      </Routes>
    </MemoryRouter>,
  );
}

it("renders engineering services", async () => {
  renderPage();

  expect(await screen.findByText("Air Conditioning")).toBeInTheDocument();

  expect(await screen.findByText("Television")).toBeInTheDocument();
});

it("shows empty state", async () => {
  server.use(
    http.get(
      "http://127.0.0.1:8000/api/v1/public/engineering/services/:token/",
      () => HttpResponse.json([]),
    ),
  );
  renderPage();

  expect(await screen.findByText(/no services available/i)).toBeInTheDocument();

  expect(screen.getByText(/please contact reception/i)).toBeInTheDocument();
});

it("shows error state", async () => {
  server.use(
    http.get(
      "http://127.0.0.1:8000/api/v1/public/engineering/services/:token/",
      () => new HttpResponse(null, { status: 500 }),
    ),
  );

  renderPage();

  expect(await screen.findByText(/something went wrong/i)).toBeInTheDocument();
});
