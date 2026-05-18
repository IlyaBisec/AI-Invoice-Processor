# Database layer.
# Handles:
# - database connection
# - session management
# - base ORM class
# 18.05.2026 (c) ilya_bisec

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from aip.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()