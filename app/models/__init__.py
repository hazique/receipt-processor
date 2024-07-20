import dataclasses
from dataclasses import dataclass
from typing import List
from app.exceptions import InvalidReceiptException
@dataclass
class Item:
    shortDescription: str
    price: float

    def __init__(self, **data):
        for key, val in data.items():
            if key == 'shortDescription':
                self.shortDescription = val.strip()
            
            elif key == 'price':
                self.price = float(val.strip())

            else:
                raise InvalidReceiptException
@dataclass
class Receipt:
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[Item]
    total: float
    points: int

    def __init__(self, **data):
        self.points = 0

        for key, val in data.items():
            if key == 'retailer':
                self.retailer = val.strip()

            elif key == 'purchaseDate':
                self.purchaseDate = val.strip()

            elif key == 'purchaseTime':
                self.purchaseTime = val.strip()

            elif key == 'total':
                self.total = float(val.strip())

            elif key == 'items':
                self.items = list(map(lambda x: Item(**x), val))

            else:
                raise InvalidReceiptException
            
        fields = dataclasses.fields(self)
        for field in fields:
            if field.name != 'points' and field.name not in data:
                raise InvalidReceiptException
            
