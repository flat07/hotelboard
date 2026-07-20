// frontend/src/features/auth/components/LoginForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { loginSchema, type LoginSchema } from "../schemas/loginSchema";

interface Props {
  isPending: boolean;
  onSubmit: (data: LoginSchema) => void;
}

export default function LoginForm({ isPending, onSubmit }: Props) {
  const form = useForm<LoginSchema>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      username: "",
      password: "",
    },
  });

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-5">
      <Input placeholder="Username" {...form.register("username")} />

      <Input
        type="password"
        placeholder="Password"
        {...form.register("password")}
      />

      <Button className="w-full" disabled={isPending}>
        Login
      </Button>
    </form>
  );
}
