numero = -1
for _ in range(3):
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break
print("voce digitou: ", numero)