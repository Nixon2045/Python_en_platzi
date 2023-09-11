#mientras la condicion sea True, siempre verdadera, se va a seguir ejecutando de manera infinita
'''
while True:
    print('se ejecuta')  
    

counter = 0 
while counter < 10:
    counter += 1
    print(counter)

# con la instruccion 'break' rompemos el codigo y no permitimos que avance en la siguiente iteracion
counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter) 
'''
counter = 0 

#con la instruccion 'continue' podemos saltar partes del codigo como en el ejemplo si el numero es igual a 15 se salta la iteracion y continua
while counter < 20:
    counter += 1
    if counter == 15:
        continue
    print(counter)