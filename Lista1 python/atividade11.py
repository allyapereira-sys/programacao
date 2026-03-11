
dias_trabalhados = int(input("digite o numero de dias trbalhados sem acidentes"))

anos = dias_trabalhados // 365
meses = (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) %30

print(f"{dias_trabalhados} dias equivalen a {anos} anos,{meses} meses e {dias} dias.")


