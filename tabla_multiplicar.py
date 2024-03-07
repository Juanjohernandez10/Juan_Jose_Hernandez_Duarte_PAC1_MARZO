#Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla de
#multiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla. 


N = int(input("Por favor ingrese un número entero positivo (N): "))


if N > 0:
    
    contador = 1

    
    while contador <= 10:
        print(f"{N} x {contador} = {N * contador}")
        contador += 1
else:
    print("Lo siento, ingresó un número no válido. Por favor intente de nuevo.")
