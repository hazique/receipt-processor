import hashlib
import uuid

def generate_unique_id(obj):
    # Serialize the object's attributes to a string
    serialized_str = str(obj.__dict__)
    
    # Create a hash from the serialized string
    hash_obj = hashlib.md5(serialized_str.encode())
    
    # Generate a UUID based on the hash
    unique_id = uuid.UUID(hash_obj.hexdigest())
    
    return str(unique_id)