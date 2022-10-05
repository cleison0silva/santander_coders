print("#########################")
print("PROGRAMA ARQUIVOS CSV")
print("##########################\n")


import csv

with open("alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
