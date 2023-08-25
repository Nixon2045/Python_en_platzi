text = 'Ella sabe python'
print(text[0])
print(text[1])
#print(text[999]) esta por fuera de rango y no la encuentra por eso no sale error
size = len(text)
print('size=>', size)
print(text[size -1])
print(text[-1])
print(text[-3])

#slicing

print(text[0:5])
print(text[0:10])
print(text[10:16])
print(text[:10]) #forma abreviada de iniciar desde cero
print(text[5:-1]) #esta sintaxis toma desde el caracter 5 hasta el final pero no toma el ultimo, la 'n'
print(text[5:]) #de esta forma desde el inicio del caracter 5 hasta el final
print(text[:]) #de esta forma toma todo el string desde el inicio al final
print(text[10:16:2]) # de esta forma salta de a 2 caracteres
print(text[::2])
