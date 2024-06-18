import uuid
import hashlib


# Generate UUID v4
def gen_uuid():
    return str(uuid.uuid4()).replace("-", "")


# Generate SHA256 hash of a string
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()
