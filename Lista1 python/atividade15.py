total = float(input("Digite o valor total da compra: "))

valor_por_pessoa = total / 3 


Carlos =int(valor_por_pessoa)
André =int(valor_por_pessoa)

Felipe = total - (Carlos + André)

print ("carlos deve pagar em R${:.2f}".format(Carlos))
print ("André deve pagar em R${:.2f}".format(André))
print ("Felipe deve pagar em R${:.2f}".format(Felipe))
