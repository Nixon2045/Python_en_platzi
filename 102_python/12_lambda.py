def increment(x):
    return x + 1
result = increment(10)
print(result)

#en la funciona lambda la sintaxis es mas corta y los parametros de entrada van primero seguidos 
# del cuerpo o retorno de la funcion como vemos en el siguiente ejemplo 

increment_v2 = lambda x : x + 1 

result = increment_v2(20)
print(result)


# ejemplo de otro lambda son varios parametros de entrada

caso_x = lambda name, last_name: f'the fullname is {name.title()} {last_name.title()}'
result = caso_x('nixon', 'betancour')
print(result) 