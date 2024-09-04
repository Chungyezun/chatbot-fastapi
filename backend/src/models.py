from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import Column
from .database import Base
from pydantic import BaseModel

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description= Column(String, nullable=False)

