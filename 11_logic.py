# AND da true cuando las dos partes de la operacion son verdaderas

print('AND')
print('True and True =', True and True)
print('True and True =', True and False)
print('True and True =', False and True)
print('True and True =', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)


#ingresamos un numero mayor o igual a 100 pero menor o igual a 1000 para que nos de true
stock = input('Ingrese el numero de stock')
stock = int(stock)

print(stock >= 100 and stock <=1000)

# OR si alguno de los dos es TRUE el resultado da True

print('OR')
print('True or True =', True or True)
print('True or True =', True or False)
print('True or True =', False or True)
print('True or True =', False or False)


#dara true si se digita cualquiera de los dos roles como admin y seller ya que se usa OR
role = input('Digita el rol=')
print (role =='admin' or role == 'seller')