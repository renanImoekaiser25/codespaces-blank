'''
Game Par Impar
2025.06.25
Renan Soares da Silva
'''

# OBJETOS:


# BIBIOTECAS:
from modules import *

# COSTANTE:
limite = 10

# VARIAVEIS:
escolha = ''
msg = ''



# LISTAS:
msgsCab = ['JOGO PAR OU ÍMPAR','Desenvolvio por Renan Soares']
msgsMenu = ['Escolha:','[0] para Par',"[1] para Ímpar"]


# FUNÇÃO:


# FUNÇÃO PRINCIPAL DO JOGO:
def playGame():
    global escolha, msg, msgsCab, msgsMenu
    LimpaTela()
    MostraCabecalho(msgsCab)
    MM(msgsMenu)
    msg = '-> Sua escolha'
    escolha = gatValue(msg)
    opcoes = ['0','1']
    while not ValidaValue(escolha,opcoes):
        escolha = gatValue
    msg = '-> Sua jogada:'
    userJogada = gatValue(msg)
    while not userJogada.isdigit():
        userJogada = gatValue(msg)
    userJogada = int(userJogada)
    pcJogada = sortNum(limite)
    result = userJogada + pcJogada
    if (result%2 ==0) and escolha == 0:
        ganhador = 'Jogador'
    elif (result%2 !=0) and escolha == 1:
        ganhador = 'Jogador'
    else:
        ganhador = 'PC'
    MSGS = [f'PC Jogou: {pcJogada}', f'Jogador jogou: {userJogada}', f'Resultado: {result}', f'Ganhador: {ganhador}']
    MostraCabecalho(MSGS)
    if playAgain():
        playGame()
    else:
        MostraCabecalho(['Obrigado por Jogar', ' Até a próxima'])
        


    




# CÓDIGO PRINCIPAL:
playGame()