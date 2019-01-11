import pygame, sys, random
from pygame.locals import *

pygame.init()

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

windowWidth = 900
windowHeight = 700
              
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, windowWidth)
        self.rect.y = random.randint(0, windowHeight)



class Player(Sprite):
    def __init__(self,  image):
        super().__init__(image)
        self.score = 0
        
        

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 10
        if key[K_DOWN]:
            self.rect.y += dist
        if key[K_UP]:
            self.rect.y -= dist
        if key[K_RIGHT]:
            self.rect.x += dist
        if key[K_LEFT]:
            self.rect.x -= dist
        self.rect.x = self.rect.x % windowWidth
        self.rect.y = self.rect.y % windowHeight



 

screen = pygame.display.set_mode((windowWidth, windowHeight))
apples = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player = Player('Smiley.png')
all_sprites_list.add(player)

FPS = 30
fpsClock = pygame.time.Clock()


running = True

while running:
    if len(apples.sprites()) == 0:
        apple = Sprite('apple.png')
        apples.add(apple)
        all_sprites_list.add(apple)

    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_keys()
    collisions = pygame.sprite.spritecollide(player,  apples,  True)
    
    all_sprites_list.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(FPS)


    


pygame.quit()
sys.exit()




