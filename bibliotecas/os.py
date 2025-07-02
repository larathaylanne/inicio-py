import os
import os
os.system('cls')

print('''
      =======MENU=======
        1- Entrar
        2- Avançar de nível
        3- Sair
      ''')

try:
    # Correção aplicada aqui (.strip() com parênteses)
    opcao_escolhida = int(input('Escolha uma opção: \n').strip())

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
    print('Por favor digite uma alternativa válida (1, 2 ou 3)')