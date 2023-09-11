#CRUD significa 'Create' crear 'Read' leer 'Update' y 'Delete'
#con el metodo 'len' podemos contar los elementos dentro del conjunto o set

set_contries = {'col','mex','dubai'}
size = len(set_contries)
print(size)

#con el metodo 'in' podemos buscar un elemento dentro del conjunto o set
#la informacion nos la devuelve como boleano
print('col' in set_contries)
print('peru' in set_contries)

# con la funcion 'add' agregamos 
set_contries.add('peru')
print(set_contries)

#la funcion actualizar tiene por nombre directamente 'update'
#funciona similar al 'add' pero se pueden agregar conjuntos pequeños

set_contries.update({'ar','peru','ch','ecu'})
print(set_contries)

#con la funcion 'remove' podemos remover elementos del set o conjunto

set_contries.remove('peru')
print(set_contries)

#si eliminamos un elemento que no existe en el conjunto con remove
#el programa se detendra pero si eliminamos con el metodo discard
# no se rompera el programa
 
#set_contries.remove('peru')
set_contries.discard('peru')
print(set_contries)

#con el metodo 'clear' 
# eliminamos todo el conjunto y el conjunto queda vacio

set_contries.clear()
print(set_contries)
print(len(set_contries))

'''
Funciones de set:

    add(): Añade un elemento.

    update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

    discard(): Elimina un elemento y si ya existe no lanza ningún error.

    remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

    pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

    clear(): Elimina todo el contenido del conjunto.


'''