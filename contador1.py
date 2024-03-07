a = 4 
cantidad_A = 0 
e = 5 
cantidad_E = 0 
i = 6 
cantidad_I = 0 
o = 7 
cantidad_O = 0 
u = 8 
cantidad_U = 0 
contadorInt = 0 

while True:
    print('seleccione una opcion')
    print('1. continue la operacion')
    print('2. mostrar en pantalla ')
    print('3. finalizar')

    option = int(input("ingresa un caracter: "))

    if option == 1:
        user_input = input('adjunta un caracter:-> ')
        if user_input.lower() in 'aeiou':
            if user_input == 'a':
                cantidad_A += 1
            elif user_input == 'e':
                cantidad_E += 1
            elif user_input == 'i':
                cantidad_I += 1
            elif user_input == 'o':
                cantidad_O += 1
            elif user_input == 'u':
                cantidad_U += 1
    elif option == 2:
        print(f'Cantidad de A: {cantidad_A}')
        print(f'Cantidad de E: {cantidad_E}')
        print(f'Cantidad de I: {cantidad_I}')
        print(f'Cantidad de O: {cantidad_O}')
        print(f'Cantidad de U: {cantidad_U}')
        print(f'Total: {cantidad_A + cantidad_E + cantidad_I + cantidad_O + cantidad_U}')
    elif option == 3:
        print(f'Total: {cantidad_A + cantidad_E + cantidad_I + cantidad_O + cantidad_U}')
        break
    else:
        print("opcion no valida")