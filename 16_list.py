number = [1, 2, 3, 4]
print(number)
print(type(number))

task = ['resolver tickets', 'entregar equipo', 'revisar punto de red']
print(task)

types = [1, True, 'hello']
print(types)

print(number[0])
print(task[1])
text = 'hola'
#text[0] = 'w' #cambiar un texto o un string de esa manera no es posible, los strings no son mutables 

task[0] = 'ver cursos de platzi'
print(task)
task[2] = 'hacer mas deberes'
print(task)

print(number[:3])
print(True in types) 
print('hello' in types)