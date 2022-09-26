distancia = float(input("Insira a distancia pecorrida: "))
tempo = float(input("Insira o tempo da viagem: "))

def calculaVelocidadeMedia(distancia, tempo):
    velocidadeMedia = distancia /tempo
    print("A velocidade média é de {0:.2f} km/h".format(velocidadeMedia))

calculaVelocidadeMedia(distancia, tempo)

calculaVelocidadeMedia(200, 30)