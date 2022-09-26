def calculaVelocidadeMedia(distancia, tempo):
    velocidadeMedia = distancia /tempo
    return velocidadeMedia


dist = float(input("Insira a distancia percorrida: "))
tempo = float(input("Insira o tempo da viagem: "))

print("A velocidade média é de {0:.2f} km/h".format(calculaVelocidadeMedia(dist, tempo)))



