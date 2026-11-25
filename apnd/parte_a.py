# Parte A - Análisis de estructuras de datos 

# Para cada una de las siguientes situaciones del caso: 
# - Indique qué estructura de datos considera más adecuada. 
# - Justifique técnicamente su respuesta. 

# ------------------------------------------------------------------------------------------

# Situación 1
# Representar la ubicación de los libros en estanterías organizadas en filas y columnas 
# Estructura de datos: matriz
# Justificación técnica: permite organizar información mediante filas y columnas


estanteria = [
    ["libro 1", "libro 2", "libro 3"],
    ["libro 4", "libro 5", "libro 6"],
    ["libro 7", "libro 8", "libro 9"]
]

print(estanteria[1][2]) # salida: libro 6


# ------------------------------------------------------------------------------------------

# Situación 2 
# Guardar información fija de un libro que no debería modificarse accidentalmente 
# Estructura de datos: tuplas
# Justificación técnica: conjunto de elementos inmutables. Una vez creada, no podemos agregar, eliminar ni 
# reasignar sus elementos de forma individual


libro = (123456, "Deja de ser tú", "Joe Dispenza", 2012)

print(libro[1]) # salida: Deja de ser tú


# ------------------------------------------------------------------------------------------

# Situación 3
# Evitar que un mismo socio aparezca registrado varias veces
# Estructura de datos: conjuntos
# Justificación técnica: colección de elementos únicos que no permite el duplicado de los mismos


socios = {101, 102, 103, 101, 102}

print(socios) # salida: {101, 102, 103}


# ------------------------------------------------------------------------------------------

# Situación 4
# Relacionar un ISBN con toda la información de un libro
# Estructura de datos: diccionarios
# Justificación técnica: estructura de datos que almacena información mediante pares de clave-valor, las claves son únicas y
# permiten el acceso a los valores asociados


libros = {
    "123456": ("Deja de ser tú", "Joe Dispenza", 2012),
    "123457": ("En el limbo", "Estanislao Bachrach", 2020)
}

print(libros["123457"]) # salida: ('En el limbo', 'Estanislao Bachrach', 2020)


# ------------------------------------------------------------------------------------------

# Situación 5
# Conservar la información del sistema luego de cerrar el programa
# Estructura de datos: archivos
# Justificación técnica: permiten almacenar información de manera persistente, los datos pueden conservarse después de finalizar 
# el programa y recuperarse mediante operaciones de lectura


archivo = open("libros.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)


archivo = open("libros.txt", "w")
archivo.write("En el limbo")
archivo.close()
