# Medrano Cardenas
#Pedir al usuario que ngrese un numero entero para los nuveles del triangulo
alturaTriangulo = int(input("Ingrese un numero entero que representara la Altura: "))

# El for comienza con 1 hasta la altura ingresada por el usuario
for i in range(1, alturaTriangulo + 1):
    # Imprimir '*' repetido i veces segun el numero ingresado
    print('*' * i)