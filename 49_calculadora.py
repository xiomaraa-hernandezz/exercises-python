import os
import time

while True:
    os.system('cls')
    opc = int(input('1. Calcular factorial\n2. Calcular potencia\n3. Salir\n--> '))
    if opc == 1:
        data = int(input('Ingrese un dato: '))
        vuelta = 0
        resultado = 1
        for i in range ((data-1)):
            resultado += (i+1) * resultado
            print(resultado)
            vuelta += 1
            os.system('cls')
        print(f'El factorial del numero {data} es: {resultado}') 
        pausa = time.sleep(4) 
    elif opc == 2:
        numu = float(input('Ingrese la base: '))
        numd = float(input('Ingrese el exponente: '))
        exp = 1
        r = numu
        while exp != numd:
            r = r  * numu
            exp += 1
        os.system('cls')
        print(f'El resultado de la potencia {numu} elevado a {numd} es {r}')
        pausa = time.sleep(4) 
    elif opc == 3:
        os.system('cls')
        print('Programa terminado, saliendo...')
        pausa = time.sleep(4) 
        break
    else:
        os.system('cls')
        print('Numero equivocado, intente de nuevo')
        pausa = time.sleep(4) 
        continue  
          
