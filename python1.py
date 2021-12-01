
res_indice = int(input("Ingresa el numero de ejercicio: \n"))

if(res_indice == 1):
    #Escribe un programa muestre por pantalla “Hello World”
    print('Hello World')

elif(res_indice == 2):
    # Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
    print(3 + 5)

elif(res_indice == 3):   
    '''Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario ”'''
    dato = input("Ingresa tu nombre: \n")
    print(f"Hola {dato}")

elif(res_indice == 4):
    '''Escribe un programa que pida un número, pida otro número y escriba el
resultado de sumar estos dos números.'''
    num1 = int(input("Ingresa un valor: \n"))
    num2 = int(input("Ingresa otro valor: \n"))
    print(f"Hola {num1 + num2}")

elif(res_indice == 5):
    '''Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.'''
    num1 = int(input("Ingresa un valor: \n"))
    num2 = int(input("Ingresa otro valor: \n"))
    if(num1 > num2):
        print(f'El primer numero es mayor')
    elif(num2 == num1):
        print('Son iguales')
    else:
        print("El segundo valor es mayor")

elif(res_indice == 6):
    '''Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.'''
    num1 = int(input("Ingresa el primer valor: \n"))
    num2 = int(input("Ingresa el segundo valor: \n"))
    num3 = int(input("Ingresa el tercer valor: \n"))
    if(num1 > num2 and num1 > num3):
        print(f'El primer valor {num1} es mayor')
    elif(num2 > num1 and num2 > num3):
        print(f'El segundo valor {num2} es mayor')
    else:
        print(f'El tercer valor {num3} es mayor')

elif(res_indice== 7):
    '''Escribe un programa que pida un número y diga si es divisible por 2'''
    num1 = int(input("Ingresa un valor: \n"))
    if(num1 % 2 == 0):
        print("Es divisible entre 2")
    else:
        print("No es divisible entre 2")

elif(res_indice == 8):
    """Un programa que sea divisible entre 2,3,5,7"""
    multiplos = [2,3,5,7]
    dato_ingresado = int(input("Ingrese un numero: "))
    hay_divisores = 0
    print("Es divisible por: ",end='')
    for multiplo in multiplos:
        if (dato_ingresado % multiplo == 0):
            print(f'{multiplo}',end=" ")
            hay_divisores += 1
        if (hay_divisores == 0):
            print("No hay divisores")

elif(res_indice == 9):
    #Cuenta las vocales en un texto
    dato_ingresado = str(input("Ingrese una frase y te dire cuantas vocales dispone: "))
    lista_vocales = ["a","e","i","o","u"]
    contenedor_vocales = [0,0,0,0,0]
    for letra in dato_ingresado:
        if(letra == " "):
            continue
        for vocal in lista_vocales:
            if (vocal == letra):
                contenedor_vocales[lista_vocales.index(vocal)] += 1
                break
        
    print("Hay un total de: ")
    for vocal_res in lista_vocales:
        print(f'{vocal_res}: {contenedor_vocales[lista_vocales.index(vocal_res)]}',)

elif(res_indice == 10):
    "Escribe un numero y verificara si es primo o no"
    dato_ingresado = int(input("Ingresa un dato numerico: "))
    contenedor_primos = [1,2,3,4,5,6,7,8,9, dato_ingresado]
    resultado_primo = set(filter(lambda x,: dato_ingresado % x == 0,contenedor_primos))
    print(resultado_primo)
    if(resultado_primo.len() -1 > 1 or dato_ingresado == 1):
        print("Es primo")
    else:
        print("No es primo ")

elif(res_indice == 11):
    'Pide una nota y muestra la calificacion segun la nota'
    validador = [["Muy deficiente",0,1,2],["Insuficiente",3,4],["Suficiente",5],["Bien",5,6],["Notable",7,8],["Sobresaliente",9,10]]
    dato_ingresado = int(input("Ingresa un dato numerico: "))

    for valor in validador:
        for valor_numerico in valor[1:len(valor)]:
            if (valor_numerico == dato_ingresado):
                print(valor[0])
elif(res_indice == 12):
    "Imprime una piramide ascendiente de numeros"
    for x in range(8):
        valor = str(x) * x
        print(valor)

elif(res_indice == 13):
    "Imprime una piramide decendiente de numeros"
    for x in range(8,0,-1):
        valor = str(x) * x
        print(valor)
elif(res_indice == 14):
    "Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal."
    contador_lineas = 0
    for valor in range(0,500):
        contador_lineas += 1
        
        if(str(valor/4) == str(valor//4)+".0" and valor != 0 ):
           print(valor,"Multiplo de 4",end='\n\n')
        elif(str(valor/9) == str(valor//9)+".0" and valor != 0):
           print(valor,"Multiplo de 9",end='\n\n')
        else:
           print(valor,end='\n\n')
        if(contador_lineas == 5):
            contador_lineas = 0
            print("---------------------------",end='\n\n')
    
        