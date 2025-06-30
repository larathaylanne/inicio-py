import os

#Biblioteca no python que permite a interação com o sistema operacional do meu computador

os.system('calc')

nome_no_pc = os.getlogin()
print(f'O computador me conhece como: {nome_no_pc}')

os.system('cls')