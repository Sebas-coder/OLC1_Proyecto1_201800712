from enum import Enum


class Tipo(Enum):
    # Errores
    CARACTERINVALIDO = 0
    ERERRONEA = 1
    NINGUNO = 2
    
class Error:
    tipoError = Tipo.NINGUNO
    lexema = ""
    fila = 0
    columna = 0
    def __init__(self, tipo, valor, fila, columna):
        self.tipoError = tipo
        self.lexema = valor
        self.fila = fila
        self.columna = columna