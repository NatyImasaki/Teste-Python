quantAlimento = int(input("Informe a quantidade de alimentos consumidos no dia: "))
totalCalorias = 0

for c in range(1, quantAlimento + 1):
    calorias = float(input("Informe a caloria do alimento {} ".format(c)))
    totalCalorias = totalCalorias + calorias

print("O total de calorias consumidas no dia foi de {}".format(totalCalorias))