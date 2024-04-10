# Captura de datos
#Medrano
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
email = input("Ingrese su dirección de correo electrónico: ")
# Impresión del mensaje con colores difaerentes
print("Mi nombre es \033[1;35m{}\033[0m, tengo \033[1;30m{}\033[0m años y se enviará un correo electrónico a la siguiente dirección \033[1;33m{}\033[0m.".format(nombre, edad, email))