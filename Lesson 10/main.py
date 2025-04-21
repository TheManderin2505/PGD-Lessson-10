
import pygame
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 600

SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

def screen_change(image):
    background_img = pygame.image.load(image)
    background = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
    SCREEN.blit(background,(0,0))

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super.__init__()
        self.image = pygame.image.load('bin.png')
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):

    def __init__(self,image):
        super.__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(image,(30,30))
        self.rect = self.image.get_rect()

class  Not_recyclable(pygame.sprite.Sprite):

    def __init__(self):
        super.__init__()
        self.image = pygame.imgage.load('bag.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()           #recycleble
plastic_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

bin = Player()
all_sprites.add(bin)

images = ['item1.png','box.png','pencil.png']

for i in range(50):
    item = Recyclable(random.choice(images))

    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)

    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    plastic = Not_recyclable()

    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.x = random.randrange(HEIGHT)

    all_sprites.add(plastic)
    plastic_list.add(plastic)

WHITE = (255,255,255)
RED = (255,0,0)
Black = (0,0,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman",22)
text = myFont.render("Score = "+str(score),True,Black)

