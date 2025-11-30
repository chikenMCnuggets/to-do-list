from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)

    notes = relationship("Note", back_populates = "owner", cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<Category(id={self.id}), name(name={self.name}) >"

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True, nullable = False, index = True)
    text = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    created_at = Column(DateTime, default = datetime.utcnow)

    owner = relationship("User", back_populates = "notes")

    def __repr__(self):
        return f"<Category(id={self.id}), name(name={self.name}), text(text={self.text}))>"

