from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
base = declarative_base()
