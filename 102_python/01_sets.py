#los 'sets' o conjuntos son estructuras de datos que
#no se repiten ni llevan ningun orden dentro de ellas
#tambien permiten su modificacion
#comparten estructura con los diccionarios usando{} pero 
# los sets no llevan key: value  o llave valor de los diccionarios
 

set_contries = {'col','mex','dubai'}
print(set_contries)
print(type(set_contries))

set_numbers = {1,2,2,3,4,5,7,8,5,7,8,9}
print(set_numbers)
print(type(set_numbers))

# los sets pueden ser de un solo tipo de dato como el ej anterior
# o incluso de diferentes tipos de datos como un entero (int)
# o una cadena (str) o float incluso boleanos

set_types = {1,'hello',False, 3.1416}
print(set_types)

#tambien podemos crear un set o conjunto a partir de un string 

set_from_string = set('hola')
print(set_from_string)
print(type(set_from_string))

#tambien podemos crear un set o conjunto apartir de una tupla

set_from_tupla = set(('abc','amor','decisiones','experiencias'))
print(set_from_tupla)
print(type(set_from_tupla))

#tambien podemos crear un set o conjunto apartir de una lista
#y volverla a convertir de un set o conjunto a una lista

numbers = [1,5,3,7,5,9,8,3,6,5,8,7]
converse_numbers = set(numbers)
print(converse_numbers)
unique_numbers = (list(converse_numbers))
print(unique_numbers)
