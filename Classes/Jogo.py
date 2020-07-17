# -*- coding: utf-8 -*-

from Classes.Baralho import *
from Classes.Jogador import *

class Jogo():
    def __init__(self):
        self.baralho = Baralho()
        self.computador = Jogador("Computador")

    def novoJogo(self, nomeJogador):
        self.jogador = Jogador(nomeJogador)
        self.jogador.zerarPontuacao()
        self.computador.zerarPontuacao()
        self.baralho.novoBaralho()
        self.baralho.embaralhar()
        self.turno = 0
    
    def jogadorDoTurno(self):
        if self.turno == 0:
            return self.jogador
        return self.computador

    def pegarCarta(self):
        cartaRetirada = self.baralho.tirarCartaTopo()
        if (cartaRetirada):
            self.jogadorDoTurno().aumentarPontuacao(cartaRetirada.getValorInt())
        return cartaRetirada
    
    def isEstouro(self):
        if self.jogadorDoTurno().pontos > 21:
            return True
        return False
    
    def isVitoria(self):
        if self.jogadorDoTurno().pontos == 21:
            return True
        return False

    def desistir(self):
        self.jogadorDoTurno().desistir = True
    
    def trocarTurno(self):
        if self.turno == 0:
            self.turno = 1
        else:
            self.turno = 0
    

    
