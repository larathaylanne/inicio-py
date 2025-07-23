num = int(input("Informe um número de a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisnado o número",num)
print("A unidade é ",u)
print("A dezena é ",d)
print("A centena é ",c)
print("A milhar é ",m)