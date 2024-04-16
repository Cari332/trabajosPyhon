import random

def adivinarNumero():
    #Medrano Cardenas Carina
    # Límites inferior y superior del rango en el que se encuentra el número
    minimo = 0
    maximo = 100
    respuesta = None

    # Mensaje inicial para el usuario
    print("Piensa en un número entre 0 y 100 y trataré de adivinarlo")

    # Bucle principal para adivinar el número
    while respuesta != "b":
        # Número en base a la mitad del rango actual
        intento = random.randint(minimo, maximo)
        print("¿Es", intento, "El numero en el que penso?")

        # Solicitamos la respuesta del usuario y la convierte en minúscula para simplificar
        respuesta = input("Ingresa 'i' si es menor, 's' si es mayor, o 'b' si es correcto ").lower()

        # Límites del rango según la respuesta del usuario
        if respuesta == "i":
            maximo = intento - 1
        elif respuesta == "s":
            minimo = intento + 1

    # Mensaje para cuando se adivina correctamente el número
    print("Adivine su número correctamente")

# Llamamos a la función para comenzar el juego
adivinarNumero()