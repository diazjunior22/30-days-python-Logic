# Día 2 - Invertir una cadena

#Crear una función que reciba una cadena y la devuelva invertida, sin usar slicing [::-1].


#palabra[inicio:fin:-1]

# Escribe tu solución aquí



def cadenaInvertida(palabra : str):
    palabra_invertida = []
    
    for i in palabra:
        #palabra_invertida.append(i)
        palabra_invertida.insert(0,i)
        
    palabra_invertida = ''.join(palabra_invertida)
    return palabra_invertida
    
print(cadenaInvertida('hola'))



