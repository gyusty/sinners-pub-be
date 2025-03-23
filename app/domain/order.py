from typing import List
from app.domain.item import Item

class Order:
    def __init__(self, id:str, owner:str ,created: str, isPaid: bool, total: float, taxes: float, discounts: float, itemList: List[Item]):
        self.id = id
        self.owner = owner
        self.created = created
        self.isPaid = isPaid
        self.total = total
        self.taxes = taxes
        self.discounts = discounts
        self.itemList = itemList
        