def calcular_dinero(puntuacion, salario):
    #Medrano Cardenas
    # Función para calcular el nivel de rendimiento y la cantidad de dinero recibida
    if 0 <= puntuacion <= 3:
        nivel = "Inaceptable"
    elif 4 <= puntuacion <= 6:
        nivel = "Aceptable"
    elif 7 <= puntuacion <= 10:
        nivel = "Meritorio"
    else:
        return "Puntuación inválida"

    dinero = salario * (puntuacion / 10)
    return nivel, dinero

def main():
    # Función principal
    try:
        salario = float(input("Ingrese su salario mensual: "))  # Solicita el salario mensual
        puntuacion = int(input("Ingrese su puntuación: "))  # Solicita la puntuación

        resultado = calcular_dinero(puntuacion, salario)  # Calcula el nivel de rendimiento y la cantidad de dinero
        if resultado != "Puntuación inválida":  # Si la puntuación es válida
            nivel, cantidad_dinero = resultado  # Obtiene el nivel y la cantidad de dinero
            # Imprime el resultado con formato
            print(f"Nivel de Rendimiento: {nivel}, Cantidad de Dinero Recibido: ${cantidad_dinero:.2f}")
        else:  # Si la puntuación es inválida
            print("Puntuación inválida, por favor ingrese una puntuación entre 0 y 10.")  # Imprime un mensaje de error
    except ValueError:
        print("Ingrese numeros válidos")  # Manejo de errores de entrada

if __name__ == "__main__":
    main()  # Llama a la función principal si el programa se ejecuta directamente