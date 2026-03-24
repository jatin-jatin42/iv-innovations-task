import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import motor.motor_asyncio

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/erp_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB connection for Gen AI logs
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client["erp_ai_logs"]
mongo_collection = mongo_db["ai_generations"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
