import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";

import EngineeringForm from "./EngineeringForm";

const services = [
  {
    id: 1,
    name: "Air Conditioning",
  },
  {
    id: 2,
    name: "Television",
  },
];
it("renders all services", () => {
  render(
    <EngineeringForm
      services={services}
      isPending={false}
      onSubmit={vi.fn()}
    />,
  );

  expect(screen.getByText("Air Conditioning")).toBeInTheDocument();
  expect(screen.getByText("Television")).toBeInTheDocument();

  expect(
    screen.getByPlaceholderText(/describe the issue/i),
  ).toBeInTheDocument();

  expect(
    screen.getByRole("button", {
      name: /submit request/i,
    }),
  ).toBeInTheDocument();
});

it("allows selecting services", async () => {
  const user = userEvent.setup();

  render(
    <EngineeringForm
      services={services}
      isPending={false}
      onSubmit={vi.fn()}
    />,
  );

  const checkboxes = screen.getAllByRole("checkbox");

  await user.click(checkboxes[0]);

  expect(checkboxes[0]).toBeChecked();
});
it("submits selected services and note", async () => {
  const user = userEvent.setup();

  const onSubmit = vi.fn();

  render(
    <EngineeringForm
      services={services}
      isPending={false}
      onSubmit={onSubmit}
    />,
  );

  await user.click(screen.getAllByRole("checkbox")[0]);

  await user.type(
    screen.getByPlaceholderText(/describe the issue/i),
    "The AC is leaking water.",
  );

  await user.click(
    screen.getByRole("button", {
      name: /submit request/i,
    }),
  );

  expect(onSubmit).toHaveBeenCalledTimes(1);

  expect(onSubmit.mock.calls[0][0]).toEqual({
    service_ids: [1],
    note: "The AC is leaking water.",
  });
});
it("disables submit button while pending", () => {
  render(
    <EngineeringForm services={services} isPending={true} onSubmit={vi.fn()} />,
  );

  expect(
    screen.getByRole("button", {
      name: /submit request/i,
    }),
  ).toBeDisabled();
});
