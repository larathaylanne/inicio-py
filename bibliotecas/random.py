#biblioteca de sorteios

import random

a1 = input("Digite o nome de um aluno:")
a2 = input("Digite o nome de um aluno:")
a3 = input("Digite o nome de um aluno:")
a4 = input("Digite o nome de um aluno:")
a5 = input("Digite o nome de um aluno:")
a6 = input("Digite o nome de um aluno:")
a7 = input("Digite o nome de um aluno:")

lista = [a1, a2, a3, a4, a5, a6, a7]

random.shuffle(lista)

print("A ordem de apresentação será: \n")
print(lista)