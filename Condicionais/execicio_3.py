import math

a = float(input("Insira o valor de A"))
b = float(input("Insira o valor de B"))
c = float(input("Insira o valor de C"))

delta = b * b - 4 * a * c

print(delta)

if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2={}".format(a, b, c, x1, x2))
elif delta == 0:
    x = (-b - math.sqrt(delta)) / 2 * a
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x = {}".format(a, b, c, x))
else:
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))