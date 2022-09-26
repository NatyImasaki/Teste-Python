#criando uma lista
jedi = ["Yoda", "Luke", "Obi-wan", "Anakin"]
#adicionando um elemento no final da lista
jedi.append("Mace Windu")
#pedindo para o usuario adicionar no final da lista
jedi.append(input("Insira o nome de um Jedi: "))
#adicinando um elemento e um indice especifico
jedi.insert(1, "Ahsoka Tano")
#pedindo para o usuario adicionar em um indice especifico
jedi.insert(2, input("Insira o nome de um jedi: "))

# print(jedi)
# print(jedi[2])

for nome in jedi:
    print(nome)