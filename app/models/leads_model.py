from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from datetime import datetime


@dataclass
class Leads(db.Model):
    __tablename__ = "leads_table"

    id: int
    name: str
    email:str
    phone:str
    creation_date:str
    last_visit:str
    visits: int
    

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.now())
    last_visit = Column(DateTime, default=datetime.now())
    visits = Column(Integer, nullable=True, default=1)
    