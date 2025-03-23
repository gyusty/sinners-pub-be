from typing import List
from fastapi import APIRouter, HTTPException
from app.repositories.Item import Item
from app.repositories.Order import Order
from pydantic import BaseModel
from app.services.stock_service import validate_and_update_stock

router = APIRouter()
items = []
orders = []
repository = Item(items)
orderList = Order(orders)

class ItemCreate(BaseModel):
    quantity: int
    unit_price: float
    name: str
    
class OrderCreate(BaseModel):
    itemList: List[dict]
    owner: str
    
class OrderUpdateInput(BaseModel):
    owner: str
    itemList: List[dict]
    isPaid: bool = False
     

@router.get("/stock")
def get_stock():
    return repository.all()

@router.post("/stock")
def create_item(item: ItemCreate):
    try:
        new_item = repository.create(item.model_dump())
        return {"message": "Item created successfully", "item": new_item}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/order")
def get_orders():
    return orderList.all()

@router.post("/order")
def create_order(order: OrderCreate):
    try:
        order.itemList = [item for item in order.itemList if item.get("canUpdate") is True]
        validate_and_update_stock(order.itemList, repository)
        new_order = orderList.create(order.model_dump())
        return {"message": "Order created successfully", "item": new_order}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/order/{order_id}")
def update_order(order_id: str, order: OrderUpdateInput):
    try:
        if not order.isPaid:
            validate_and_update_stock(order.itemList, repository)
        updated_order = orderList.update_order(order_id, order.itemList, order.isPaid)
        if not updated_order:
            raise HTTPException(status_code=404, detail="Order not found")
        return {"message": "Order updated successfully", "order": updated_order}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))