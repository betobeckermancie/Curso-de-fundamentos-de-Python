numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)
#imprime cualquier tipo de cosas numeros, valores, strings
types = [1, True, 'hola']
print(types)
#muestra el elemento de la posicion 0
print(numbers[0])
print(tasks[0])

#para actualizar lo quue hay en la primer posicion es
tasks[0] = 'watch platzy courses'
print(tasks)
#modificar de nuevo la lista con otro elemento
tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
#asi confirmamos si hay un elemento en la lista nos dara un True
print('hola' in types)

