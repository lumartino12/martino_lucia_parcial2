import json


def cargar_archivo() -> dict:
    """
    Lee el archivo JSON y retorna el diccionario
    de alumnos registrados.
    """
    with open("alumnos.json", "r", encoding="utf-8") as archivo:
        registros = json.load(archivo)

    return registros


def guardar_archivo(registros: dict) -> None:
    """
    Guarda el diccionario de alumnos actualizado
    en el archivo JSON.
    """
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, indent=4)