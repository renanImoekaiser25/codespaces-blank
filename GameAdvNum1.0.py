from random import randint
from time import sleep
from modules import LimpaTela, Linha, msgCenter, msgLeft, MostraCabecalho, MM, sortNum, ValidaValue, gatValue,  mostraDica, playAgain 

vida = 0
key = 0
reps = 0
vida = 0
msg = ''
limite = 0
tentativa = 0

MAR = int(1)
TAM = int(50)

MSGS = []
msgsCab = ['JOGO DO ADIVINHE O NÚMERO','Feito por Renan']
msgsLevel = ['NÍVEIS DE DIFICULDADE','[1] Facíl (1 a 10)','[2] dificil (1 a 100)','[3] Impossivel (1 a 1000)']



def playGame():
    global key, reps, vidas, limite, tentativas, MSGS
    LimpaTela()
    MostraCabecalho(msgsCab)
    MM(msgsLevel)
    msg = '-> Digite o número correspondente ao nivel'
    reps = gatValue(msg)
    opcoes = ['1', '2', '3']
    while not ValidaValue(reps, opcoes):
        reps = gatValue(msg)
    if reps == '1':
        vidas = 3
        limite = 10
    elif reps == '2':
        vidas = 5
        limite = 100
    elif reps == '3':
        vidas = 10
        limite = 1000
    key = sortNum (limite)
    LimpaTela()
    sleep(1)
    MostraCabecalho(msgsCab)
    MostraCabecalho([f'Adivinhe o numero entre 1 e {limite}', f"Você tem {vidas} tentativas"])
    for tentativa in range(vidas):
        msg = f'Tentativa {tentativa+1}/{vidas} -> seu palpite'
        reps = gatValue(msg)
        while not reps.isdigit():
            MostraCabecalho(['Entrada inváliida! Por favor, insira um número.'])
            reps = gatValue(msg)
        reps = int(reps)
        if reps ==  key :
            sleep(1)
            MostraCabecalho(['Parabéns!!!', 'Você acertou o número'])
            break
        else:
            if tentativa < vidas - 1:
                sleep(1)
                MostraCabecalho(['Número incorreto',f'Você ainda tem {vidas - tentativa - 1} tentativas'])
                mostraDica(reps, key)
    else:
        sleep(1)
        MostraCabecalho(['que pena...', f'O número secreto era {key}', "fim de jogo"])
    if playAgain():
        playGame()
    else:
        MostraCabecalho(["obrigado por jogar", "Até a próxima!"])
playGame()