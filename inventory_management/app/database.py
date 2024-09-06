from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://book_inventory_user:ZKvfpDLKgYeEOd4SfCZ8XzDrYdYW9vjy@dpg-crd60n3tq21c73cu0rm0-a.oregon-postgres.render.com/book_inventory"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
