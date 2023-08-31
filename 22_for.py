'''
# el metodo range no toma el ultimo valor dado, por lo que
# en el sigt codigo va del 1 hasta el 20  

for element in range(1, 21):
    print(element)

'''
# element es una variable que puede ser 'i' o 'element' o la variable que queramos
my_list = [45,76,73,65,34,56,5,68,94]
for element in my_list:
    print(element)

my_tuple = ('foseja', 'joven', 'viejo', 'vivencias')
for element in my_tuple:
    print(element)

person = {
    'name': 'Nixon',
    'age': 27,
    'vivencias': 'querer vivir y conocer'
}
# itera sobre las llaves
for element in person: 
    print(element)  

#itera sobre los valores
for element in person:
    print(person[element])

#iterando dejando las keys y los values del diccionario
for key in person:
    print(key ,'=>', person[key])

#mismo resultado sacando las keys y los value de forma directa en el codigo
for key , value in person.items():
    print(key, '=>', value)

list_people = [
    {
        'name': 'ome programador',
        'age': '2 años',
        'ganas de': 'comerse al mundo',
        'profesion': 'Data ciencies',
    },
    {
        'name': 'yop',
        'age': 'apenas 1',
        'ganas de': 'aprender numpy',
        'profesion': 'Desarrollador lider',
    },
    {
        'name': 'yo it manager',
        'age': 'ya 5',
        'ganas de': 'comerse al mundo',
        'profesion': 'ingenieria de datos',
    }
]

for units in list_people:
    print('name =>', units['name'])

