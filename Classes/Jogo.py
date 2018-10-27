# -*- coding: utf-8 -*-

from Classes import Baralho
import os

class Jogo():
    def __init__(self):
        self.baralho = Baralho.Baralho()
        self.baralho.embaralhar()
        self.pontos = 2 * [0]
        self.lixo = Baralho.Lixo()
        self.rodada = 1
        print ('Pontos - jogador 1:', self.pontos[0])
        print ('Pontos - jogador 2:', self.pontos[1], '\n')

    def pegar(self, quantidade = 1):
        self.rodada = self.rodada + 1
        for i in range(quantidade):
            if self.baralho.carta == []:
                print ('O baralho acabou')
                break
            self.lixo.carta.append(self.baralho.carta[-1])
            retirada = self.baralho.carta.pop()
            self.pontos[self.rodada % 2] += retirada.valor
            print (retirada)
            print ('Pontos - jogador 1:', self.pontos[0])
            print ('Pontos - jogador 2:', self.pontos[1], '\n')
            
            if self.pontos[self.rodada % 2] == 21:
                os.system('cls || clear')
                print ('O jogador', (self.rodada % 2) + 1, 'ganhou\n')
                self.__init__()
            elif self.pontos[self.rodada % 2] > 21:
                os.system('cls')
                print ('Estourou, jogador', ((self.rodada + 1) % 2) + 1, 'ganhou\n')
                self.__init__()

    def fugir(self):
        os.system('cls || clear')
        print ('O jogador', ((self.rodada + 1) % 2) + 1, 'fugiu\n')
        rodada = self.rodada + 1
        if rodada % 2 == 0:
            while (self.pontos[1] < self.pontos[0]):
                self.rodada = rodada
                print ('Jogador 2')
                self.pegar()
        else:
            opcao = 1
            while opcao != 0 or self.pontos[0] < self.pontos[1]:
                opcao = input()
                os.system('cls || clear')
                print ('Jogador 1')
                if opcao == '1':
                    self.rodada = rodada
                    self.pegar()
                elif opcao == '2':
                    self.fugir()
                else:
                    print('Erro: Opção inválida')

        if self.pontos[0] > self.pontos[1]:
            print ('O jogador 1 ganhou')
        else:
            print('O jogador 2 ganhou')
        self.__init__()

    def prob(self):
        p = 56
        if self.pontos[1] >=  8:
            p = (21 - self.pontos[1]) * 4
            for carta in self.lixo.carta:
                if carta.valor <= (21 - self.pontos[1]):
                    p = p - 1

        p = p / 56
        p = p * 100
        return p

    def j2(self):
        if (self.pontos[0] < self.pontos[1]) and self.prob() <= 30:
            self.fugir()
        else:
            self.pegar()
