#CALCULADORA - suma, resta, multiplicacion, division.

numero_1 = int(input("Introduzca el primer numero: "))
numero_2 = int(input("Introduzca el segundo numero: "))

#Se ha guardado cada operacion en una variable, asi podriamos utilizarla cuando nos haga falta en el programa.
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

#Seleccionamos la operacion que queremos realizar para los numeros introducidos
operacion = input("Introduzca la operacion que desea realizar: + - * / ")

#Realizaremos la operacion que le hayamos indicado y nos mostrara un mensaje con el resultado (haciendo casting al resultado)
if operacion == "+":
    print("\nLa suma de los dos numeros introducidos es: ",(suma))

elif operacion == "-":
    print("\nLa resta de los dos numeros introducidos es: ",(resta))

elif operacion == "*":
    print("\nLa multiplicacion de los dos numeros introducidos es: ",(multiplicacion))

elif operacion == "/":
    print("\nLa division de los dos numeros introducidos es: ",(division))

else:
    print("\nERROR! La operacion seleccionada no existe actualmente en el sistema!!!")