# Medrano Cardenas
#Función para verificar si el número es primo
def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Pedir al usuario que ingrese un número primo
while True:
    try:
        numero = int(input("Ingrese un Número primo: "))
        if primo(numero):
            break
        else:
            print("El número ingresado no es primo ingrese otro nuevamente")
    except ValueError:
        print("ingresar un número entero")

# Generar el triángulo rectángulo con números primos anteriores
for i in range(numero, 0, -1):
    for j in range(i, numero + 1, 2):
        print(j, end=" ")
    print()  # Salto de línea después de cada fila