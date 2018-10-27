# -*- coding: utf-8 -*-

from Classes import Jogo
import os

os.system('cls || clear')
print ('Seu objetivo é acumular 21 pontos apartir do 0')
print ('Cada carta possui um valor que será somado aos pontos quando retirada')
print ('Se os pontos pasarem de 21 você perde, por isso você pode escolher fugir')
print ('Digite 1 para pegar uma carta, 2 para fugir ou 0 para sair\n\n')

j = Jogo.Jogo()

opcao = 1
while (opcao != '0'):
    if j.rodada % 2 == 0:
        print ('Jogador 2')
        j.j2()
    else:
        opcao = input()
        os.system('cls || clear')
        print ('Jogador 1')
        if opcao == '1':
            j.pegar()
        elif opcao == '2':
            j.fugir()
        else:
            print('Erro: Opção inválida')

