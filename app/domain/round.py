from app.domain.item import Item
from typing import List

class Round:
    def __init__(self, created: str, items: List[Item]):
        self.created = created
        self.items = items