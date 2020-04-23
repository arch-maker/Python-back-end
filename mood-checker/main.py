#COMPROBADOR DE HUMOR.

#Pedimos por pantalla el estado de animo y lo asignamos a la variable modo.
modo = input("Hola Humano ¿Como estás? ¿En que estado de animo te encuentras? ")

#Comprobacion de los diferentes estados de animo.
if modo == "feliz":
    print("\nEs genial verte feliz!")
elif modo == "nervioso":
    print("\nRespira hondo 3 veces")
elif modo == "triste":
    print("\nAnimate amigo!")
elif modo == "emocionado":
    print("\nEs normal llegar a emocionarse en este caso. No te preocupes!")
elif modo == "relajado":
    print("\nMe gusta verte asi de relajado")
else:
    print("\nNo reconozco este estado de animo, lo siento! ")