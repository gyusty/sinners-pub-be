# app/services/stock_service.py
from fastapi import HTTPException
from typing import List
from app.repositories.Item import Item

def validate_and_update_stock(order_items: List[dict], repository: Item):
    
    for ordered_item in order_items:
        if not ordered_item.get('canUpdate', False):
            continue

        item_name = ordered_item['name']
        ordered_quantity = ordered_item['quantity']
        
        stock_item = repository.find(item_name)
        if not stock_item:
            raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found in stock")
        if stock_item.quantity < ordered_quantity:
            raise HTTPException(status_code=400, detail=f"Not enough stock for item '{item_name}'")

    for ordered_item in order_items:
        if ordered_item.get('canUpdate', False):
            repository.update_stock(ordered_item['name'], -ordered_item['quantity'])
            updated_item = repository.find(ordered_item['name'])

            if updated_item and updated_item.quantity <= 0:
                print(f"Removing item: {ordered_item['name']} from stock (quantity is 0 or less)")
                repository.delete_item(ordered_item['name'])

