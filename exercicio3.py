#Gabriel Custodio Boelter 2190

h = float(input("Digite a altura da parede: "))#Entrada das variaveis n1,n2,n3,4 pedindo para lhe dar um valor
c = float(input("Digite o comprimento da parede: "))

m = (h*c) #equação de metros quadrados

consumolitros = (m/3) #equação do consumo de litros de tinta

latas = consumolitros/ 3.6 #equação da quatidade de latas

vt = (latas * 107) #valor total


print("A quantidade de latas é de {}" .format(latas))#Print na tela mostrando a quantidade de latas
print("E o valor total é de {}" .format(vt))#Print na tela com o valor total
