#escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

print("Olá!")
numero = int(input("digite um número \n"))
print("1- binário")
print("2- octal")
print("3- hexadecimal")
escolha = input(f"como você quer converter {numero}? \n")

if (escolha == '1'):
    print(f"{numero} convertido para binário é {bin(numero)}[2:]")
    
elif (escolha == '2'):
    print(f"{numero} em octal é {oct(numero)}[2:]")

else:
    print(f"{numero} em hexadecimal é {hex(numero)}[2:]")