nome = str(input("Digite seu nome completo: \n")).strip()
print("Analisando seu nome: \n")
print("Seu nome em maiúculas é: \n {}".format(nome.upper()))
print("Seu nome em minúsculas é: \n{}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome)-nome.count(" ")))

print("Seu primeiro nome tem {} letras".format(nome.find(" ")))

separa = nome.split()
print("seu primeiro nome é {} e tem {} letras ".format(separa[0], len(separa[0])))