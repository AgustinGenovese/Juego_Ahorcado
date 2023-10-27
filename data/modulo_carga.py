import json

def carga_json():
    """
    Carga datos desde un archivo JSON y los devuelve como un diccionario.
    Returns:
    dict: Un diccionario que contiene los datos cargados desde el archivo JSON.
    """
    with open("./data/data.json", "r") as file:
        return json.load(file)
 
def obtener_reglas(cargar_reglas):
    """
    Carga reglas desde un archivo CSV y pasa los datos a una función dada.
    Parameters:
    cargar_reglas (function): Una función que acepta los datos cargados  desde el archivo CSV.
    """
    with open('./data/reglas.csv', 'r') as archivo:
        cargar_reglas(archivo)