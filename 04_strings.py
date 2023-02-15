name = "Beto"
last_name="barrera salas"
edad=26
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Beto"
print(quote)

quote2= 'She said "hello" '
print(quote2)

# format 
template ="Hola, mi nombe es " + name + " y mi apellido es " + last_name
print(template)

template = "hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', last_name)

# forma mas usada de mandar a llamar a las variables dentro de los corchetes
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

# actividad
template=f"Hola, mi nombre es {name} y mis apellidos son {last_name}, tengo {edad} years"
print('actividad', template)