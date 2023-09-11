#DICCIONARIO

my_dict = {}
print (type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'nixon',
    'last_name': 'betancour',
    'age': '27',
    'status': 'living_alone',
}
print(my_dict)

#con 'len' podemos saber cuantos elementos se encuentran en el diccionario o tupla o lista, se enumeran los elementos dentro de ella

print(len(my_dict))

# con corchetes podemos leer directamente sobre el valor que me interesa sin contar en que posicion esta el valor 

print(my_dict['age'])
print(my_dict['name'])
print(my_dict.get('last_name')) 
print(my_dict.get('day')) # buscar con .get da como resultado un none a un valor que se encuentre vacio al contrario que con [] que rompre el codigo al no encontrar lo buscado

print('avion' in my_dict)
print('otravariable x' in my_dict)