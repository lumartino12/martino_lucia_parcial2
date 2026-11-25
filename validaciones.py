
def validar_entero(texto: str) -> bool:
    """
    Valida que el dato ingresado esté conformado únicamente por números
    """
    if len(texto) == 0:
        return False

    for i in range(len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            return False

    return True


def validar_dni(dni: str, registros: dict) -> bool:
    """
    Valida que el dni no esté registrado en el diccionario
    """
    return dni not in registros


def pedir_dni() -> str:
    """
    Solicita y valida el dni del alumno
    """
    dni = input("Ingrese el DNI del alumno: ")

    while validar_entero(dni) == False:
        print("Error. El DNI debe contener únicamente números.")
        dni = input("Ingrese nuevamente el DNI del alumno: ")

    return dni


def validar_nombre(nombre: str) -> bool:
    """
    Valida que el nombre o apellido esté formado únicamente por letras y espacios
    """
    tiene_letras = False

    for i in range(len(nombre)):
        caracter = nombre[i]

        if ("a" <= caracter <= "z") or ("A" <= caracter <= "Z"):
            tiene_letras = True

        elif caracter != " ":
            return False

    return tiene_letras


def pedir_nombre() -> str:
    """
    Solicita el nombre del alumno y valida el dato ingresado
    """
    nombre = input("Ingrese el nombre del alumno: ")

    while validar_nombre(nombre) == False:
        print("Error. El nombre debe contener únicamente letras y espacios, y no puede estar vacío.")
        nombre = input("Ingrese nuevamente el nombre del alumno: ")

    return nombre


def pedir_apellido() -> str:
    """
    Solicita el apellido del alumno y valida el dato ingresado
    """
    apellido = input("Ingrese el apellido del alumno: ")

    while validar_nombre(apellido) == False:
        print("Error. El apellido debe contener únicamente letras y espacios, y no puede estar vacío.")
        apellido = input("Ingrese nuevamente el apellido del alumno: ")

    return apellido


def validar_edad(edad: str) -> bool:
    """
    Valida que la edad ingresada sea un número entero y sea mayor a 18
    """
    if validar_entero(edad) == False:
        return False

    edad = int(edad)

    if edad <= 18:
        return False

    return True


def pedir_edad() -> int:
    """
    Solicita la edad del alumno y verifica que cumpla con las condiciones establecidas
    """
    edad = input("Ingrese la edad del alumno: ")

    while validar_edad(edad) == False:
        print("Error. La edad debe ser un número entero mayor a 18.")
        edad = input("Ingrese nuevamente la edad del alumno: ")

    return int(edad)


def validar_nota(nota: str) -> bool:
    """
    Valida que la nota ingresada sea un número entero entre 0 y 10 inclusive
    """
    if validar_entero(nota) == False:
        return False

    nota = int(nota)

    if nota < 0 or nota > 10:
        return False

    return True


def pedir_nota() -> int:
    """
    Solicita la nota final del alumno y verifica que cumpla con las condiciones establecidas
    """
    nota = input("Ingrese la nota final del alumno: ")

    while validar_nota(nota) == False:
        print("Dato no válido. Sólo se permiten números enteros entre 0 y 10.")
        nota = input("Ingrese nuevamente la nota final del alumno: ")

    return int(nota)
