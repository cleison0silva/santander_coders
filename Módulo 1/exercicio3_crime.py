print("#############################")
print("PROGRAMA QUEM É O ASSASSINO")
print("#############################\n")

print("RESPONDA S ou N\n")
endereco = input("Mora perto da vítima? ")
trabalho = input("Já trabalhou com a vítima? ")
telefone = input("Telefonou para a vítima? ")
local = input("Esteve no local do crime? ")
divida = input("Devia para a vítima? ")

pontos = 0

if endereco == "S":
    pontos += 1
if trabalho == "S":
    pontos += 1
if telefone == "S":
    pontos += 1
if local == "S":
    pontos += 1
if divida == "S":
    pontos += 1

print("Total de Pontos: ", pontos)

if pontos == 5:
    print("A pessoa é o Assassino")
elif pontos >= 3:
    print("A pessoa é Cúmplice")
elif pontos == 2:
    print("A pessoa é Suspeita")
else:
    print("A pessoa está Liberada")