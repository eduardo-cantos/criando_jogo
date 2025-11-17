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
    pygame.display.update() #cada iteração do looping principal atualiza a tela do jogo