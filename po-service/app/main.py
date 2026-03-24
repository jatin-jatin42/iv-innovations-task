from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database, ai_service

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="PO Service API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products", response_model=List[schemas.ProductSchema])
def get_products(db: Session = Depends(database.get_db)):
    return db.query(models.Product).all()

@app.get("/products/{product_id}", response_model=schemas.ProductSchema)
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/po", response_model=schemas.POResponse)
def create_po(po_in: schemas.POCreate, db: Session = Depends(database.get_db)):
    db_po = models.PurchaseOrder(
        reference_no=po_in.reference_no,
        vendor_id=po_in.vendor_id,
        status="Pending"
    )
    db.add(db_po)
    db.flush() # get id

    subtotal = 0.0

    for item in po_in.items:
        db_item = models.PurchaseOrderItem(
            po_id=db_po.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price
        )
        db.add(db_item)
        subtotal += (item.quantity * item.unit_price)

    # Business Logic: Apply 5% tax
    tax = subtotal * 0.05
    total_amount = subtotal + tax
    
    db_po.total_amount = total_amount

    db.commit()
    db.refresh(db_po)

    # Attempt to notify via notification-service (Bonus)
    import requests
    try:
        requests.post("http://notification-service:3000/notify", json={"po_id": db_po.id, "status": db_po.status})
    except Exception:
        pass # Optional so not fatal if down

    return db_po

@app.get("/po", response_model=List[schemas.POResponse])
def get_pos(db: Session = Depends(database.get_db)):
    return db.query(models.PurchaseOrder).all()

@app.post("/generate-description")
async def generate_product_description(req: schemas.GenerateDescriptionRequest):
    return await ai_service.generate_description(req.product_name, req.category)
