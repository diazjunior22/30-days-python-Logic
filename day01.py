# # Día 1 - FizzBuzz

# Escribe un programa que imprima los números del 1 al 100 siguiendo estas reglas:
# - Múltiplos de 3 -> 'Fizz'
# - Múltiplos de 5 -> 'Buzz'
# - Múltiplos de ambos -> 'FizzBuzz'

# # Escribe tu solución aquí



for i in range (1,101):
    
    if i % 3 == 0 and  i % 5 == 0:
        print('Fizz buzz',  end=" ")
    elif i % 3 == 0 :
        print('fizz' ,  end=" ")
    elif i % 5 ==  0:
        print('buzz',  end=" ")
    else:
        print(f'{i}' , end=" ")