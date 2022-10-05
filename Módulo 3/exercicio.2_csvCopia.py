print("###########################")
print("PROGRAMA ARQUIVOS CÓPIA CSV")
print("##########################\n")

import csv

with open("alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    with open("alunos_copia.csv", "w", encoding="utf-8", newline="") as arquivo_copia:
        escrita = csv.writer(arquivo_copia)
        for linha in leitor:
            escrita.writerow(linha)