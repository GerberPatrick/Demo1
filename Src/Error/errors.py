class MissingParameterError(Exception):
    def __init__(self, message: str):
        self.message = message

class DuplicateParameterError(Exception):
    def __init__(self, message: str):
        self.message = message
