from alumnos import mostrar_alumno


def cantidad_alumnos(registros: dict) -> int:
    """
    Retorna la cantidad total de alumnos registrados
    """
    cantidad = len(registros)
    return cantidad


def calcular_promedio_general(registros: dict) -> float:
    """
    Calcula el promedio general de las notas finales de los alumnos registrados
    """
    acumulador = 0

    if len(registros) == 0:
        return 0.0

    for dni in registros:
        acumulador = acumulador + registros[dni]["nota_final"]

    promedio_general = acumulador / len(registros)

    return promedio_general


def buscar_mayor_nota(registros: dict) -> int:
    """
    Busca la nota final más alta entre los alumnos registrados
    """
    mayor_nota = 0

    for dni in registros:
        if registros[dni]["nota_final"] > mayor_nota:
            mayor_nota = registros[dni]["nota_final"]

    return mayor_nota


def contar_por_condicion(registros: dict) -> list:
    """
    Cuenta cuántos alumnos aprueban y cuántos desaprueban
    """
    aprueban = 0
    desaprueban = 0

    for dni in registros:
        if registros[dni]["nota_final"] >= 6:
            aprueban = aprueban + 1

        else:
            desaprueban = desaprueban + 1

    cantidades = [aprueban, desaprueban]

    return cantidades


def mostrar_estadisticas(registros: dict) -> None:
    """
    Muestra las estadísticas generales de los alumnos registrados
    """
    cantidad = cantidad_alumnos(registros)

    print("\n--- Estadísticas generales ---")
    print(f"Cantidad total de alumnos: {cantidad}")

    if cantidad == 0:
        print("No hay alumnos registrados para calcular estadísticas.")
        return

    promedio_general = calcular_promedio_general(registros)
    mayor_nota = buscar_mayor_nota(registros)
    cantidades = contar_por_condicion(registros)

    print(f"Promedio general: {promedio_general}")
    print(f"Alumnos que aprueban: {cantidades[0]}")
    print(f"Alumnos que desaprueban: {cantidades[1]}")
    print(f"Mayor nota final: {mayor_nota}")

    print("\n--- Alumnos con mayor nota final ---")

    for dni in registros:
        if registros[dni]["nota_final"] == mayor_nota:
            mostrar_alumno(dni, registros[dni])