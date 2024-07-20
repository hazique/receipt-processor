from flask import Flask, request
from flask_restful import Resource
from app.models import Receipt
from app.services.points_calculator import calculate_points
from app.util import generate_unique_id
from app.schema.receipt_points import ReceiptPointsModel

class ReceiptPointsResource(Resource):
    def get(self, id):
        # Logic to get points for a receipt by ID
        return {"receipt_id": id, "points": 100}


class ReceiptProcessResouce(Resource):
    def post(self):
        # Logic to process a receipt
        data = request.get_json()
        receipt = Receipt(**data)
        receipt_id = generate_unique_id(receipt)
        
        data: ReceiptPointsModel = ReceiptPointsModel.find_by_receipt_id(receipt_id)
        if data is None:
            print("New receipt")
            points = calculate_points(receipt)
            data = ReceiptPointsModel(receipt_id, points)
            data.save_to_db()

        return {"message": "Receipt processed successfully", "data": data.receipt_id}