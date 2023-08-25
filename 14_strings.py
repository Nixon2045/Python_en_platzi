# in sirve para buscar un string dentro de otro string
text = 'Yo estoy aprendiendo python para ser un buen analista de datos'
print('Javascript'in text)
print('python' in text)

if 'python' in text:
    print('elegiste bien!')
else:
    print('Javascript tambien es chevere, elegiste bien!')


""" para evaluar el tamaño de un string podemos usar el metodo
'len' que determina cuantas letras tiene un string. 
recuerda que los espacios tambien son considerados un 
caracter por lo cual tambien lo suma"""

size = len(text)
print(size)

print(text)
print(text.upper())
print(text.lower()) 
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Yo'))
print(text.endswith('python'))
print(text.replace('python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print('345'.isdigit())