import random
countries = ['col','pe','mex','bol']

population_v2 =  {country: random.randint(1, 100) for country in countries}
print(population_v2)

#El cambio principal que hice fue agregar .items() a population_v2 dentro del bucle for
#Esto es necesario para iterar sobre los elementos clave-valor del diccionario population_v2
#condicional_add = { country : population for (country, population) in population_v2.items() if population > 50 }
#print(condicional_add)


text = 'Hola me estoy poniendo a prueba'
variable_x = {caracter:caracter.upper() for caracter in text if caracter in 'aeiou' }
print(variable_x)
