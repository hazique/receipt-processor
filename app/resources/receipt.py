from flask import request

from flask_restful import Resource
from app.models import Receipt
from app.services.points_calculator import calculate_points
from app.util import generate_unique_id
from app.schema.receipt_points import ReceiptPointsModel
from app.exceptions import InvalidReceiptException, InvalidReceiptIdException

class ReceiptPointsResource(Resource):
    def get(self, id):
        """
        Get points for a receipt by ID
        Args:
            id (str): 

        Returns:
            response (Response): HTTP Response
        """
        try:
            data: ReceiptPointsModel = ReceiptPointsModel.find_by_receipt_id(id)
        except InvalidReceiptIdException as e:
            return e.serialize()
        
        return {"points": data.receipt_points}, 200


class ReceiptProcessResource(Resource):
    def post(self):
        """
        Process the receipt received as JSON.
        Returns:
            response (Response): HTTP Response
        """
        data = request.get_json()
        try:
            receipt = Receipt(**data)
        except InvalidReceiptException as e:
            return e.serialize()
        
        receipt_id = generate_unique_id(receipt)
        
        try:
            data: ReceiptPointsModel = ReceiptPointsModel.find_by_receipt_id(receipt_id)
        except InvalidReceiptIdException:
            points = calculate_points(receipt)
            data = ReceiptPointsModel(receipt_id, points)
            data.save_to_db()

        return {"id": data.receipt_id}, 200