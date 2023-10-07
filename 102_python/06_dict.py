'''
import random
countries = ['col','pe','mex','bol']

population_v2 =  {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country: population for country, population in population_v2.items() if population > 50}
print(result)
'''
text = 'hola estoy iterando este string para sacar las vocales'
vocals = { caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
print(vocals)

text_v2 = 'voy a iterar un texto largo para poder realizar el conteo de vocales y agregarlas como valor en un diccionario'
count = { c : text_v2.count(c) for c in text_v2 if c in 'aeiou'}
print(count)