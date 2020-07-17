# -*- coding: utf-8 -*-

from random import randrange

class Carta():
    def __init__(self, naipe, valor):
        self.listaNaipes = ['Copas', 'Paus', 'Ouros', 'Espadas']
        self.listaValores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                        'Valete', 'Dama', 'Rei'] #1-indexed
        self.naipe = naipe #int
        self.valor = valor #int

    def getValorString(self):
        return self.listaValores[self.valor - 1]

    def getValorInt(self):
        return self.valor

    def getNaipeString(self):
        return self.listaNaipes[self.naipe]

    def getNaipeInt(self):
        return self.naipe

class Baralho(list):
    def novoBaralho(self):
        self.clear()
        #Append de todas as cartas no baralho
        for naipe in range(4):
            for valor in range(1, 12):
                self.append(Carta(naipe, valor))

    def embaralhar(self):
        #Itera todas as cartas do baralho e troca de posição com outra
        for carta in range(len(self)):
            troca = randrange(len(self))
            self[carta], self[troca] = self[troca], self[carta]


    def tirarCartaTopo(self):
        if(len(self)): #Verifica se o baralho não está vazio
            return self.pop(0) #retorna objeto Carta
        return None

    def getValores(self):
        return list(map(lambda x: x.getValorInt(), self))
        