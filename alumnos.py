from validaciones import pedir_dni, validar_dni, pedir_nombre, pedir_apellido, pedir_edad, pedir_nota


def cargar_alumno(registros: dict) -> bool:
    """
    Registra un nuevo alumno en el diccionario, verificando que su dni no esté duplicado
    """
    dni = pedir_dni()

    while validar_dni(dni, registros) == False:
        print("Error. El DNI ya se encuentra registrado.")
        dni = pedir_dni()

    nombre = pedir_nombre()
    apellido = pedir_apellido()
    edad = pedir_edad()
    nota = pedir_nota()

    registros[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota_final": nota
    }

    print("Alumno registrado correctamente.")

    return True


def mostrar_alumno(dni: str, alumno: dict) -> None:
    """
    Muestra los datos del alumno
    """
    print(f"DNI: {dni}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Nota final: {alumno['nota_final']}")
    print(f"----------------------------------")


def listar_alumnos(registros: dict) -> None:
    """
    Muestra todos los alumnos registrados en el sistema
    """
    if len(registros) == 0:
        print("No hay alumnos registrados.")

    else:
        print("\nLISTADO DE ALUMNOS")
        print("--------------------------------")

        for dni in registros:
            mostrar_alumno(dni, registros[dni])


def buscar_alumno(registros: dict) -> None:
    """
    Busca un alumno mediante su dni y muestra sus datos si está registrado
    """
    dni = pedir_dni()

    if dni in registros:
        mostrar_alumno(dni, registros[dni])

    else:
        print("El alumno no se encuentra registrado.")


def mostrar_menu_modificacion() -> None:
    """
    Muestra las opciones disponibles para modificar los datos de un alumno
    """
    print("\nMODIFICAR ALUMNO")
    print("1. Modificar nombre")
    print("2. Modificar apellido")
    print("3. Modificar edad")
    print("4. Modificar nota final")
    print("0. Volver al menú principal")


def modificar_alumno(registros: dict) -> bool:
    """
    Permite modificar los datos de un alumno registrado, excepto su DNI
    """
    dni = pedir_dni()

    if dni not in registros:
        print("El alumno no se encuentra registrado.")
        return False

    mostrar_alumno(dni, registros[dni])

    mostrar_menu_modificacion()
    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "0":
        print("Opción no válida.")
        opcion = input("Seleccione nuevamente una opción: ")

    if opcion == "1":
        registros[dni]["nombre"] = pedir_nombre()

    elif opcion == "2":
        registros[dni]["apellido"] = pedir_apellido()

    elif opcion == "3":
        registros[dni]["edad"] = pedir_edad()

    elif opcion == "4":
        registros[dni]["nota_final"] = pedir_nota()

    elif opcion == "0":
        return False

    print("Alumno modificado correctamente.")

    return True


def eliminar_alumno(registros: dict) -> bool:
    """
    Elimina un alumno del diccionario mediante su dni
    """
    dni = pedir_dni()

    if dni not in registros:
        print("El alumno no se encuentra registrado.")
        return False

    mostrar_alumno(dni, registros[dni])

    confirmacion = input("¿Desea eliminar al alumno? (S/N): ")

    while confirmacion != "S" and confirmacion != "s" and confirmacion != "N" and confirmacion != "n":
        print("Opción no válida.")
        confirmacion = input("Ingrese nuevamente S o N: ")

    if confirmacion == "S" or confirmacion == "s":
        del registros[dni]
        print("Alumno eliminado correctamente.")
        return True

    else:
        print("Eliminación cancelada.")
        return False