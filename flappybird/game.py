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

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('flappybird\img\ssbombonera_1200_4.jpg').convert()
    assets['alex'] = pygame.image.load('flappybird\img\sslex.png').convert_alpha()
    assets['alex'] = pygame.transform.scale(assets['alex'], (alex_width, alex_height))
    assets['pipe'] = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
    assets['pipe'] = pygame.transform.scale(assets['pipe'], (pipe_width, pipe_height))
    return assets
#create a game like flappy bird
#variables Alex
#create same game using classes
gravity = 1 
pipe_speed = 2
class Alex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappybird\img\sslex.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (alex_width, alex_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 0
    def update(self):
        self.speedy += gravity
        self.rect.y += self.speedy
        if self.rect.bottom > height:
            self.rect.bottom = height
            self.speedy = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = 0
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):
        self.rect.x -= pipe_speed
        if self.rect.right < 0:
            self.rect.left = width
            self.rect.y = random.randint(-200, -100)
#--------------------
# if alex collides with pipe, game over
#--------------------
# gera saídas
def game_over():
    pygame.quit()
    exit()
# loop do jogo
def game():
    assets = load_assets()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    alex = Alex(100, 350)
    all_sprites.add(alex)
    pipes = pygame.sprite.Group()
    for i in range(2):
        pipe = Pipe(width + i * 300, random.randint(-200, -100))
        all_sprites.add(pipe)
        pipes.add(pipe)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alex.speedy = -15
        all_sprites.update()
        hits = pygame.sprite.spritecollide(alex, pipes, False)
        if hits:
            running = False
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)
        pygame.display.update()
    game_over()
game()

