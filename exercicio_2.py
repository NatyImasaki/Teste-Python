valorCompra = float(input("Informe o valor da compra: "))
cupom = input("Informe o cupom: ")

if cupom.upper() == "NIVER10":
    valorFinal = valorCompra * 0.9
else:
    valorFinal = valorCompra

print("O valor final da compra é de {0:.2f}".format(valorFinal))



