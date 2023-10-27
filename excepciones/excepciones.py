class NoEsLetraException(Exception):
    def __init__(self, message='No se ingreso una letra'):
        self.message = message

class EstaRepetidoException(Exception):
    def __init__(self, message='La letra ingresada esta repetida'):
        self.message = message

class NoPresionaEnterException(Exception):
    def __init__(self, message='No se presiona enter'):
        self.message = message
     
## las clases no es letra y esta repetido, heredan de la clase madre excepcio,.
#por ese motivo se convierten en clases consideradas excepciones
# Al heredar, hereda todas sus funciones y variables como por ejemplo en este caso "message"
#que se esaria sobreescribiendo