from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Date,
    Text,
    ForeignKey,
    Boolean,
    TIMESTAMP,
)
from sqlalchemy.sql import func
from .database import Base


class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location_code = Column(String(50), unique=True)
    address = Column(Text)


class SalesData(Base):
    __tablename__ = "sales_data"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    date = Column(Date, nullable=False)
    product_name = Column(String(100))
    quantity_sold = Column(Integer)
    total_sales = Column(Numeric(10, 2))
    delivery_platform = Column(String(50))
    source_file = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    review_date = Column(Date)
    platform = Column(String(50))
    rating = Column(Numeric(2, 1))
    comment = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())


class WeeklyReport(Base):
    __tablename__ = "weekly_reports"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    week_start = Column(Date)
    week_end = Column(Date)
    report_type = Column(String(50))  # "owner" or "store"
    report_text = Column(Text)
    generated_by_ai = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
