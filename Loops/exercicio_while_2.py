pesoTotal = 0.0

for x in range(1, 101):
    pesoAtual = float(input("Insira o peso da caixa atual: "))

    pesoTotal = pesoTotal + pesoAtual

media = pesoTotal/100
print("O peso total das caixas é de {}."
      "A média de dos pesos é de {}.".format(pesoTotal, media))
