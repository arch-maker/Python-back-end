#ADIVINA EL NUMERO SECRETO.

#Introducimos una variable para almacenar el numero secreto premiado.
numero_secreto = 17

#Le pediremos al usuario que introduzca un numero por pantalla del 1 al 20.
numero_usuario = int(input("ADIVINA EL NUMERO SECRETO! ¿Qué numero quieres introducir del 1 al 20: "))

#Realizamos las comprobaciones para saber si el numero es premiado.
if numero_usuario == numero_secreto:
    print("\nENHORABUENA! El numero " + str(numero_usuario) + " es el premiado! ha ganado usted el gran PREMIO!")
else:
    print("\nLo sentimos mucho! el numero " + str(numero_usuario) + " no es el numero premiado!")