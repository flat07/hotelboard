// frontend/src/lib/axios.ts

import { API_BASE_URL } from "@/config/api";
import { getAccessToken } from "@/features/auth/utils/token";
import axios from "axios";

export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  const token = getAccessToken();

  const isPublic = config.url?.startsWith("/public/");

  if (token && !isPublic) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (!error.response) {
      return Promise.reject(new Error("Network Error"));
    }

    switch (error.response.status) {
      case 400:
        return Promise.reject(new Error("Bad Request"));

      case 404:
        return Promise.reject(new Error("Not Found"));

      case 500:
        return Promise.reject(new Error("Server Error"));

      default:
        return Promise.reject(error);
    }
  },
);
