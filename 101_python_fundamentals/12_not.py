# con NOT podemos negar cualquier operacion booleana
print(not True)
print(not False) # nos dara el inverso de la ecuacion

print('*' * 10)

print('NOT y OR')
print('not True or True =>', not (True or True))
print('not True or False =>', not (True or False))
print('not False or True =>', not (False or True))
print('not False or False =>', not (False or False))

stock = int (input ('Pon aqui tu numero de inventario =>'))
print( not (stock >= 100 and stock <= 1000))

