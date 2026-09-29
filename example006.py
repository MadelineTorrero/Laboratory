import random

numero_secreto = random.randint(1, 10)
intento = 0

print("¡Adivina el número secreto entre 1 y 10!")

while intento != numero_secreto:
    intento = int(input("Introduce tu número: "))
    
    if intento < numero_secreto:
        print("Más alto... ¡Inténtalo de nuevo!")
    elif intento > numero_secreto:
        print("Más bajo... ¡Inténtalo de nuevo!")
    else:
        print("¡Felicidades! ¡Adivinaste el número!")