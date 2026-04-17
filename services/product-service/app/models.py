from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Product(Base):
    __tablename__ = "products"

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)
    price    = Column(Float, nullable=False)
    stock    = Column(Integer, default=0)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
