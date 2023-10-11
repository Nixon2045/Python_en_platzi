# los parametros con lo cuales funciona una funcion  son los que vienen como el siguiente ejemplo 
# def UNA_funcion(parametro a, perametro b, parametro c) 

def my_print(text):
    print( text * 2)
#al llamar la funcion el argumento es el que se encuentra entre parentesis al llamar la funcion
my_print('texto de prueba')

def suma (a,b):
    my_print(a + b) # usando la funcion my_print multiplica *2 el resultado de los argumentos en la funcion suma

suma(23,56) #79
suma(58,82) #140