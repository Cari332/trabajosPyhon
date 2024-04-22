def calcular_capital(cantidad, interes, años):
    #MedranoCardenas
    # Función para calcular el capital obtenido cada año
    capital = cantidad  # Inicializa el capital con la cantidad inicial
    for i in range(1, años + 1):  # Itera sobre cada año
        capital += capital * (interes / 100)  # Calcula el nuevo capital con el interés
        print(f"Capital tras {i} año(s): {capital:.2f}")  # Imprime el capital tras cada año

def main():
    # Función principal
    try:
        cantidad = float(input("¿Ingrese la Cantidad a invertir?: "))  # Solicita la cantidad a invertir
        interes = float(input("¿ingrese el Interés porcentual anual?: "))  # Solicita el interés anual
        años = int(input("¿ingrese los Años?: "))  # Solicita la cantidad de años

        if cantidad < 0 or interes < 0 or años < 0:
            raise ValueError("Los valores a ingresar deben ser positivos.")

        calcular_capital(cantidad, interes, años)  # Llama a la función para calcular el capital
    except ValueError as e:
        print(f"Error: {e}")  # Errores de entrada

if __name__ == "__main__":
    main()  # Llama a la función principal si el programa se ejecuta directamente