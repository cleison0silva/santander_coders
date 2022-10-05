print("#############################")
print("PROGRAMA VALIDAR INFORMAÇÕES")
print("#############################\n")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Valor inválido, digite novamente: "))

salario = float(input("Digite o salário: "))
while salario < 0:
    salario = int(input("Valor inválido, digite novamente: "))

sexo = input("Digite o sexo: ")
while sexo != "M" and sexo != "F" and exo != "Outro":
    sexo = input("Valor inválido, digite novamente: ")

print(f"Sua Idade é: {idade} anos, \nSeu salário é: {salario} \nE seu sexo é: {sexo}")

