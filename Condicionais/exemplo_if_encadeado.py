pontuacao = int(input("Insira a pontuação do cliente: "))

if pontuacao >= 1000:
    print("O cliente tem direito a 3gb na sua franquia de internet!")
elif pontuacao >= 500:
    print("O cliente tem direito a 1.5gb na sua franquia de internet!")
elif pontuacao >= 200:
    print("O cliente tem direito a 500mb na sua franquia de internet!")
else:
    print("O cliente não recebera bônus")
