#Las alcances de las variables pueden variar de locales a globales 
#siendo locales si hacen parte de una funcion y solo se puedan usar en ese contexto
#y globales desde que se puede usar la variable en cualquier parte del codigo 

#jemeplo

cuenta = 100 # Global

def my_pretty_variable():
    cuenta = 200  # Local
    result = cuenta + 10
    print(result) 
    return result
    

print(cuenta)
cuenta_2 = my_pretty_variable()
print(cuenta_2)
print(result) #este result no funciona porque no esta definido en el contexto global 
# y solo puede usarse dentro del contecto local de la funcion donde esta definido
