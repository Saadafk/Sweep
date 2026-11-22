from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.db import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    requester = Column(String(100), nullable=False)
    category = Column(String(20), default="other")
    priority = Column(String(10), default="medium")
    status = Column(String(20), default="open")
    created_at = Column(DateTime, default=datetime.now)