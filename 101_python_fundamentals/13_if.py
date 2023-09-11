# ejecutando condicionales
if True:
    print('deberia ejecutarse')

if False:
    print('No deberia ejecutarse ')


#jercicio para demostrar funcionamiento de if

pet = input ('¿Cual es tu mascota preferida?: ')

if pet == 'perro':
    print ('genial, tienes un buen amigo')
elif pet == 'gato':
    print ('genial, tienes un sadico en casa')
elif pet == 'pez':
    print('genial, eres primo de aquaman')
else:
    print('sorprendeme con mas mascotas')



"""

stock = int (input ('Pon aqui tu numero de inventario =>'))

if stock >= 100 and stock <= 1000:
    print('el inventario esta en el rango')

else:
    print('El inventario no esta ok')
"""


number = int (input ('ingresa un numero: '))
if number % 2 == 0:
    print('Este es un numero par, Ganaste!')
else:
    print('No es par, sigue intentando')
