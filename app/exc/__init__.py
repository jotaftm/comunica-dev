class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid, code=400):
        self.message = f"{key} must be of the {type_valid} type, and was sent as {type_send}."
        self.code = code

class InvalidZipCodeLenError(Exception):
    ...