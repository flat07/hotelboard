// frontend/src/contexts/AuthContext.tsx

import {
  createContext,
  useContext,
  useEffect,
  useState,
  type PropsWithChildren,
} from "react";

import { me } from "@/features/auth/api/me";
import type { User } from "@/features/auth/types";
import {
  clearTokens,
  getAccessToken,
  setTokens,
} from "@/features/auth/utils/token";

interface AuthContextType {
  user: User | null;
  loading: boolean;
  isAuthenticated: boolean;
  login: (access: string, refresh: string) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<User | null>(null);

  const [loading, setLoading] = useState(true);

  async function refreshUser() {
    const data = await me();

    setUser(data);
  }

  async function login(access: string, refresh: string) {
    setTokens(access, refresh);

    await refreshUser();
  }

  function logout() {
    clearTokens();

    setUser(null);
  }

  useEffect(() => {
    async function initialize() {
      const token = getAccessToken();

      if (!token) {
        setLoading(false);
        return;
      }

      try {
        await refreshUser();
      } catch {
        logout();
      } finally {
        setLoading(false);
      }
    }

    initialize();
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated: !!user,
        login,
        logout,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used inside AuthProvider");
  }

  return context;
}
