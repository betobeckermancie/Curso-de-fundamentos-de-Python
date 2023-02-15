#CRUD Create, read, Update, & Delete
numbers = [1,2,3,4,5]#crear
print(numbers[1])#leer
numbers[-1]=10#actualizar
print(numbers)

#se inserta 700 hasta el final de la lista
numbers.append(700)
print(numbers)

#se inserta hola en la posicion 0
numbers.insert(0, 'hola')
print(numbers)
#crea un espacio y corre esoos elementos a la derecha
numbers.inserte(3, 'change')
print(numbers)

#agregar una lista con una ya creada
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)
#eliminamos de index 'todo 2' y cambiamos/guardamos 'todo changed' en la nueva lista
index = new_list.index('todo 2')
new_list[index] = ' todo changed'
print(new_list)
#asi se borra un elemento
new_list.remove('todo 1')
print(new_list)
#elimina el ultimo elemento de la lista
new_list.pop()
print(new_list)

#elimina uun elemento de esa posicion
new_list.pop(0)
print(new_list)

#mover un array, invertirlo
new_list.reverse()
print(new_list)
#ordena los numeros de mayor a menor
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)
#ordena conforme el abacedario
strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)
#sort no funciona con tipos de datos mezclados