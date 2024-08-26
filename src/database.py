import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv('.env.template')

db_url = os.getenv("DB_URL")

# Asegúrate de que db_url no es None
if db_url is None:
    raise ValueError("La URL de la base de datos no está definida en la variable de entorno DB_URL")

engine = create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
