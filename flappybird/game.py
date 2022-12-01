 # importa biblioteca
import pygame
import random

#--------------------
pygame.init() # inicializa o pygame
pygame.mixer.init() 
  
# gera tela
width = 580 # largura tela
height = 480 # altura tela
window = pygame.display.set_mode((width, height)) # cria a tela
pygame.display.set_caption('Flappy Alex') # nome da tela

# inicia assets
FPS = 30 # frames por segundo
alex_width = 90 # largura alex
alex_height = 68 # altura alex
pipe_width = 300 # largura pipe
pipe_height = 400 # altura pipe
backgorund = pygame.image.load('flappybird\img\Rbckgu.jpg').convert() # carrega imagem de fundo

def load_assets(): # carrega assets
    assets = {} # dicionario de assets
    assets['background'] = pygame.image.load('flappybird\img\Rbckgu.jpg').convert() # carrega imagem de fundo
    assets['alex'] = pygame.image.load('flappybird\img\kisspng-king-kong-western-gorilla-ape-portable-network-gra-g (1).png').convert_alpha() # carrega imagem do alex
    assets['alex'] = pygame.transform.scale(assets['alex'], (alex_width, alex_height)) # redimensiona imagem do alex
    assets['pipe'] = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha() # carrega imagem do pipe
    assets['pipe'] = pygame.transform.scale(assets['pipe'], (pipe_width, pipe_height)) # redimensiona imagem do pipe
    assets['inicial'] = pygame.image.load('flappybird\img\sstela_inicial.jpeg') # carrega imagem do pipe
    assets['inicial'] = pygame.transform.scale(assets['inicial'], (width, height)) # redimensiona imagem do pipe
    assets['gameover'] = pygame.image.load('flappybird\img\sstela_gameover.jpeg') # carrega imagem do pipe
    assets['gameover'] = pygame.transform.scale(assets['gameover'], (width, height))     
    assets['som_pulo'] = pygame.mixer.Sound('flappybird\img\X2Download (mp3cut.net).mp3')
    assets['fail'] = pygame.mixer.Sound('flappybird\img\X2Download.app - Sound _Fail_ (Som de falha) (128 kbps).mp3')
    assets['musica_jog'] = pygame.mixer.Sound('flappybird\img\HQ The Weeknd - Blinding Lights (Chipmunk Version).mp3')
    return assets

