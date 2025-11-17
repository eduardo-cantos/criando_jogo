import pygame
from pygame.locals import *
from sys import exit #função fecha a janela

pygame.init()

#criar objeto que será a tela
largura = 640
altura = 480
x = largura/2
y = altura/2
tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Jogo teste") # muda o nome da janela

relogio = pygame.time.Clock() #Controla velocidade frames do game

#criando loop infinito, todo jogo tem
while True:
    relogio.tick(40) #velocidade de descida do retangulo 40 frames
    tela.fill((0,0,0))
    for event in pygame.event.get():#detectar se algum evento aconteceu
        if event.type == QUIT:
            pygame.quit()
            exit()
            '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
'''
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    pygame.draw.rect(tela,(255,0,0),(x,y,40,50)) # 1. tela → Surface onde o retângulo será desenhado (geralmente a tela principal do jogo).
    # 2. (255,0,0) → Cor do retângulo em RGB (neste caso, vermelho).
    # 3. (200,300,40,50) → Tupla que define o retângulo:
    #    - x → posição X (horizontal, distância da borda esquerda).
    #    - y → posição Y (vertical, distância do topo).
    #    - 40  → largura do retângulo.
    #    - 50  → altura do retângulo.


    pygame.display.update() #cada iteração do looping principal atualiza a tela do jogo

    
