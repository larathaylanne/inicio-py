print("====LOJA DA LARA====")
preco = float(input("Preço das compras: \n"))
print("FORMAS DE PAGAMENTO")
print("1- À vitas")
print("2- À vista no cartão")
print("3- 2x cartão")
print("4- 3x ou mais no cartão")
opcao = int(input("Digite uma opção:\n"))

if (opcao == 1):
    valor= preco-(preco*10/100)
    print(f"O valor total é:{valor}")
elif (opcao == 2):
    valor= preco-(preco*5/100)
    print(f"O valor total é:{valor}")
elif (opcao == 3):
   print(f"O valor total é:{preco}")
else:
    valor= preco+(preco*20/100)
    print(f"O valor a ser pago é: {valor}")
    