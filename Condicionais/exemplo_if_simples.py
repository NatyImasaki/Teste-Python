idade = input("Insira sua idade:")
rm = input("Insira se RM:")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}".format(rm))
    print("Mais instruções serão enviadas para seu e-mail cadastrado da FIAP!")
else:
    autorizado = input("Você possui autorização do responsavel? S-Sim ou N-não")
    if autorizado == 'S':
        print("Sua participação foi autorizada, aluno de RM {}".format(rm))
        print("Mais instruções serão enviadas para seu e-mail cadastrado da FIAP!")
    else:
        print("Sua participação foi negada devido a sua idade")




