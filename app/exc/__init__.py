from http import HTTPStatus


class InvalidCPFError(Exception):
    def __init__(self):
        self.message = {'error': 'The CPF must be numbers only.'}
        self.code = HTTPStatus.BAD_REQUEST


class InvalidEmailError(Exception):
    def __init__(self):
        self.message = {'error': 'Email format must be name@domain.com or name@domain.com.xx'}
        self.code = HTTPStatus.BAD_REQUEST


class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid):
        self.message = {'error': f'{key} must be of the {type_valid} type, and was sent as {type_send}.'}
        self.code = HTTPStatus.BAD_REQUEST


class InvalidZipCodeError(Exception):
    def __init__(self, value):
        self.message = {'error': f'Zip code must have 8 digits, but {len(value)} was sent.'}
        self.code = HTTPStatus.BAD_REQUEST


class InvalidPassword(Exception):
    def __init__(self):
        self.message = {'error': 'Invalid password.'}
        self.code = HTTPStatus.UNAUTHORIZED


class DataNotFound(Exception):
    def __init__(self, data):
        self.message = {'error': f'{data} not found.'}
        self.code = HTTPStatus.NOT_FOUND


class DataAlreadyRegistered(Exception):
    def __init__(self, data):
        self.message = {'error': f'{data} already exists.'}
        self.code = HTTPStatus.CONFLICT
        

class InvalidKey(Exception):
    def __init__(self, key):
        self.message = {'error': f'The key {key} is invalid.'}
        self.code = HTTPStatus.NOT_FOUND


class EmailVerifiedError(Exception):
    def __init__(self):
        self.message = {'error': 'Failed to verify email'}
        self.code = HTTPStatus.UNAUTHORIZED


class UnauthorizedAccessError(Exception):
    def __init__(self):
        self.message = {'error': 'No authorization to access this feature.'}
        self.code = HTTPStatus.UNAUTHORIZED
