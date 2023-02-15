text = "ella sabe python"
print(text[0])
print(text[1])
#print (text[999])
size = len(text)
print('size =', size)
print(text[size -1])#forma antigua y larga
print(text[-1])#esta forma es mas corta y hace lo mismo que arriba

#slicing , extra desde donde indiques a donde quieras
print(text[0:5])
print(text[10:16])
print(text[:10])#si no declaras el inicio de marca desde la posicion que inicia
print(text[5:-1]) # desde la posicion 5 hasta el final
print(text[5:])#como no le damos nada comienza desde la posicion 5 hasta el final
print(text[:])#desde el inicio hasta el final
print(text[10:16:1])#con esto saltas de posiciones aqui '1'
print(text[10:16:2])#con esto saltas de posiciones aqui '2'
print(text[::2])#con esto saltas de posiciones aqui '3'