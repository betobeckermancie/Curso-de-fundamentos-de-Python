#se define el diccionario
person = {
  'name': 'nico',
  'last': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print (person)
#remplaza el valor de nico a santi
person['name']= 'santi'
person['age'] -=50#resta el valor actual -50
print(person)
#inserta un elemento en la lista
person['langs'].append('rust')
print(person)
#elimamos la llave que se quiere eliminar
del person['last_name']
#eliminamos el ultimo elemento y decimos que llave
person.pop('age')

print(person)

print(person.items())
#genera una tupla donde devuelve la clave y valor
print('items')
print(person.items())
#devuelve las llaves
print('keys')
print(person.keys())
#devuelve los valores
print('values')
print(person.values())