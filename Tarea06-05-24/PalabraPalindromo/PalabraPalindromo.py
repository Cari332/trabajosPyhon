# Medrano Cardenas
#Pedir al usuario que ingrese una palabra
palabra = input("Palabra: ")

# Verificar si la palabra es un palíndromo 
# verificando que la palabra sea iual al reverso usando la tecnica de slicing [::1]
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")# si lo es
else:
    print("La palabra no es un palíndromo.")# si no lo es