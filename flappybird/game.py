# importa biblioteca
import pygame
import random
#--------------------
pygame.init()
pygame.mixer.init()

# gera tela
width = 580
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Alex')

# inicia assets
FPS = 30
alex_width = 60
alex_height = 48
pipe_width = 300
pipe_height = 400

backgorund = pygame.image.load('flappybird\img\ssbombonera_1200_4.jpg').convert()
backgorund = pygame.transform.scale(backgorund, (width, height)) 
alex = pygame.image.load('flappybird\img\sslex.png').convert_alpha()
alex = pygame.transform.scale(alex, (alex_width, alex_height))
pipe = pygame.image.load('flappybird\img\ssflappy-bird-pipe-transparent-11549930651hqzkrjyfcl.png').convert_alpha()
pipe = pygame.transform.scale(pipe, (pipe_width, pipe_height))
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('flappybird\img\ssbombonera_1200_4.jpg').convert()
    assets['alex'] = pygame.image.load('flappybird\img\sslex.png').convert_alpha()
    assets['alex'] = pygame.transform.scale(assets['alex'], (alex_width, alex_height))
    assets['pipe'] = pygame.image.load('flappybird\img\sstrophy-11527593161wjmswjufrj.png').convert_alpha()
    assets['pipe'] = pygame.transform.scale(assets['pipe'], (pipe_width, pipe_height))
    return assets
#create a game like flappy bird
#variables Alex
alex_x = 100
alex_y = 350
alex_speed = 0
gravity = 1
#variables pipe
pipe_x = 500
pipe_y = 0
pipe_speed = 2
#--------------------
# loop do jogo
game = True
while game:
    # ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    clock.tick(FPS)
    # processa os eventos
    for event in pygame.event.get():
        # verifica se foi fechado
        if event.type == pygame.QUIT:
            game = False
        # verifica se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                alex_speed = -10
    # atualiza a posição do alex
    alex_speed += gravity
    alex_y += alex_speed
    # atualiza a posição do pipe
    pipe_x -= pipe_speed
    # desenha o fundo na tela
    window.blit(backgorund, (0, 0))
    # desenha o alex na tela
    window.blit(alex, (alex_x, alex_y))
    # desenha o pipe na tela
    window.blit(pipe, (pipe_x, pipe_y))
    # atualiza a tela
    pygame.display.update()
# finaliza a janela do jogo
pygame.quit()
