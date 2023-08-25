name      = 'Nixon'
last_name = 'Betancour andica'
age       =  27
print(name)
print(last_name)
print(age)

full_name = name + ' ' + last_name
print(full_name)

# formato

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}" .format(name, last_name)
print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

# reto de la clase

template = f"hola mi nombre es {name} y mi apellido es {last_name} y actualmente tengo la edad de {age}"
print(template) 

# practiquemos jugando con input

name      = input ("pon primero tu nombre: ")
last_name = input ("pon aqui tu apellido: ")
age       = input ("por ultimo pon aqui tu edad: ")

template = (f"Hola tu nombre es {name} y tienes un apellido {last_name} que significa riqueza y valor, cuentas con una edad de {age} y estas a punto de iniciar una de las carreras mas excitantes de todos los tiempos")
print('v1.', template)