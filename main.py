from archivos import cargar_archivo, guardar_archivo
from alumnos import cargar_alumno, listar_alumnos, buscar_alumno, modificar_alumno, eliminar_alumno
from estadisticas import mostrar_estadisticas


def mostrar_menu() -> None:
    """
    Muestra las opciones disponibles del menú principal
    """
    print("\n--- SISTEMA DE GESTIÓN DE ALUMNOS ---")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")


def main() -> None:
    """
    Controla el flujo principal del sistema e invoca las funciones correspondientes a cada opción
    """
    registros = cargar_archivo()

    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    while opcion != "7":

        if opcion == "1":
            if cargar_alumno(registros) == True:
                guardar_archivo(registros)

        elif opcion == "2":
            listar_alumnos(registros)

        elif opcion == "3":
            buscar_alumno(registros)

        elif opcion == "4":
            if modificar_alumno(registros) == True:
                guardar_archivo(registros)

        elif opcion == "5":
            if eliminar_alumno(registros) == True:
                guardar_archivo(registros)

        elif opcion == "6":
            mostrar_estadisticas(registros)

        else:
            print("Error. Opción no válida.")

        mostrar_menu()
        opcion = input("Seleccione una opción: ")


main()