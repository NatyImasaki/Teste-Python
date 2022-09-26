quantTransacoes = int(input("Informe a quantidade de transações efetuadas no dia: "))
totalGastos = 0

for x in range(1, quantTransacoes + 1):
    gastos = float(input("Informe o valor da transação {} ".format(x)))
    totalGastos = totalGastos + gastos

media = totalGastos/quantTransacoes

print("O total dos gastos diários foi de {}".format(totalGastos))
print("A média das transações diarias foram de {0:.2f}".format(media))