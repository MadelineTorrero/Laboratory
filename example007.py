
cantidad = int(input("¿Cuántas estrellas quieres ver?: "))


print("Mostrando con bucle:")
for i in range(cantidad):
    print("*", end="")
print()  # Salto de línea


print("Mostrando de forma directa:")
print("*" * cantidad)