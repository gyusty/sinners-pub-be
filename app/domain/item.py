class Item:
    def __init__(self, quantity: int, unit_price: float, name: str, canUpdate: bool = True):
        self.quantity = quantity
        self.unit_price = unit_price
        self.name = name
        self.canUpdate = canUpdate