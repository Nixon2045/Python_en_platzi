# C R U D Create, Read, Update, Delete

#read
numbers = [1,2,3,4,5,6]
print(numbers)
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'holi quiero verte')
print(numbers)

numbers.insert(3, True)
print(numbers)

tasks = ['todo1', 'todo2', 'todo3']
new_list = tasks + numbers
print(new_list)

index = new_list.index('holi quiero verte')
new_list[index] = 'quiero que llegues yaa'
print(new_list)
new_list.remove('todo1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

number_a = [3,7,5,8,15,3,5,2,1,89]
number_a.sort()
print(number_a)

strings = ['holi', 'hola', 'holas', 'que dice usted gonorrea']
strings.sort()
print(strings)



