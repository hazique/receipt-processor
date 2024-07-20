from app.models import Item, Receipt

def test_item_model():
    # Create a user instance
    item = Item(**{"shortDescription": "Mountain Dew 12PK", "price": "6.49"})

    # Test the attributes of the user instance
    assert item.shortDescription == 'Mountain Dew 12PK'
    assert item.price == 6.49
    