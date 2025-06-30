
#removendo a parte decimal de um número

from math import trunc
n = float(input("diga um número quebrado: \n"))

print("A quebra de {} é {}".format(n,trunc(n)))