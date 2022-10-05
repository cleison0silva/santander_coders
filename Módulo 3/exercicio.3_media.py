print("###########################")
print("PROGRAMA MÉDIA DOS ALUNOS")
print("##########################\n")

import csv

with open("alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    head_media = next(leitor)
    with open("alunos_media.csv", "w", encoding="utf-8", newline="") as arquivo_media:
        escrita = csv.writer(arquivo_media)
        head_media.append("Media")
        escrita.writerow(head_media)

        for linha in leitor:
            for coluna in range(3,7):
                linha[coluna] = float(linha[coluna])
            linha.append(sum(linha[3:7])/len(linha[3:7]))
            escrita.writerow(linha)




