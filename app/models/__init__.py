from dataclasses import dataclass

@dataclass
class Item:
    short_description: str
    price: float

@dataclass
class Receipt:
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: int
    total: float
