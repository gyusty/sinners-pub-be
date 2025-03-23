from app.interfaces.item import IItem 
from app.domain.item import Item as item_entity
class Item(IItem):
    def __init__(self, items):
        self.__items = items
    def all (self):
        return self.__items
    def find(self, name):
        for item in self.__items:
            if item.name == name:
                return item
        return None
    def create(self, item):
        print(item)
        new_item = item_entity(item['quantity'], item['unit_price'], item['name'])
        self.__items.append(new_item)
        return self.__items
    def update_stock(self, name, delta_quantity):
        item = self.find(name)
        if not item:
            return None
        item.quantity += delta_quantity
        return item
    def delete_item(self, name):
        item = self.find(name)
        if not item:
            return None
        self.__items.remove(item)
        return item
    