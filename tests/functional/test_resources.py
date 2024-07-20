

def test_new_receipt(test_client):
    # Test getting a non-existing subscription
    # Use the subscription_resource fixture to access the SubscriptionResource instance
    # Perform the necessary assertions to verify the behavior
    json = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
        ],
        "total": "35.35",
    }
    response = test_client.post("/receipts/process", json=json)
    assert response.status_code == 200