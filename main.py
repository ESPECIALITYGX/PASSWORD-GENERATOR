import random

elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int( input("Ingresa el numero de caracteres q deseas en tu contraseña:") )

password = ""

for i in range( size ):
    password += random.choice(elementos)

print(password)