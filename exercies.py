#Exercise 1
'''
giveme = (input('give me one word =>'))

for i in range(10):
    print(giveme)

#exercise 2
age = int(input('¿cual es tu edad?:'))

for element in range(age):
    print('has cumpliado ' + str(element+1) + ' años')
'''
number = int(input('dame un numero entero positivo => '))
for element in range(1, number+1, 2):
    print(element, end=', ')
