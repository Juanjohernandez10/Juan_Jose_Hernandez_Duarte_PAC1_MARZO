

import os 
os.system ("cls")
cantidad_ferre = 0
cantidad_ase = 0
cantidad_segu = 0
cantidad_ali = 0
cantidad_elect = 0
while  True:
    opcionesInt = int(input('>>>>CATEGORIA<<<< \n1. ferreteria \n2. aseo \n3. seguridad \n4. alimentos \n5. electrodomesticos \n6. facturar \n. opcion -> '))
    
    if opcionesInt < 1 or opcionesInt > 6:
        print('informacion no valida')
    elif opcionesInt == 1:
        objetoStr = input('ingrese el objeto a comprar -> ')
        valorInt = int(input('ingrese el valor del objeto -> '))
        print('el objeto es: ',objetoStr)
        descuentoFlt = valorInt * 0.10
        pagarFlt = valorInt - descuentoFlt
        cantidad_ferre += 1
    elif opcionesInt == 2:
        objetoStr = input('ingrese el objeto a comprar -> ')
        valorInt = int(input('ingrese el valor del objeto -> '))
        print('el obejto es:',objetoStr)
        descuentoFlt = valorInt * 0.05
        pagarFlt= valorInt - descuentoFlt
        cantidad_ase+=1
    elif opcionesInt == 3:
        objetoStr = input('ingrese el objeto a comprar -> ')
        valorInt = int(input('ingrese el valor del objeto -> '))
        print('el objeto es :',objetoStr)
        descuentoFlt = valorInt * 0.15
        pagarFlt = valorInt -  descuentoFlt 
        cantidad_segu += 1
    elif opcionesInt == 4:
        objetoStr = input('ingrese el objeto a comprar -> ')
        valorInt = int(input('ingrese el valor del objeto -> '))
        print('el objeto es :',objetoStr)
        descuentoFlt = valorInt * 0.08
        pagarFlt = valorInt -  descuentoFlt 
        cantidad_ali += 1
    elif opcionesInt == 5:
        objetoStr = input('ingrese el objeto a comprar -> ')
        valorInt = int(input('ingrese el valor del objeto -> '))
        print('el objeto es :',objetoStr)
        descuentoFlt = valorInt * 0.12
        pagarFlt = valorInt -  descuentoFlt 
        cantidad_elect+= 1
    elif  opcionesInt == 6:
        print(f'cantidad de objetos en ferreteria es: {cantidad_ferre}')
        print(f'cantidad de objetos en aseo es: {cantidad_ase}')
        print(f'cantidad de objetos en seguridad es: {cantidad_segu}')
        print(f'cantidad de objetos en alimentos es: {cantidad_ali}')
        print(f'cantidad de objetos en electrodomesticos es: {cantidad_elect}')
        print(f'valor a pagar es: {pagarFlt}')
        break

        
        
         
         
        
     