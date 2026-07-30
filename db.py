from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

CONNECTION_STRING = (
    "mssql+pyodbc://@ABI-LENOVO/CODE-GENERATOR-DB"
    "?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
)

engine = create_engine(CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
