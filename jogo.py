import pygame
from pygame.locals import *
from sys import exit #função fecha a janela

pygame.init()

#criar objeto que será a tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Jogo teste") # muda o nome da janela

#criando loop infinito, todo jogo tem
while True:
    for event in pygame.event.get():#detectar se algum evento aconteceu
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela,(255,0,0),(200,300,40,50)) # 1. tela → Surface onde o retângulo será desenhado (geralmente a tela principal do jogo).
    # 2. (255,0,0) → Cor do retângulo em RGB (neste caso, vermelho).
    # 3. (200,300,40,50) → Tupla que define o retângulo:
    #    - 200 → posição X (horizontal, distância da borda esquerda).
    #    - 300 → posição Y (vertical, distância do topo).
    #    - 40  → largura do retângulo.
    #    - 50  → altura do retângulo.

    pygame.draw.circle(tela, (0,0,200),(300,260), 40)

    pygame.draw.line(tela,(255,255,3), (390,0), (390,600), 5)


    pygame.display.update() #cada iteração do looping principal atualiza a tela do jogo

    
