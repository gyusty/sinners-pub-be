from app.interfaces.order import IOrder
from app.domain.order import Order as order_entity
import uuid
from datetime import datetime
class Order(IOrder):
    def __init__(self, orders):
        self.__orders = orders
    def find(self, id):
        for order in self.__orders:
            if str(order.id) == str(id):
                return order
        return None
    def create(self, order):
        id = uuid.uuid4()
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = sum(item['unit_price'] * item['quantity'] for item in order['itemList'])
        
        new_order = order_entity(id, order['owner'],created, False, total, 0, 0, order['itemList'])
        self.__orders.append(new_order)
        return self.__orders
    def update_order(self, id, itemList, isPaid):
        order = self.find(id)
        if order:
            order.itemList = itemList
            order.total = sum(item['unit_price'] * item['quantity'] for item in itemList)
            order.isPaid = isPaid
        return self.__orders
    def all (self):
        return self.__orders