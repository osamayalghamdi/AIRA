# backend/fastapi/models/user.py

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    firebase_uid = Column(String(128), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    display_name = Column(String(100), nullable=True)
    role = Column(String(50), default='user')
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    organization_id = Column(Integer, ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    assigned_tickets = relationship("Ticket", foreign_keys="[Ticket.assigned_agent_uid]", back_populates="assigned_agent")
    organization = relationship("Organization", back_populates="users")