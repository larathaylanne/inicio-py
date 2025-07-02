#O DESAFIO ERA CRIAR UM PROGRAMA QUE LESSE AS NOTAS DE UM ALUNO, CALCULASSE E MOSTRASSE A MÉDIA

print("Olá, jovem prodígio. \n")
nota-mat=float(input("Digite aqui sua nota de matemática: \n"))
nota-port= float(input("Agora digite aqui sua nota de Português: \n"))
nota-cie= float(input("Nota ciências: \n"))
nota-hist= float(input("Nota história: \n"))
nota-geo= float(input("POr fim, sua nota de geografia: \n"))

media = (nota-mat + nota-port + nota-cie + nota-hist + nota-geo) / 5

print("Legal. A média das suas notas foi: ",media)