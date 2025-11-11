import uuid
def uid() -> str:
    return uuid.uuid4().hex
