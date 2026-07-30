// src/test/setup.ts

import "@testing-library/jest-dom/vitest";

import { afterAll, afterEach, beforeAll, vi } from "vitest";

import { server } from "./server";

beforeAll(() => server.listen());

// beforeAll(() =>
//   server.listen({
//     onUnhandledRequest: "error",
//   }),
// );
afterEach(() => server.resetHandlers());

afterAll(() => server.close());

// Polyfill ResizeObserver for Radix UI
class ResizeObserverMock {
  observe() {}
  unobserve() {}
  disconnect() {}
}

vi.stubGlobal("ResizeObserver", ResizeObserverMock);
