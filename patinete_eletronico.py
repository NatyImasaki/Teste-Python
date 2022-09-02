print("Este programa calcula a velocidade média de um patinete")
distancia = input("Insira a distancia percorrida pelo patinete em metros: ")
tempo = input("Quantos minutos o petinete demorou para percorrer a distancia: ")
velocidade_media = float(distancia) / float(tempo)

print("A velociade média é: {0:.2f}".format(velocidade_media))