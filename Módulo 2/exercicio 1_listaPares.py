print("####################################")
print("PROGRAMA NÚMEROS PARES DE UMA LISTA")
print("####################################\n")

lista = [1,2,3,4,5,6,7,8,9,10]
total = []

print(f"Lista: {lista}")

for i in lista:
    if i % 2 == 0:
        total.append(i)

print(f"A quantidade de números pares é: {len(total)}")

