class InvalidCPFError(Exception):
    def __init__(self, message="The CPF must be numbers only.", code=400):
        self.message = message
        self.code = code


class InvalidEmailError(Exception):
    def __init__(self, message="Email format must be name@domain.com or name@domain.com.xx", code=400):
        self.message = message
        self.code = code


class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid, code=400):
        self.message = f"{key} must be of the {type_valid} type, and was sent as {type_send}."
        self.code = code


class InvalidZipCodeError(Exception):
    def __init__(self, value, code=400):
        self.message = f"Zip code must have 8 digits, but {len(value)} was sent."
        self.code = code


class InvalidUser(Exception):
    def __init__(self, code=404):
        self.message = f"User is not found."
        self.code = code


class InvalidPassword(Exception):
    def __init__(self, code=401):
        self.message = f"Invalid password."
        self.code = code