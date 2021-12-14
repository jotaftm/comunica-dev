class InvalidCPFError(Exception):
    def __init__(self, message="The CPF must be numbers only.", code=400):
        self.message = message
        self.code = code


class InvalidEmailError(Exception):
    def __init__(self, message="Email format must be name@domain.com or name@domain.com.xx"):
        self.message = message


class LeadExistsError(Exception):
    def __init__(self, message="Lead already exists."):
        self.message = message


class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid):
        self.message = f"{key} must be of the {type_valid} type, and was sent as {type_send}."


class InvalidZipCodeError(Exception):
    def __init__(self, value):
        self.message = f"Zip code must have 8 digits, but {len(value)} was sent."


class InvalidUser(Exception):
    def __init__(self, code=404):
        self.message = f"User is not found."
        self.code = code


class InvalidPassword(Exception):
    def __init__(self, code=401):
        self.message = f"Invalid password."
        self.code = code


class DataNotFound(Exception):
    def __init__(self, data):
        self.message = {"error": f'{data} not found.'}
        

class EmailVerifiedError(Exception):
    def __init__(self,message="Failed to verify email", code=401):
        self.message = message
        self.code = code
