import re


indice = int(input("Ingrese un numero de ejercicio: "))
if(indice == 1):
    """ Desarrollar una función que reciba tres números positivos y devuelva el mayor
de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor
estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y
mostrar el máximo hallado, o un mensaje informativo si éste no existe"""
# valor 1, valor 2, valor 3'
#if max( v1,v2,v3) and max != v2 and v3 (else return -1)
    def validarMayor(valores):
        resultado = max(valores)
        hayRepetidos = valores.count(resultado)
        if(hayRepetidos > 1):
            return -1
        else:
            return resultado

    contenedor = []
    while True:
        valor = input("Ingresa un dato numerico: ")
        if(valor == "salir" or valor == "Salir"):
            break
        if(valor.isalpha()):
            print("Por favor, ingrese un dato valido.")
            continue
        else:    
            contenedor.append(int(valor))

    respuesta = validarMayor(contenedor)
    if(respuesta == -1):
        print("no hay mayor unico")
    else:
        print(f"El numero mayor es: {respuesta}")
elif(indice == 2):
    """Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función."""

    def validarFecha(va1,va2,va3):
        fecha = str(va1)+ "/" + str(va2)+ "/" +str(va3)
        patron = re.compile("^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$")
        if(bool(patron.search(fecha))):
            return "Fecha correcta"
        else:
            return "Fecha incorrecta"

    def validarNumero(valor):
        if(str(valor).isalpha()):
            print("Por favor, ingrese un dato correcto")
            return True
            
    while True:
        valor1 = input("Ingresa el dia: ")
        if(validarNumero(valor1)):
            continue       
        valor2 = input("Ingresa  el mes: ")
        if(validarNumero(valor2)):
            continue       
        valor3 = input("Ingresa el año: ")
        if(validarNumero(valor3)):
            continue
        print(validarFecha(valor1,valor2,valor3))
        valor4 = str(input("Deseas validar otra fecha? (s/n): "))
        if(valor4 != "s"):
            break

elif(indice == 3):
    """Un comercio de electrodomésticos necesita para su línea de cajas un programa
que le indique al cajero el cambio que debe entregarle al cliente. Para eso se
ingresan dos números enteros, correspondientes al total de la compra y al
dinero recibido. Informar cuántos billetes de cada denominación deben ser
entregados al cliente como vuelto, de tal forma que se minimice la cantidad de
billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la
compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de
$100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1."""

# contenedor = [100,50,20,10,5,1]
# costo = 500
# recibido = x
# vuelto = x (costo - recibido)  
#cambio = x
#recorremos (contenedor) desde mayor a menor denominacion
#Si mayor denominacion alcanza como vuelto se agrega a cambia
#asi hasta llegar a la minima denominacion

def devolverVuelto(costo,recibido):
    if(recibido < costo):
         print("Error: Falta dinero para cubrir el costo")
    else:
        contenedorBilletes = [100,50,20,10,5,1]
        vuelto = recibido - costo
        #Almacena los billetes requeridos para dar el cambio
        cambioContendor = []
        #suma cambioContenedor para tener una referencia de cuanto necesitamos
        cambioTotal = vuelto
        #Retornamos resultadoFinal como un string que suma todo el cambio necesario
        resultadoFinal = ""
        for valorDinero in contenedorBilletes:
            while cambioTotal >= 0 and cambioTotal >= valorDinero:
                    cambioContendor.append(valorDinero)
                    cambioTotal = cambioTotal - valorDinero
                    continue
           
        for valorDinero in cambioContendor:
            resultadoFinal = resultadoFinal+" "+str(valorDinero)        
        print(f"Cambio a dar:{resultadoFinal}")    

devolverVuelto((int(100)),int(711))         