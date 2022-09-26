emailAluno = input("Informe o e-mail do aluno: ")
notaSemestral = float(input("Informe a nota semestral do aluno: "))

if notaSemestral >= 8.5:
    print("Enviando e-mail para {} ".format(emailAluno))

