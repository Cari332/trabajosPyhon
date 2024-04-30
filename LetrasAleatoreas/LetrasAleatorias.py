import random
#MedranoCardenas
# Función para convertir números en letras
def Aleatorio(num):
    if num == 1:
        return 'a'
    elif num == 2:
        return 'b'
    elif num == 3:
        return 'c'
    else:
        return None

# Generamos números aleatorios del 1 al 3 y los convertimos en letras
random_numbers = [random.randint(1, 3) for _ in range(3)]
random_letters = [Aleatorio(num) for num in random_numbers]

# Imprimimos las letras aleatorias
print("Letras aleatorias:", random_letters)
