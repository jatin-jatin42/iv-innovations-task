from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    sku: str
    unit_price: float
    stock_level: int

class ProductCreate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int
    model_config = {"from_attributes": True}

class POItemBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class POCreate(BaseModel):
    reference_no: str
    vendor_id: int
    items: List[POItemBase]

class POItemResponse(POItemBase):
    id: int
    model_config = {"from_attributes": True}

class POResponse(BaseModel):
    id: int
    reference_no: str
    vendor_id: int
    total_amount: float
    status: str
    items: List[POItemResponse]

    model_config = {"from_attributes": True}

class GenerateDescriptionRequest(BaseModel):
    product_name: str
    category: Optional[str] = "Electronics"
