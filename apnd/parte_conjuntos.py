# Demostración práctica de una de las preguntas de selección múltiple

# Pregunta elegida: conjuntos 


# primero creamos una lista de socios con elementos repetidos, los números 18 y 7 aparecen 2 veces
socios = [18, 6, 7, 18, 5, 7]

print("Lista de socios:", socios)


# luego, convertimos la lista en un conjunto, la función set() crea el conjunto y elimina los elementos duplicados
socios_unicos = set(socios)

print("Conjunto de socios:", socios_unicos)


# luego, intento agregar un socio que ya está registrado
# la función add() permite agregar un elemento al conjunto, pero como el elemento 6 ya existe, no se modifica y tampoco tira error
socios_unicos.add(6)

print("Conjunto luego de agregar un socio existente:", socios_unicos)


# intento agregar un nuevo socio
# en este caso, el elemento se agrega al conjunto porque anteriormente no estaba
# el orden de los elementos puede cambiar ya que no garantiza un orden
socios_unicos.add(14)

print("Conjunto luego de agregar un nuevo socio:", socios_unicos)


# recorro el conjunto con un bulce for sin utilizar índice
# si intento ejecutar socios_unicos[0] me tira error porque no puedo acceder mediante índices
print("Listado de socios:")

for socio in socios_unicos:
    print(socio)
