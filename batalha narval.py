from modules import * # importa a função basicas para o interface do jogo
from time import sleep # importa a funçaõ de esperar um tempo indeterminado

px = 0 #criação de variavel
msglevel = 'fácil[1]','médio[2]','difícil[3]' # criação das variaveis 
msgtexto = '' # criação das variaveis 
key = [0,0] # criação das variaveis 
kay2 = 0 # criação das variaveis  
i = -1 # criação das variaveis 

def jogo():
    vidaIA = 3 # criação das variaveis fixas 
    vidaPss = 3 # criação das variaveis fixas 
    LimpaTela() #parte de interface do jogo, limpa a tela
    Linha() #parte de interface do jogo,cria uma linha
    msgCenter('Batalha naval') #parte de interface do jogo, mostra um texto 
    Linha() # cria uma linha
    msgLeft('escolha uma dificuldade') # mostra uma msg a esquerda
    MostraCabecalho(msglevel) # mostra um cabeçalho com todas as informações dentro da variavel
    msg = 'Selecione a Difículdade' # variavel para guardar um texto
    resp = gatValue(msg) # verificação de entrada 
    opcoes = ['1', '2', '3'] # opções das possíveis entradas
    while not ValidaValue(resp,opcoes): # sistema de verificação que ira definir a dificuldade
        resp = gatValue(msg)# novamente uma verificação de entrada dentro do loop
    if resp == '1': # verificação caso a resposta seja 1
        tamanhoXY = 5 # difinição da variavel para tamanho do campo 
        ncpNivel = 10 # definição para difículdade
    elif resp == '2': # verificação caso a resposta seja 2
        tamanhoXY = 6 # difinição da variavel para tamanho do campo
        ncpNivel = 5 # definição para difículdade
    elif resp == '3': # verificação caso a resposta seja 3
        tamanhoXY = 7 # difinição da variavel para tamanho do campo
        ncpNivel = 2 # definição para difículdade
    LimpaTela() # limpa tela
    Linha() #  cria uma linha
    msgLeft(f'Você pode selecionar 3 barcos na posição x,y 1 até x,y {tamanhoXY} ') # mostra uma msg a esqueda
    msgLeft('digite a posição dos seus barcos',) # mostra uma msg a esquerda
    barco1 =  list(map(int,input('barco 1 -> ').split(','))) # pega a entrada do jogador do barco 1 e transforma em inteiro/número
    barco2 =  list(map(int,input('barco 2 -> ').split(','))) # pega a entrada do jogador do barco 1 e transforma em inteiro/número
    barco3 =  list(map(int,input('barco 3 -> ').split(','))) # pega a entrada do jogador do barco 1 e transforma em inteiro/número
    px = (f'{barco1}',f'{barco2}',f'{barco3}') #organização das posições para mostrar pro jogador
    Linha() # cria uma linha
    msgCenter('Seus Barcos são') # mostra uma msg centralizada
    MostraCabecalho(px) # mostra para os jogadores as posições que ele selecinou
    msgLeft('IA está colocando seus barcos') # mostra um a msg a esquerda
    Linha() # cria uma linha
    key = sortNum(tamanhoXY),sortNum(tamanhoXY) #sistema para sortear a posição dos barcos da IA
    IA1 = key  #lugar onde guardado a posição do barco da IA
    key = sortNum(tamanhoXY),sortNum(tamanhoXY) #sistema para sortear a posição dos barcos da IA
    IA2 = key #lugar onde guardado a posição do barco da IA
    key = sortNum(tamanhoXY),sortNum(tamanhoXY) #sistema para sortear a posição dos barcos da IA
    IA3 = key #lugar onde guardado a posição do barco da IA
    barcoIA1 = IA1[0] + IA1[1] # ajustes para poder ler de forma mais fácil as posiçoes dos barcos
    barcoIA2 = IA2[0] + IA2[1] # ajustes para poder ler de forma mais fácil as posiçoes dos barcos
    barcoIA3 = IA3[0] + IA3[1] # ajustes para poder ler de forma mais fácil as posiçoes dos barcos
    sleep(1) # espera por um segundo
    msgLeft('Barcos colocados, sua vez de atacar') # mostra uma msg a esqueda
    while True: # sistema de repetição que irá realmente executar o jogo
        ataque = list(map(int,input('Qual posição deseja atacar?').split(','))) # entrada do jogador para atacar uma posição da tabela da IA
        ataque1 = ataque[0] + ataque[1] # ajustes para poder ler de forma mais fácil as posiçoes dos ataques
        sleep(1) # espera um segundo
        if ataque1 == barcoIA1: #verificação se o jogador acertou a posição da IA
            barcoIA1 = [0,0] # caso acerte ele tira o barco da IA de jogo deixando na posição 0,0
            vidaIA -= 1 # tira uma vida da IA
            msgCenter(f'Você acertou parabens, agora falta só mais {vidaIA} barcos')
        elif ataque1 == barcoIA2: #verificação se o jogador acertou a posição da IA
            barcoIA2 = [0,0] # caso acerte ele tira o barco da IA de jogo deixando na posição 0,0
            vidaIA -= 1 # tira uma vida da IA
            msgCenter(f'Você acertou parabens, agora falta só mais {vidaIA} barcos')
        elif  ataque1 == barcoIA3: #verificação se o jogador acertou a posição da IA
            barcoIA3 = [0,0] # caso acerte ele tira o barco da IA de jogo deixando na posição 0,0
            vidaIA -= 1 # tira uma vida da IA
            msgCenter(f'Você acertou parabens, agora falta só mais {vidaIA} barcos')  # mostra uma msg centralizada    
        else: # caso a verificação de false ele dira ao jogador que ele errou
            msgCenter('Foi quase porém você errou o alvo, boa sorte na pròxima') # msg ao centro
        if vidaIA == 0: # caso a vida da IA seja igual a 0 ele finaliza o jogo
            msgCenter('Parabéns, você eliminou todos os barcos') # mostra uma msg ao centro
            break # quebra o código   
        Linha() # faz uma linha
        msgLeft('Vez da IA atacar') # faz uma msg a esquerda
        Linha() # faz uma linha
        key2 = sortNum(ncpNivel) # sorteia um número para o ataque da IA
        sleep(1) # espera um segundo
        if ncpNivel == 10: # verificação de dificuldade         
            if key2 == 4: # verificação do ataque, se for == 4 ele acerta um barco caso não ele erra
                key2 = sortNum(3) # caso acerte ele ira sortear qual barco ira atacar
                if key2 == 1: # primeiro caso de ataque 
                    msgCenter(f'A IA acertou seu barco na posição {barco1}') # mostra uma msg ao centro
                    if barco1 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos') # msg a esquerda
                    else: # caso seja a primera vez que acerta esse barco ele ira 
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco1 = [0,0] # tirar esse barco de jogo 
                if key2 == 2: #segundo caso de ataque
                    msgCenter(f'A IA acertou seu barco na posição {barco2}') # mostra uma msg ao centro
                    if barco2 == [0,0]:  # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco2 = [0,0]  # tirar esse barco de jogo 
                if key2 == 3:  #terceiro caso de ataque
                    msgCenter(f'A IA acertou seu barco na posição {barco3}') # mostra uma msg ao centro
                    if barco3 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco3 = [0,0] # tirar esse barco de jogo 
            else: # em caso dele errar o atque ele ira mostar que o ataque errou
                msgCenter("Que sorte, a IA errou o seu barco") # mostra uma msg ao centro
        if ncpNivel == 5: # verificação de dificuldade
            if key2 == 1: # verificação do ataque, se for == 1 ele acerta um barco caso não ele erra
                key2 = sortNum(3) # caso acerte ele ira sortear qual barco ira atacar
                if key2 == 1: 
                    msgCenter(f'A IA acertou seu barco na posição {barco1}') # mostra uma msg ao centro
                    if barco1 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco1 = [0,0] # tirar esse barco de jogo 
                if key2 == 2:
                    msgCenter(f'A IA acertou seu barco na posição {barco2}') # mostra uma msg ao centro
                    if barco2 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco2 = [0,0] # tirar esse barco de jogo 
                if key2 == 3:
                    msgCenter(f'A IA acertou seu barco na posição {barco1}') # mostra uma msg ao centro
                    if barco3 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco3 = [0,0] # tirar esse barco de jogo 
            else: # em caso dele errar o atque ele ira mostar que o ataque errou
                msgCenter("Que sorte, a IA errou o seu barco") # mostra uma msg ao centro
        if ncpNivel == 2: # verificação de dificuldade
            if key2 == 1: # verificação do ataque, se for == 4 ele acerta um barco caso não ele erra
                key2 = sortNum(3) # caso acerte ele ira sortear qual barco ira atacar
                if key2 == 1:
                    msgCenter(f'A IA acertou seu barco na posição {barco1}') # mostra uma msg ao centro
                    if barco1 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco1 = [0,0] # tirar esse barco de jogo 
                if key2 == 2:
                    msgCenter(f'A IA acertou seu barco na posição {barco2}') # mostra uma msg ao centro
                    if barco2 == [0,0]: # caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco2 = [0,0] # tirar esse barco de jogo 
                if key2 == 3:
                    msgCenter(f'A IA acertou seu barco na posição {barco1}') # mostra uma msg ao centro
                    if barco3 == [0,0]:# caso o barco seleconado já tenha sido atacado ele ira ignorar o barco
                        msgLeft(f'Como esse barco já foi acertado você ainda tem {vidaPss} barcos')
                    else: # caso seja a primera vez que acerta esse barco ele ira
                        vidaPss -= 1 # tirar uma vida do jogar e
                        barco3 = [0,0] # tirar esse barco de jogo 
            else:# em caso dele errar o atque ele ira mostar que o ataque errou
                msgCenter("Que sorte, a IA errou o seu barco") # mostra uma msg ao centro
        if vidaPss == 0: # em caso do pleyar peder todas suas vidas ele ira mostrar que perdeu e ira finalizar o jogo
            msgCenter('Que pena, você perdeu todos os barcos') # mostra uma msg ao centro
            msgCenter('infelizmente você foi derrotado') # mostra uma msg ao centro
            break #quebra o código
    Linha() # mostra uma linha
    sleep(5) # espera 5 segundos
    LimpaTela() #limpa a tela
    msgfinal = ('Obrigado por jogar','Pretende jogar novamente?','sim[1]','não[0]') # msg para ver se o jogador quer jogar novamente
    MostraCabecalho(msgfinal) # mostra a msg final
    R = input() # resposta do jogador
    if R == '1': # caso a resposata seja 1 ele ira reinaiciar o jogo
        jogo() # inicia o jogo
    if R == '0': # caso a resposta seja 0 ele ira finalizar o jogo
        print('#Obrigado por jogar#') # agredecimento
        print(" Jogo feito por Rnena Soares da Silva") # creditos
jogo() # inicia o jogo

