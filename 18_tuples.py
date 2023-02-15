#tupla puede tener varios valores, strings y numbers pero no se puede modificar una vez creada
numbers = (1,2,3,5)
strings = ('nico', 'zule', 'santi')
print(numbers)
print('0 =', numbers [0])#ELEMENTO AL INICIO
print('-1 =', numbers [-1])#ELEMENTO AL FINAL
print(type(numbers))

print(strings)
print(type(strings))


#CRUD 
print(strings)
print(strings.index('zule'))#nos dice en que posicion esta ese elemento
print(strings.count('nico'))#nos dice cuantas veces se encuentra nico en esa posicion

#convertir de tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

#agregar y modificar en la lista
my_list[1] = 'juli'
print(my_list)

#trasformar de lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)