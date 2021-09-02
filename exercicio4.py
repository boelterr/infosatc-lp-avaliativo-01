#Gabriel Custodio Boelter 2190 

p = float(input("Digite o valor do premio:"))

d = p*(7/100)

desconto = (p-d)

p1 = desconto-(desconto*(46/100))

p2 = (desconto)*(32/100)

p3 = desconto-(p1+p2)

print("O total do premio foi: R${}".format(p))
print("O valor do premio com os impostos é de: R${}".format(desconto))
print("O valor descontado do premio foi de: R${}".format(desconto))
print("O primeiro ganhador recebeu: R${}".format(p1))
print("O segundo ganhador recebeu: R${}".format(p2))
print("O terceiro ganhador recebeu: R${}".format(p3))