from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# El parámetro sslmode lo necesito para que Deta se conecte a la BBDD en Neon
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'sslmode': "allow"})

#if you don't want to install postgres or any database, use sqlite, a file system based database, 
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print("No se ha podido establecer conexión con la BBDD")
        print(e)
    finally:
        db.close()