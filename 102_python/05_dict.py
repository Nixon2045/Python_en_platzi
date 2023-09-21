'''
# version larga de sintaxis para list comprehension con dictionarios, usamos los llaves {} para formular

dict = {}
for i in range(1, 6):
    dict[i] = i * 2 #en esta linea agregamos el par de valor a la llave multiplicando 2 veces por cada iteracion dada en la llave

print(dict)

#version de sintaxis corta para list comprenhension con diccionarios

dict_v2 = {i : i * 2 for i in range(1, 6)}
print(dict_v2)
'''
# se agrego el valor population a las llaves del diccionario countries con la biblioteca random
import random
countries = ['col','pe','mex','bol']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

#usando list comprehension para el ej anterior(usando sintaxis corta)

population_v2 =  {country: random.randint(1, 100) for country in countries}
print(population_v2)
