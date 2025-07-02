'''
Arquivo de funções utilizadas
2025.06.25
Renan Soares da Silva

'''
# BIBLIOTECA:
from random import randint
from time import sleep

# CONSTANTES:
MAR = int(1)
TAM = int(60)
CAR = "#"

# VÁRIAVEIS:

# LISTAS:

# FUNÇÕES:

def LimpaTela():
    print('\n'*TAM)

def Linha():
    print(F'{CAR}'*TAM)

def msgCenter(msg):
    print(f'{CAR}{msg:^{TAM-MAR-MAR}}{CAR}')

def msgLeft(msg):
        print(f'{CAR}{msg:<{TAM-MAR-MAR}}{CAR}')

def MostraCabecalho(msgs):
    Linha()
    for msg in msgs:
        msgCenter(msg)
    Linha()

def MM(msgs): #mostra menu
    for msg in msgs:
        msgLeft(msg)
    Linha()

def sortNum (limite):
    key = randint(1, limite)
    return key

def ValidaValue(reps, opcoes):
    if reps in opcoes:
        return True
    else:
        MSGS = [f'{reps} não é uma opção validada!', f'Escolha entre {opcoes}']
        MM(MSGS)
        return False

def gatValue(msg):
    reps = input(f'{CAR}{msg}: ').strip()
    return reps

def mostraDica(reps,key):
    if reps > key:
        MostraCabecalho(['Tente um número menor!'])
    else:
        MostraCabecalho(["tente um numero maior!"])

def playAgain():
    opcoes = ['1','0']
    MostraCabecalho(["Deseja joga novamente?",'[1] sim', '[0] não'])
    reps = gatValue('Escolha uma opção')
    return reps == '1'

# pixelX = 10
# pixelY = 10
# i = 0
# msg = ''
# for i in range(50):
#     i += 1
#     if i == pixelX and pixelY:
#         msg += '*'
#     else:
#         msg += '0'
#     if i == 25:
#         msg += '\n'
# print(msg)
# largura = 50
# altura = 10
# tabuleiro = []
# linha = []
# msg = '0'*largura
# for i in range(altura):
#     if i == 3 :
#         msg = 'teste'
#     else:
#         msg = '0'*largura
#     linha.append(msg)

# tabuleiro.append(linha)

# for l in tabuleiro :
#    for t in l :
#        print(t)

# # print(tabuleiro[1][4])