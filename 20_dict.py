person = {
      'name': 'Nixon',
      'last_name': 'Betancour',
      'langs': ['python', 'javascript'],
      'age': 27,
}

print(person)

person['name'] = 'Arley'
person['langs'].append('go')
person['age'] += 5

print(person)

#formas de eliminar en un diccionario
del person['last_name']# con del la forma abreviada de 'delete' podemos eliminar elementos con la llave
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())