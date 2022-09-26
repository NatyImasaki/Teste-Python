numeroInt = int(input("Insira um numero inteiro: "))
anterior1 = 1
anterior2 = 0
for i in range(1, numeroInt + 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numeroInt == atual:
        print("Ação bem sucedida!")
        break
    elif numeroInt < atual:
        print("A ação falhou...")
        break
