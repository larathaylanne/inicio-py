i = int(input("Por onde vc vai começar? \n"))
f = int(input("Onde você quero chegar? \n"))
p = int(input("Quais passos você quer pisar? \n"))

for n in range(i, f+1, p):
    print(n)