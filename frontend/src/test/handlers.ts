// src/test/handlers.ts

import { http, HttpResponse } from "msw";

export const handlers = [
  http.post("/api/staff/auth/login/", async () => {
    return HttpResponse.json({
      access: "access-token",
      refresh: "refresh-token",
    });
  }),
  http.get(
    "http://127.0.0.1:8000/api/v1/public/engineering/services/:token/",
    ({ params }) => {
      // console.log(params);

      return HttpResponse.json([
        {
          id: 1,
          name: "Air Conditioning",
        },
        {
          id: 2,
          name: "Television",
        },
      ]);
    },
  ),
];
// http://127.0.0.1:8000/api/v1/public/engineering/services/:token/
