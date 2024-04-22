def convertir_a_monedas(cantidad):
    #MedranoCardenas
    # Función para convertir una cantidad en monedas
    monedas20 = cantidad // 20  # Calcula la cantidad de monedas de $20
    cantidad %= 20  # Actualiza la cantidad restante
    monedas10 = cantidad // 10  # Calcula la cantidad de monedas de $10
    cantidad %= 10  # Actualiza la cantidad restante
    monedas5 = cantidad // 5  # Calcula la cantidad de monedas de $5
    cantidad %= 5  # Actualiza la cantidad restante
    monedas1 = cantidad  # La cantidad restante son monedas de $1

    # Imprime el resultado
    print(f"Monedas de $20: {monedas20}")
    print(f"Monedas de $10: {monedas10}")
    print(f"Monedas de $5: {monedas5}")
    print(f"Monedas de $1: {monedas1}")

def main():
    # Función principal
    try:
        cantidad = int(input("Ingrese la Cantidad a Convertir: "))  # Solicita la cantidad a convertir
        if cantidad < 0:
            raise ValueError("La cantidad debe ser un valor entero y positivo.")
        convertir_a_monedas(cantidad)  # Llama a la función para convertir a monedas
    except ValueError as e:
        print(f"Error: {e}")  # Errores de entrada

if __name__ == "__main__":
    main()  # Llama a la función principal si el programa se ejecuta directamente