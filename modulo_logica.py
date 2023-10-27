import random
import re
from excepciones.excepciones import  *

def obtener_tema(temas: dict):
    """
     Obtiene aleatoriamente un tema de un diccionario que contiene listas de palabras.
    Parameters:
        temas (dict): Un diccionario donde las claves son los temas y los valores son listas de palabras asociadas a cada tema.
    Returns:
        str: Un tema aleatorio seleccionado del diccionario.
    """
    
    claves = list(temas.keys())              
    tema_aleatorio = random.choice(claves)
    return tema_aleatorio

def obtener_palabra(temas: dict, clave: str):
    """
    Obtiene aleatoriamente una palabra en mayúsculas de una lista de palabras asociada a una clave en un diccionario de temas.
    Parameters:
        temas (dict): Un diccionario donde las claves son los temas y los valores son listas de palabras asociadas a cada tema.
        clave (str): La clave que identifica el tema del cual se seleccionará una palabra aleatoria.
    Returns:
        str: Una palabra aleatoria en mayúsculas seleccionada de la lista de palabras asociada a la clave especificada.
    """
    lista_de_palabras = temas[clave]
    palabra = random.choice(lista_de_palabras)
    palabra = palabra.upper()
    return palabra

def validar_letras(lista_letras:list,letra:str):
    """
     Valida una letra en función de dos condiciones:
        1. Si la entrada es una letra.
        2. Si la letra no está repetida en una lista.

    Parameters:
    letra (str): La letra que se va a validar.
    lista_letras (list): Una lista de letras en la que se verificará si la letra ya está presente.

    Returns:
    bool: True si la letra es válida según las condiciones especificadas.

    Raises:
    NoEsLetraException: Se lanza si la entrada no es una letra.
    EstaRepetidoException: Se lanza si la letra ya está presente en la lista.
    """

    if not letra.isalpha():
        raise NoEsLetraException
    if letra.upper() in (lista_letras):
        raise EstaRepetidoException
    return True


def reemplazar_letras(palabra:str, lista_letras_presionadas:list):
    """
    Reemplaza las letras no adivinadas de una palabra con guiones bajos (_) y devuelve la palabra oculta.
    Parameters:
        palabra (str): La palabra que se debe ocultar, reemplazando las letras no adivinadas con guiones bajos.
        lista_letras (list): Una lista de letras presionadas
    Returns:
        str: La palabra oculta con las letras no adivinadas reemplazadas por guiones bajos (_).
    """
    abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
    palabra_oculta = palabra     #importante
    for letra_abecedario in abecedario:
        if letra_abecedario not in lista_letras_presionadas:
                palabra_oculta = re.sub(letra_abecedario, "_", palabra_oculta)
        else:
            pass
    return palabra_oculta

def validador_start(tecla:str):
    """
    Valida si se presiona la tecla "Enter"y lanza una excepción si no se cumple.
    Parameters: tecla (str): La tecla presionada que se va a validar.

    Returns: bool: True si se presionó la tecla "Enter" exitosamente.

 Raises: NoPresionaEnterException: Se lanza si la tecla no es igual a "return" (Enter).

    """
    if not tecla == "return":       
        raise NoPresionaEnterException() ## finaliza en esta linea por la excepcion 
    return True

    
    