gravity = 1  # gravidade
pipe_speed = 10 # velocidade do pipe
class Alex(pygame.sprite.Sprite): # classe alex
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)     
        self.image = pygame.image.load('flappybird\img\kisspng-king-kong-western-gorilla-ape-portable-network-gra-g (1).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (alex_width, alex_height))
        self.rect = self.image.get_rect() # pega o retangulo da imagem
        self.rect.centerx = x # centraliza no eixo x
        self.rect.centery = y # centraliza no eixo y
        self.speedy = 0 # velocidade no eixo y
    def update(self): # atualiza a posição do alex
        self.speedy += gravity # adiciona gravidade
        self.rect.y += self.speedy # adiciona velocidade no eixo y
        if self.rect.bottom > height: # se o alex passar do chão
            self.rect.bottom = height # ele volta para o chão
            self.speedy = 0 # velocidade no eixo y volta a ser 0
        if self.rect.top < 0: # se o alex passar do teto
            self.rect.top = 0 # ele volta para o teto
            self.speedy = 0 # velocidade no eixo y volta a ser 0
class Pipe(pygame.sprite.Sprite): # classe pipe
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x # centraliza no eixo x
        self.rect.centery = y # centraliza no eixo y
    def update(self):
        self.rect.x -= pipe_speed # adiciona velocidade no eixo x
        if self.rect.right < 0: # se o pipe passar da tela
            self.rect.left = width # ele volta para a tela
        
            
class Pipe2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('flappybird\img\pipe_top.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width, pipe_height))
        self.image = pygame.transform.flip(self.image, False, True) # inverte a imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = x # centraliza no eixo x
        self.rect.centery = y # centraliza no eixo y
    def update(self):
        #height = random.randint(500,600)
        self.rect.x -= pipe_speed
        if self.rect.right < 0: # se o pipe passar da tela
            self.rect.left = width # ele volta para a tela
            self.rect.centery =  random.randint(400, 600) #muda seu tamanho
               

#--------------------

all_sprites = pygame.sprite.Group() # grupo de sprites
alex = Alex(100, 350) # cria o alex
all_sprites.add(alex) # adiciona o alex ao grupo de sprites
pipe = Pipe(500, 0) # cria o pipe
pipe2 = Pipe2(500, 500) # cria o pipe 

all_sprites.add(pipe) # adiciona o pipe ao grupo de sprites
#--------------------
# game loop
def restart_game(): # função para reiniciar o jogo
    global pipe, pipe2, alex, all_sprites
    all_sprites = pygame.sprite.Group()
    alex = Alex(100, 350)
    all_sprites.add(alex)
    pipe = Pipe(500, 0)
    pipe2 = Pipe2(500, 500)
    all_sprites.add(pipe)
    all_sprites.add(pipe2)
    game()

 

def game_over(): # função para tela de game over
    pygame.quit()
    exit()
# loop do jogo
def game(): # função do jogo
    score = 0 # pontuação
    assets = load_assets() # carrega os assets
    clock = pygame.time.Clock() # cria o clock 
    
    all_sprites = pygame.sprite.Group() # grupo de sprites
    alex = Alex(100, 350) # cria o alex
    all_sprites.add(alex) # adiciona o alex ao grupo de sprites 
    pipe2 = Pipe2(random.randint(0, 500), 500)  # cria o pipe
    pipes = pygame.sprite.Group() # grupo de pipes
    assets['musica_jog'].play() # toca a musica
    for i in range(1): # cria  pipes
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
                if event.key == pygame.K_SPACE: # se apertar espaço
                    inicial = False # sai do loop
                    running = True # entra no loop do jogo
        pygame.display.update() # atualiza a tela
                    
    while running: # loop do jogo
        clock.tick(FPS) # define o FPS 
        
        for event in pygame.event.get(): # loop de eventos
            if event.type == pygame.QUIT: # se apertar o x
                running = False # sai do loop
            if event.type == pygame.KEYDOWN: # se apertar uma tecla
                if event.key == pygame.K_SPACE: # se apertar espaço
                    alex.speedy = -12  # adiciona velocidade no eixo y
                    assets['som_pulo'].play() # toca o som do pulo
        all_sprites.update() # atualiza os sprites
        hits = pygame.sprite.spritecollide(alex, pipes, False) # verifica se o alex colidiu com os pipes
        if hits: # se colidiu
            assets['fail'].play() # toca o som de game over
            running = False # sai do loop
            final = True # entra no loop de game over
        tt = pygame.time.get_ticks() # pega o tempo
        score = tt/1000   # define a pontuação

        window.blit(assets['background'], (0, 0)) # desenha o background
        all_sprites.draw(window) # desenha os sprites
        # desenha placar
        font_name = pygame.font.match_font('arial') # define a fonte
        def draw_text(surf, text, size, x, y): # função para desenhar o placar
            font = pygame.font.Font(font_name, size)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)
        draw_text(window, str(score), 18, width / 2, 10)


        pygame.display.update()
    while final: # loop de game over
        window.blit(assets['gameover'], (0,0))  # desenha a tela de game over
        draw_text(window, str(score), 18, width / 2, 10) # desenha o placar
        assets['musica_jog'].stop() # para a musica
        for event in pygame.event.get(): # loop de eventos
            if event.type == pygame.KEYDOWN: # se apertar uma tecla
                if event.key == pygame.K_ESCAPE: # se apertar esc
                    final = False # sai do loop
                    
                if event.key == pygame.K_SPACE: # se apertar espaço
                    restart_game() # reinicia o jogo
                
                    
        pygame.display.update() # atualiza a tela
                     
    game_over()

game()
