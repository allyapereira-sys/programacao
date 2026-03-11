hora_normal = 10
hora_extra = 15
hora_normal = float(input("Digite a quantidade de horas trabalhadas"))
hora_extra = float(input("Digite a quantidade de horas extras"))
salário_bruto= (hora_normal*10)+(hora_extra*15)
salario_liquido= salário_bruto-(salário_bruto*0.10)
print("o salário bruto é",salário_bruto)
print("o salário liquido é",salario_liquido)





