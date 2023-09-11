""" COMENTARIO PARA RESOLVER RETO DE CLASE
lives = 3
print(type(lives))

age = 12
budget = 100

#floats
temperature = 37.8
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 35 + 45
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 82
print(lives)

lives += 98
print(lives)

number_a = 24000000000000000000000.1
print(number_a)

number_b = 0.000000000000000000000000000032
print(number_b)
"""
budget_enero    =  (input ("pon aqui tu presupuesto del mes de enero: "))
budget_febrero  =  (input ("pon aqui tu presupuesto del mes de febrero: "))
budget_marzo    =  (input ("pon aqui tu presupuesto del mes de marzo: "))

budget_enero      = int (budget_enero)
budget_febrero    = int (budget_febrero)
budget_marzo      = int (budget_marzo)

budget_avg = ((budget_enero+budget_febrero+budget_marzo)/3)
print("tu gasto promedio es: ", budget_avg)

#budget_total = int (budget_enero + budget_febrero + budget_marzo)

#months = 3

#budget_avg = int (budget_total / months)
#print = ("el promedio de tus primeros 3 meses es: ", budget_avg)