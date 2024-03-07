#Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debe
#solicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversión
#correspondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.
while True:
    print("Menú de opciones:")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Convertir Fahrenheit a Celsius")
    print("3. Salir")

    opcion = int(input("Por favor seleccione una opción: "))

    if opcion == 1:
       
        celsius = float(input("Por favor ingrese la temperatura en Celsius: "))

        
        fahrenheit = (celsius * 9/5) + 32

        
        print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")

    elif opcion == 2:
        
        fahrenheit = float(input("Por favor ingrese la temperatura en Fahrenheit: "))

        
        celsius = (fahrenheit - 32) * 5/9

        
        print(f"La temperatura en Celsius es: {celsius:.2f}°C")

    elif opcion == 3:
        print("¡Hasta luego!")
        break # finalizamos el bucle  while para salir del programa

    else:
        print("Opción no válida, intente de nuevo.")