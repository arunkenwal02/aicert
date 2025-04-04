from sqlalchemy import Column, Integer, DateTime, func, String
from sqlalchemy.ext.declarative import declared_attr
from database import Base, engine

class TimestampMixin:
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    

class Document(TimestampMixin, Base):
    __tablename__ = "document"
    name = Column(String(255), unique=True, nullable=False)  
    type = Column(String(100), nullable=False)  


Base.metadata.create_all(bind=engine)
