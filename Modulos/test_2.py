#importando funções especificas do modulo calc
from calc import somar, subtrair
#para importar todas as funções do modulo, usamos o import abaixo
# from calc import *

valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")

#importando as funções especificas não precisamos escrever o nome do modulo. exemplo: calc.somar()
soma = somar(valor1, valor2)
subtracao = subtrair(valor1, valor2)

print(soma)
print(subtracao)