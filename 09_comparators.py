""" 
Los operadores de comparacion son aquellos que
comparan dos valores y devuelven un booleano como respuesta
de si es True o False

"""


# > mayor que

print(7 > 3)
print(3 > 7)
print(7 > 7)

# < menor que

print(5 < 6)
print(6 < 5)
print(6 < 6)

# >= mayor o igual

print(2 >= 1)
print(1 >= 2)
print(2 >= 2)

# <=  menor o igual

print(4 <= 5)
print(4 <= 3)
print(4 <= 4)

# == estrictamente de igualdad
print( 5 == 5)
print( 55 == 6)

# != diferente a
print(6 != 10)
print(6 != 6)

# comparando con strings

print("desk" == 'chair')
print('bruno' == 'Bruno')
print('Bruno' == 'Bruno')
print("1" == 1)

# comparacion entre variables

age = 27
print(age)

name = "Nixon"
print(name)

comparation = (name == age)
print(comparation)

ingreso_bar = (age >= 18)
print("puedes ingresar al bar papu pronto podras hacer un if"," ", ingreso_bar)

""" 
Al comparar strings tener en cuenta que
python toma como valor del codigo ascii de cada letra,
asi que cada letra representa un valor que es lo que python interpreta
y puede resultar verdadero si la suma del valor de sus letras
coincide con el valor de las letras del string comparado
"""

print("Pera" >= "Banano")
print('Pera' >= 'banano')