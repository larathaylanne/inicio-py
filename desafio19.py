import random

n1 = input("primeiro aluno: \n")
n2 = input("segundo aluno: \n")
n3 = input("terceiro aluno: \n")
n4 = input("quarto aluno: \n")
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))