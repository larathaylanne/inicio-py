def escolhar_opcao():
    print("1- cadastro")
    print("2- ativar")
    print("3- sair")   
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            print("cadastrar restaurante: ")
        elif opcao_escolhida == 2:
            print("Ativar restaurante")
        elif opcao_escolhida == 3:
            print("saindo")
        else:
            print("Opção inválida")
    except:
        print("Opção inváloda")