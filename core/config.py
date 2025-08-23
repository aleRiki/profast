import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/postgres")
SECRET_KEY = os.getenv("SECRET_KEY", "8f4e8c3b2a1d6e0f5d8a3b7c9e2a1d6f0b8c5d2a1f6e8d3c2b1a0f9e8d5c2a1b")
ALGORITHM = "HS256"
