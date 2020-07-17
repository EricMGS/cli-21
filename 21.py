# -*- coding: utf-8 -*-

from Classes.Jogo import *
import os

def limparTela():
    fail = os.system('cls')
    if(fail):
        os.system('clear')

def mostrarInstrucoes():
    instrucoes = '''INSTRUÇÕES\n
    O QUE É?
        21 é um jogo de cartas de dois jogadores
        Cada jogador começa com uma pontuação igual a 0
        A cada turno um jogador retira uma carta do topo do baralho
        O valor da carta retirada será somado a pontuação do jogador\n
    E QUEM GANHA?
        O objetivo do jogo é alcançar 21 pontos
        Se um jogador alcançar 21 pontos antes do outro ele ganha
        Porém se sua pontuação ultrapassar 21 pontos ele perde
        Para não estourar(ultrapassar 21 pontos) um jogador pode desistir
        Quando ele desiste o outro jogador poderá continuar retirando cartas
        até desistir ou estourar
        Se o jogador restante estourar o que desistiu ganha
        Porém se ele desistir ganha o jogador com maior pontuação\n
        '''
    print(instrucoes)
    print("Pressione Enter para continuar...")
    input()
    print(instrucoes)

def mostrarPontuacao(jogo):
    print("TURNO: " + jogo.jogadorDoTurno().nome + '\n')
    print("PONTUAÇÃO")
    print(jogo.jogador.nome, ":", jogo.jogador.pontos, end='')
    if(jogo.jogador.desistir): print(" DESISTIU", end='')
    print()
    print(jogo.computador.nome, ": ", jogo.computador.pontos, end='')
    if(jogo.computador.desistir): print(" DESISTIU", end='')
    print()

def mostrarOpcoes(jogo):
    print("\nOPÇÕES")
    print("1- Pegar carta")
    print("2- Desistir")
    print("3- Mostrar instruções")
    print("0- Sair do jogo")
    print("\nDigite a opção: ", end='')

def sairDoJogo():
    print("\n\nDeseja mesmo sair? s/n ", end='')
    opcao = input()
    opcao = opcao.upper()
    if(opcao == "S"):
        exit()

def anunciaVencedor(vencedor):
    print('\n')
    print("Fim de jogo!")
    print("Vencedor: " + vencedor)

def anunciaEmpate():
    print('\n')
    print("Fim de jogo!")
    print("Empate!")

def fimDeJogo(jogo):
    print()
    print("Deseja jogar outra vez? s/n")
    opcaoIncorreta = True
    while(opcaoIncorreta):
        opcao = input()
        opcao = opcao.upper()
        if(opcao == "N"):
            exit()
        elif(opcao == "S"):
            opcaoIncorreta = False
    
    limparTela()

def iniciarJogo(jogo):
    while(True):
        print("Digite seu nome para jogar ou 0 para sair: ")
        opcao = input()
        if opcao == "0":
            sairDoJogo()
        else:
            jogo = Jogo()
            jogo.novoJogo(opcao)
            jogar(jogo)
            fimDeJogo(jogo)

def jogar(jogo):
    emJogo = True
    while(emJogo):
        if (jogo.jogador.desistir and jogo.computador.desistir):#Se ambos desistiram
            if(jogo.jogador.pontos == jogo.computador.pontos):
                anunciaEmpate()
            elif(jogo.jogador.pontos > jogo.computador.pontos):
                anunciaVencedor(jogo.jogador.nome)
            else:
                anunciaVencedor(jogo.computador.nome)
            emJogo = False
        else:
            limparTela()
            turno(jogo)
            if(jogo.isVitoria()):
                anunciaVencedor(jogo.jogadorDoTurno().nome)
                emJogo = False
            elif(jogo.isEstouro()):
                jogo.trocarTurno()
                anunciaVencedor(jogo.jogadorDoTurno().nome)
                emJogo = False
            else:
                jogo.trocarTurno()
                if (jogo.jogadorDoTurno().desistir): #Se o jogador desistiu troca de novo
                    jogo.trocarTurno()

def pegarCarta(jogo):
    limparTela()
    carta = jogo.pegarCarta()
    if(carta):
        print("Carta retirada: ", end='')
        print(carta.getValorString() + " de " + carta.getNaipeString())
        print()
    else:
        print('Baralho vazio')
        print()
    mostrarPontuacao(jogo)
    print("\nPressione Enter para continuar...")
    input()

def turno(jogo):
    opcaoIncorreta = True
    while(opcaoIncorreta):
        mostrarPontuacao(jogo)
        if (jogo.jogadorDoTurno().nome == jogo.jogador.nome): #Turno do jogador
            mostrarOpcoes(jogo)
            opcao = input()
            if(opcao == "1"): #pegar carta
                pegarCarta(jogo)
                opcaoIncorreta = False
            elif(opcao == "2"): #desistir
                jogo.desistir()
                opcaoIncorreta = False
            elif(opcao == "3"): #instruções
                limparTela()
                mostrarInstrucoes()
                limparTela()
            elif(opcao == "0"): #sair
                sairDoJogo()
        else: #Turno do computador
            if(jogo.jogador.desistir == False): #Se o jogador não desistiu
                #Calcula probabilidade de pegar carta boa
                prob = jogo.computador.calcProbCartaBoa(jogo.baralho.getValores())
                if(prob > 0.6): #constante de comportamento do computador
                    pegarCarta(jogo)
                else:
                    jogo.desistir()
            else: #Se o jogador desistiu
                if(jogo.computador.pontos > jogo.jogador.pontos):
                    jogo.desistir()
                else:
                    pegarCarta(jogo)
            opcaoIncorreta = False

if __name__ == "__main__": 
    limparTela()
    print("\nBem-vindo!!!\n")
    mostrarInstrucoes()
    limparTela()
    jogo = Jogo()
    iniciarJogo(jogo)
