import os
os.system('cls')

print('''
      =======MENU=======
        1- Entrar
        2- Avançar de nível
        3- Sair
      ''')
try:
    opcao_escolhida = int(input('Escolha uma opção: \n'))

    match opcao_escolhida:
        case 1:
            print('Você entrou!')
        case 2:
            print('Você avançou de nível!')
        case 3:
            print('Você saiu!')
        case _:
            print('Opção inválida')

except ValueError:
    print('Por favor digite um alternativa válida (1, 2 ou 3)')