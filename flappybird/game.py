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
        self.image = pygame.image.load('flappybird\img\ssflappy-bird-pipe-transparent-11549930651hqzkrjyfcl.png').convert_alpha()
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
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Alex')
clock = pygame.time.Clock()
#--------------------
# create game objects
all_sprites = pygame.sprite.Group()
alex = Alex(100, 350)
all_sprites.add(alex)
pipe = Pipe(500, 0)
all_sprites.add(pipe)
#--------------------
# game loop
game = True
while game:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            game = False
        # check for keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                alex.speedy = -10
    
    hits = pygame.sprite.spritecollide(alex,pipe,True)
    if len(hits) > 0:
        alex.kill()
    # update
    all_sprites.update()
    # draw / render
    window.blit(backgorund, (0, 0))
    all_sprites.draw(window)
    # after drawing everything, flip the display
    pygame.display.flip()
#--------------------
pygame.quit()

