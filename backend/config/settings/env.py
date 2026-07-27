# backend/config/env.py
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROJECT_DIR = BASE_DIR.parent
ENV_FILE = os.getenv("ENV_FILE", ".env.development")

ENV_PATH = PROJECT_DIR / ENV_FILE


load_dotenv(ENV_PATH)


def env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Environment variable '{name}' is missing.")
    return value


def env_list(name: str) -> list[str]:
    return [item.strip() for item in env(name).split(",") if item.strip()]
