from abc import ABC, abstractmethod
from app.models import Receipt
from flask import g
from datetime import datetime
import math

class Rule(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    @abstractmethod
    def handle(self, receipt: Receipt):
        # print(f'Receipt points: {receipt.points}')
        if self._successor:
            self._successor.handle(receipt)


class AlphaNumericCharInRetailerNameRule(Rule):
    def handle(self, receipt):
        """
        One point for every alphanumeric character in the retailer name.
        """
        points = 0
        for char in receipt.retailer:
            if char.isalnum():
                points += 1
        receipt.points += points

        super().handle(receipt)

class TotalIsRoundDollarAmountRule(Rule):
    def handle(self, receipt):
        """
        50 points if the total is a round dollar amount with no cents.
        """
        if receipt.total.is_integer():
            receipt.points += 50
        super().handle(receipt)

class TotalIsMultipleOfQuarterRule(Rule):
    def handle(self, receipt):
        """
        25 points if the total is a multiple of 0.25
        """
        is_multiple = lambda x: x % 0.25 == 0
        if is_multiple(receipt.total):
            receipt.points += 25
        super().handle(receipt)

class FivePointsForEveryTwoItemsRule(Rule):
    def handle(self, receipt):
        """
        5 points for every two items on the receipt.
        """
        noOfItems = len(receipt.items)
        while noOfItems >= 2:
            receipt.points += 5
            noOfItems -= 2
        super().handle(receipt)

class TrimmedDescriptionLenIsMultipleofThreeRule(Rule):
    def handle(self, receipt):
        """
        If the trimmed length of the item description is a multiple of 3,
        multiply the price by 0.2 and round up to the nearest integer.
        The result is the number of points earned.
        """
        for item in receipt.items:
            if len(item.shortDescription) % 3 == 0:
                points = item.price * 0.2
                points = math.ceil(points)
                receipt.points += points
        super().handle(receipt)

class PurchaseDateOddRule(Rule):
    def handle(self, receipt):
        """
        6 points if the day in the purchase date is odd.
        """
        date_format = "%Y-%m-%d"
        date = datetime.strptime(receipt.purchaseDate, date_format)
        if date.day % 2 == 1:
            receipt.points += 6
        super().handle(receipt)

class TimeBetweenTwoAndFourPMRule(Rule):
    def handle(self, receipt):
        """
        10 points if the time of purchase is after 2:00pm and before 
        4:00pm.
        """
        date_format = "%H:%M"
        date = datetime.strptime(receipt.purchaseTime, date_format)
        if 60 * 14 < date.hour * 60 + date.minute < 60 * 16:
            receipt.points += 10
        super().handle(receipt)


rulesHandler: Rule = None

def calculate_points(receipt: Receipt) -> float: 
    if 'rulesHandler' not in g:
        g.rulesHandler = AlphaNumericCharInRetailerNameRule()
        rule2 = TotalIsRoundDollarAmountRule()
        rule3 = TotalIsMultipleOfQuarterRule()
        rule4 = FivePointsForEveryTwoItemsRule()
        rule5 = TrimmedDescriptionLenIsMultipleofThreeRule()
        rule6 = PurchaseDateOddRule()
        rule7 = TimeBetweenTwoAndFourPMRule()

        g.rulesHandler.set_successor(rule2)
        rule2.set_successor(rule3)
        rule3.set_successor(rule4)
        rule4.set_successor(rule5)
        rule5.set_successor(rule6)
        rule6.set_successor(rule7)

    g.rulesHandler.handle(receipt)
    return receipt.points
