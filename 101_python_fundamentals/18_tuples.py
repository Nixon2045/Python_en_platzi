numbers = (1,2,3,4,5,6)
strings = ('jose', ' mario', 'brunito','alejacosota','brunito')
print(numbers)
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

index = strings.index('alejacosota')
print(index)

print(strings.count('brunito'))

#transformando una tupla
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[2] = 'Brunito juicioso'
print(my_list)

strings = tuple(my_list)
print(strings)
print(type(strings))