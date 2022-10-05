print("########################################")
print("PROGRAMA SOMA ENTRE ELEMENTOS DE LISTAS")
print("########################################\n")

lista1 = []
lista2 = []
total = []

print("Digite duas listas com a mesma quantidade de elementos\n")

resposta = input("Informe a primeira lista de números, separados por vírgula: ")
lista1 = list(map(int,resposta.split(",")))

resposta = input("Informe a segunda lista de números, separados por vírgula: ")
lista2 = list(map(int, resposta.split(",")))

for l1, l2 in zip(lista1,lista2):
    soma = l1 + l2
    total.append(soma)
print(f"A soma entre os elementos das duas lista são: {total}")

