#simulando PEDRA, PAPEL E TESOURA com o RANDIT, que é como um dado digital

from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print("1- Pedra")
print("2- Papel")
print("3- Tesoura")
jogador = int(input("escolha sua jogada: \n"))
print("=========================")
print(f"computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("====================")

if computador == 0:
    if jogador==1:
        print("EMPATE!!")
    elif jogador==2:
        print("VOCÊ GANHOU!!!!!!!!!")
    else:
        print("VOCÊ PERDEU!!!!")
    
elif computador == 1:
    if jogador==1:
        print("VOCÊ PERDEU!!!")
    elif jogador==2:
        print("EMPATE!!!!!!!!!")
    else:
        print("VOCÊ GANHOU!!!!")

elif computador == 2:
    if jogador==1:
        print("VOCÊ VENCEU!!!!!!!")
    elif jogador==2:
        print("VOCÊ PERDEU!!!!!!!!!")
    else:
        print("VOCÊ GANHOU!!!!")