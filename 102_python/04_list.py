#list comprehension:  el como iterar en una sola linea de codigo  
# iterando la lista se necesitan 3 lineas de codigo para  ir del 1 al 11
'''
number = []
for element in range(1, 11):
    number.append(element * 2)
print(number)

#pero con list comprehension podemos iterar un array en una sola linea de codigo

numbers_v2 = [element * 2 for element in range (1, 11)]
print(numbers_v2) 
'''
#un list comprehension con una condicion

number = []
for i in range(1, 11):
    if i % 2 == 0:
        number.append(i)  
print(number)

numbers_v2 = [i for i in range (1 ,11) if i % 2 == 0]
print(numbers_v2)

#el list comprenhension nos sirve para la creacion de una lista con una sintaxis mas corta que traduce 
# en menos lineas de codigo, se puede realizar con conjuntos, listas, tuplas y diccionarios