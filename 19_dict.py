my_dict ={}#creamos el diccionario
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age' : 87
}

print(my_dict)
print(len(my_dict))

#obtiene el valor guardado en ese elemento
print(my_dict['age'])
print(my_dict['last_name'])
#si no existe un valor da 'none', se previene un error
print(my_dict.get('age'))
#asegurar con IF si esa llave existe dentro del diccionario
print('avion' in my_dict)
print('otro que no' in my_dict)
