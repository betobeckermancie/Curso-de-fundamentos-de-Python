'''
#el element se usa dentro del range definido
for element in range(1,21):
  print(element)

'''
#imprime cada elemento que itera en la lista
my_list=[23,45,67,89,43]
for element in my_list:
  print(element)
#imprime cada elemento que itera en la tupla
my_tuple = ('inicio', 'juli', 'santi')
for element in my_tuple:
  print(element)
#creamos el diccionario
product = {
  'name' : 'Camisa',
  'price':100,
  
}
#itera lo que hay en el diccionario diciendo que key es el valor 
for key in product:
  print(key, '=', product[key])
#de uuna forma mas facil muiestra las llaves con su valor
for key, value in product.items():
  print(key, '=', value)
#se crea una lista de personas que tiene diccionarios
people = [
  {
    'name': 'nico',
    'age':34
  },
  {
    'name': 'zule',
    'age':45
  },
  {
    'name': 'santi',
    'age':4
  }
]

for person in people:#itera cada elemento dentro de people
  print('name =', person['name'])#muestra dentro de persona el atributo name

