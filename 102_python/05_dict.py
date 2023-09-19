# version larga de sintaxis para list comprehension con dictionarios, usamos los llaves {} para formular

dict = {}
for i in range(1, 6):
    dict[i] = i * 2 #en esta linea agregamos el par de valor a la llave multiplicando 2 veces por cada iteracion dada en la llave

print(dict)

#version de sintaxis corta para list comprenhension con diccionarios

dict_v2 = {i : i * 2 for i in range(1, 6)}
print(dict_v2)