# # Día 1 - FizzBuzz

# Escribe un programa que imprima los números del 1 al 100 siguiendo estas reglas:
# - Múltiplos de 3 -> 'Fizz'
# - Múltiplos de 5 -> 'Buzz'
# - Múltiplos de ambos -> 'FizzBuzz'

# # Escribe tu solución aquí



# Recorremos los números del 1 al 100 (range(1, 101) incluye el 1 y excluye el 101)
for i in range(1, 101):
    
    # Si 'i' es múltiplo de 3 y de 5 al mismo tiempo (es decir, de 15)
    # se imprime primero esta rama para no “capturar” antes los casos de 3 o 5 por separado.
    if i % 3 == 0 and i % 5 == 0:
        # Imprime 'Fizz buzz' y NO hace salto de línea gracias a end=" "
        # (así todos los resultados salen en una sola línea separados por espacios).
        print('Fizz buzz', end=" ")
        
    # Si no cayó en la condición anterior y es múltiplo de 3:
    elif i % 3 == 0:
        print('fizz', end=" ")
    
    # Si no cayó en las anteriores y es múltiplo de 5:
    elif i % 5 == 0:
        print('buzz', end=" ")
    
    # En cualquier otro caso, imprime el número tal cual.
    else:
        # f'{i}' usa f-strings para convertir 'i' a texto.
        print(f'{i}', end=" ")
