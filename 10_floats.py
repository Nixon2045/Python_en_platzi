"""
La prececision decimal en python es diferente,
al compararse por esto da False
"""


x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
# al compararse dira false por el formato diferente en los decimales
print(x == y)


"""
cambiando los decimales a solo 2 digitos con format
y resolviendo la comparacion pasando de float a str 
"""
y_str = format(y, ".2g")
print('str =>', y_str)

""" 
realice el cambio de formato de x a str pero 
habia una forma mas sencilla y directa de hacerlo cambiando
directamente la variable en el print => str(x)

x_str = format(x, ".2g")
print('str =>', x_str)
"""
print(y_str == str(x))

print('*' * 10)

"""
resolviendo el igual de comparacion de forma matematica
"""

print(x, y)
tolerance = 0.01
print(abs(x - y) < tolerance)

print('*' * 10) #Prueba de clase

x = 3.3
y = (round(1.1 + 2.2, 1)) # con round podemos redondear a 1 decimal o el decimal que queramos el (, 1) al final de la variable sirve para definir el numero de decimal querido
print(x == y)





