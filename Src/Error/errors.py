class MissingParameterError(Exception): #Argument -> Exception-Klasse
    def __init__(self, message: str): #Konstruktor -> Message als String
        self.message = message

class DuplicateParameterError(Exception): #Argument -> Exception-Klasse
    def __init__(self, message: str): #Konstruktor -> Message als String
        self.message = message
