# -*- coding: utf-8 -*-

class Carta:
    def __init__(self, naipe, valor):
        self.listanaipes = ['Copas', 'Paus', 'Ouros', 'Espadas']
        self.listavalores = ['Coringa', 'Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                        'Valete', 'Dama', 'Rei']
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return (self.listavalores[self.valor] + ' de ' + self.listanaipes[self.naipe])
