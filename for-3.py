#mostrando apenas números pares na tela

for n in range (0, 501, 2):
    if n % 3 == 0:
        print(n, end=" ")