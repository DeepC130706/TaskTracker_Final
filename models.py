from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path
DB_URL = "sqlite:///tasktracker_final.db"
engine = create_engine(DB_URL, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    difficulty = Column(Integer)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
    actual_time = Column(Float, nullable=True)

def init_db():
    Base.metadata.create_all(bind=engine)
