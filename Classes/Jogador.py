# -*- coding: utf-8 -*-

class Jogador():
    def __init__(self, nome):
        self.pontos = 0
        self.nome = nome
        self.desistir = False

    def zerarPontuacao(self):
        self.pontos = 0
        self.desistir = False
    
    def aumentarPontuacao(self, valor):
        self.pontos += valor
    
    def calcProbCartaBoa(self, valores):
        #verifica a probabilidade de tirar uma carta boa
        #entende-se por carta boa uma carta que não fará a pontuação estourar
        #Probabilidade = nCartasBoas / totalDeCartas
        cartasBoas = 0
        for v in valores:
            if (v <= (21 - self.pontos)):
                cartasBoas += 1
            
        if (len(valores) == 0):
            return 0
        return cartasBoas / len(valores)