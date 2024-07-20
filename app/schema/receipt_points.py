from sqlalchemy import event
from app import db

class ReceiptPointsModel(db.Model):
    """
    Class that represents a ReceiptPoints.

    The following attributes of a user are stored in this table:
        * receipt_id - id of receipt. Mapped to receipt object in the NoSQL store
        * receipt_points - total points calculated for the receipt

    REMEMBER: Never store the plaintext password in a database!
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
        return cls.query.filter_by(receipt_id=receipt_id).first()

# @event.listens_for(SubscriptionModel.__table__, 'after_create')
# def create_subscriptions(*args, **kwargs):
#     db.session.add(SubscriptionModel(user_id=1, industry='Technology', source='TechCrunch', subcategory='Latest'))
#     db.session.add(SubscriptionModel(user_id=2, industry='Technology', source='TechCrunch', subcategory='Latest'))  
#     db.session.commit()