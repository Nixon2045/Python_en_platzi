def find_volume(length, width, depth):
    return length * width * depth

#agregando los valores de cada parametro calcula el valumen pero 
# si quiero ingresar valores a un solo parametro debo especificarlo 
result = find_volume(5, 9, 8) #resultado 360
print(result)

print('*' * 10)
#ejemplo definiendo valores por default y asignando valor a un solo parametro
#se definen los valores por default en los parametros '=1' (solo es de ejemplo)
def find_volume(length=1, width=1, depth=1):
    return length * width * depth
result = find_volume(width=60) # se especifica al unico parametro al que se le asigna valor
print(result)

print('*' * 10)

#para agregar mas valores que retornar se agregan con coma luego de metodo
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, 'hola', 56, width # el resultado de este return sera una tupla
result = find_volume()
print(result[2]) # al ser una tupla podemos escoger el resultado a mostrar con slicing '(result[2])', 
#seleccionando el valor en la posicion indicada

print('*' * 10)

def find_volume(length=1, width=1, depth=1):
    return length * width * depth, 'this is a probe', 57, length#para dar con el valor de cada return lo asignamos en el 
result, text, number, length = find_volume(width=60) #en el mismo orden en que se declararon en el return
print(result) #y asi podemos imprimir el resultado de cada return
print(text)
print(number)
print(length)