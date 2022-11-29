 # importa biblioteca
import pygame
import random

#--------------------
pygame.init()
pygame.mixer.init()
  
# gera tela
width = 580
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Alex')

# inicia assets
FPS = 30
alex_width = 90
alex_height = 68
pipe_width = 300
pipe_height = 400
backgorund = pygame.image.load('flappybird\img\Rbckgu.jpg').convert()

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('flappybird\img\Rbckgu.jpg').convert()
    assets['alex'] = pygame.image.load('flappybird\img\kisspng-king-kong-western-gorilla-ape-portable-network-gra-g (1).png').convert_alpha()
    assets['alex'] = pygame.transform.scale(assets['alex'], (alex_width, alex_height))
    assets['pipe'] = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
    assets['pipe'] = pygame.transform.scale(assets['pipe'], (pipe_width, pipe_height))
    assets['inicial'] = pygame.image.load('flappybird\img\sstela_inicial.jpeg')
    assets['gameover'] = pygame.image.load('flappybird\img\sstela_gameover.jpeg')
    return assets

gravity = 1 
pipe_speed = 10
class Alex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappybird\img\kisspng-king-kong-western-gorilla-ape-portable-network-gra-g (1).png').convert_alpha()
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
        
            
class Pipe2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):
        #height = random.randint(500,600)
        self.rect.x -= pipe_speed
        if self.rect.right < 0:
            self.rect.left = width
            self.rect.centery =  random.randint(400, 600)
               

#--------------------

all_sprites = pygame.sprite.Group()
alex = Alex(100, 350)
all_sprites.add(alex)
pipe = Pipe(500, 0)
pipe2 = Pipe2(500, 500)

all_sprites.add(pipe)
#--------------------
# game loop
 

def game_over():
    pygame.quit()
    exit()
# loop do jogo
def game():
    score = 0
    assets = load_assets()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    alex = Alex(100, 350)
    all_sprites.add(alex)
    pipe2 = Pipe2(random.randint(0, 500), 500)
    pipes = pygame.sprite.Group()
    for i in range(1):
        pipe = Pipe(width , random.randint(-200, -100))
        pipe2 = Pipe2(width, random.randint(500, 600))
        all_sprites.add(pipe)
        all_sprites.add(pipe2)
        pipes.add(pipe)   
        pipes.add(pipe2)
    inicial = True
    final = False
    while inicial:
        window.blit(assets['inicial'], (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inicial = False
                    running = True
        pygame.display.update()
                    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alex.speedy = -12
        all_sprites.update()
        hits = pygame.sprite.spritecollide(alex, pipes, False)
        if hits:
            running = False
            final = True
        tt = pygame.time.get_ticks()
        score = tt/1000  

        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)
        # desenha placar
        font_name = pygame.font.match_font('arial')
        def draw_text(surf, text, size, x, y):
            font = pygame.font.Font(font_name, size)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)
        draw_text(window, str(score), 18, width / 2, 10)


        pygame.display.update()
    while final:
        window.blit(assets['gameover'], (0,200))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    final = False
        pygame.display.update()
                    
    game_over()
game()
