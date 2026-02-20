import os
from sqlmodel import create_engine, Session

DB_HOST = os.getenv("DB_HOST", "postgres-service.db-space.svc.cluster.local")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "hello_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session