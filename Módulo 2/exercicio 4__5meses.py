print("########################################")
print("PROGRAMA DICIONÁRIO DIAS DE CADA MÊS")
print("########################################\n")

dia_mes = {"jan": 31, "fev": 28, "mar": 31,"abr": 30, "mai": 31, "jun": 30, "jul": 31, "ago": 31, "set": 30, "out": 31, "nov": 30, "dez": 31}

for mes in dia_mes.keys():
    print(f'{mes} tem {dia_mes[mes]} dias')