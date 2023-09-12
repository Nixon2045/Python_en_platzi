set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
#para realizar una union de dos conjuntos o sets se puede usar el metodo .union o un 
# operador numerico '|'que funciona de igual manera

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# tambien podemos hacer la interseccion de dos conjuntos para revisar los elementos que unen dichos
# conjuntos usando el metodo .intersection o el operador &

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# realizamos la operacion de diferencia que trata de sustraer del conjunto 'a' el conjunto 'b' usando 
# el metodo .difference o el operador matematico de resta " - "

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#podemos realizar la operacion de diferencia simetrica donde solo dejamos los elementos de cada conjunto 
#sin los elementos en comun lo hacemos con el metodo .symmetric_difference o el operador ^

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)