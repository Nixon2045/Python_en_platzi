# operadores logicos

# and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10) # al ser un resultado True y False el resultado del AND resulta ser un False

"""
Se realizo programa de prueba para comparacion de numeros y operadores logicos
stock = int (input ('Pon aqui tu numero de inventario =>'))
print(stock >= 100 and stock <= 1000) #se realizo un rango entre 100 y 1000
"""

#####
# operador OR 

print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

role = input ('ingresa tu rol para ingresar : ')
print(role == 'admin' or role == 'seller')