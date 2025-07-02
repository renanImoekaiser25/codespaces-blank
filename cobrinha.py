import pygame, sys, os

x,y = 600,600

preta = (0,0,0)
branco = (255,255,255)
vermelha = (255,0,0)
verde = (0,255,0)

tamanhoQuadrado = 10
velocidade = 15


pygame.init()
pygame.display.set_caption("Snake")
janela = pygame.display.set_mode((x,y))
relogio = pygame.time.Clock()


gameOver = False
while not gameOver:
    janela.fill(preta)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            gameOver = True





