from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    sku = Column(String(100), unique=True, index=True, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    stock_level = Column(Integer, nullable=False)

class PurchaseOrder(Base):
    __tablename__ = "purchaseorders"

    id = Column(Integer, primary_key=True, index=True)
    reference_no = Column(String(100), unique=True, index=True, nullable=False)
    vendor_id = Column(Integer) # Linked to Vendor Service
    total_amount = Column(Numeric(10, 2), default=0)
    status = Column(String(50), default="Pending")

    items = relationship("PurchaseOrderItem", back_populates="po", cascade="all, delete-orphan")

class PurchaseOrderItem(Base):
    __tablename__ = "purchaseorderitems"

    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchaseorders.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)

    po = relationship("PurchaseOrder", back_populates="items")
