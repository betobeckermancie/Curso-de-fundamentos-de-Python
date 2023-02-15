# asi buscamos una palabra 'text' dentro de un texto ya predeterminado

text='ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien')
else:
  print('Tambien elegiste bien')
# podemos leer cuantos caracteres tiene el texto de la sig forma
size = len(text)
print(size)

print(text)
print(text.upper())#hace las letras en mayus
print(text.lower())#hace las letras en minus
print(text.count('a'))#cuenta cuales tienen a

print(text.swapcase())
print(text.starswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capital())#pone el primer caracter en mayuscula
print(text_2.title())#pone el inicio de cada palabra en mayus
print(text_2.isdigit())#nos dice si es un digito
print("398".isdigit())#agarra el digito y nos dice si lo es

textote=input('Ingresa lo que sea en mayusculas')
print(textote.lower())