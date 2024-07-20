from app import db
from app.exceptions import InvalidReceiptIdException

class ReceiptPointsModel(db.Model):
    """
    Class that represents a ReceiptPoints.

    The following attributes of a user are stored in this table:
        * receipt_id - id of receipt
        * receipt_points - total points calculated for the receipt
    """

    __tablename__ = 'receipt_points'

    receipt_id = db.Column(db.String, primary_key=True)
    receipt_points = db.Column(db.Integer)

    def __init__(self, receipt_id, receipt_points):
        self.receipt_id = receipt_id
        self.receipt_points = receipt_points

    def json(self):
        return {
            'receipt_id': self.receipt_id,
            'receipt_points': self.receipt_points,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self, receipt_points):
        self.receipt_points = receipt_points

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_receipt_id(cls, receipt_id):
        data = cls.query.filter_by(receipt_id=receipt_id).first()
        if not data:
            raise InvalidReceiptIdException
        return data
