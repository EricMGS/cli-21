# -*- coding: utf-8 -*-

from Classes import Cartas
from random import randrange

class Baralho:
    def __init__(self):
        self.carta = []
        for naipe in range(4):
            for valor in range(13):
                self.carta.append(Cartas.Carta(naipe, valor))

    def __str__(self):
        s = ''
        for i in range(len(self.carta)):
            s = s + ' ' * i + str(self.carta[i]) + '\n'
        return s
    
    def embaralhar(self):
        for i in range(len(self.carta)):
            r = randrange(i, len(self.carta))
            self.carta[i], self.carta[r] = self.carta[r], self.carta[i]

class Lixo:
    def __init__(self):
        self.carta = []

    def __str__(self):
        s = ''
        for i in range(len(self.carta)):
            s = s + ' ' * i + str(self.carta[i]) + '\n'
        return s
