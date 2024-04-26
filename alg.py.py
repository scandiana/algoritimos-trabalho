import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhacao!")
    palpite = int(input('digite seu palpite: '))

    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    
    while tentativas != palpite:

     if palpite < numero_aleatorio :
        print("Seu palpite e muito baixo. AUMENTE")
    
     elif palpite > numero_aleatorio:
        print("Seu palpite e muito alto. ABAIXE")
        
    else:
        print("Parabens! Voce acertou o numero")