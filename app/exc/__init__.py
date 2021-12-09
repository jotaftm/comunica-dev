class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid, code=400):
        self.message = f"{key} must be of the {type_valid} type, and was sent as {type_send}."
        self.code = code

class InvalidZipCodeError(Exception):
    def __init__(self, value, code=400):
        self.message = f"Zip code must have 8 digits, but {len(value)} was sent."
        self.code = code