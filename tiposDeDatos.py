#tipo de listas
###listas###

lista_de_numeros = [1,2,3,4,5,6,7,8,9  ]

frutas = ["manzanas", "bananas","naranjas",True, [1,2,3,4,5,[3,4,5,],4]]

""" print(frutas) """
#como imprimir un dato especifico ejemplo True#
""" print(frutas[-2])
print(frutas[1]) """

#modificar la lista#
""" frutas[0] = "manzanita"
frutas[3] = 'uva'

print(frutas[4][5][2])

print(dir(list)) """


#append agrga un item al final de la lista#
""" 
frutas = ["manzanas", "bananas","naranjas",True, [1,2,3,4,5,[3,4,5,],4]]
frutas.append("kiwi")
print(frutas) """

#insert incertar un elemento a un indice#

frutas.insert(2, 'nueva_fruta')
print(frutas)

#remove elimina por un valor#
frutas.remove("bananas")
print(frutas)
frutas.pop(4)
print(frutas)

#ordenar #
""" 
frutas.sort()

print(frutas) """

##diccionario

persona = {
    "nombre":"juan",
    "edad":35,
    "ciudad":"valparaiso",
    "cursos": ["html","css","js"]
    }

print(persona)

# acceso al diccionario #

print(persona["cursos"])

# modificar un dato 

persona["ciudad"] = "Santiago"
print(persona)

# agregar nueva clave

persona["rut"] = "23443746-k"
print(persona)

#para eliminar
del persona["rut"]
print(persona)

## sets {} no permite duplicados
numeros = {1,2,3,4,5,6,4}
print(numeros)

numeros.add(122)

print(numeros)

numeros.remove(122)
print(numeros)


#tupas son listas ordenadas que no se pueden modificar, son con parentesis redondos

colores = ("rojo", "verde","azul")

#acceso


print(colores)

print(colores[1])

## lo fundamental es estudiar diccionarios y listas
