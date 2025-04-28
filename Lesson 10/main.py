
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
        super().__init__()
        self.image = pygame.image.load('bin.png')
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):

    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

class  Not_recyclable(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bag.png')
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
    plastic.rect.y = random.randrange(HEIGHT)

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

while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    timeElapsed = time.time() - start_time

    if timeElapsed >= 20:
        if score >= 20:
            SCREEN.fill("green")
            text1= myFont.render("Bin loot : \nSuccessful", True, RED)
        
        else:
            SCREEN.fill("red")
            text1 = myFont.render("Bin Loot : \nFAILED",True,Black)

        SCREEN.blit(text1,(400,300))

    else:
        screen_change('background.png')
        countDown = myFont.render("Time Left :"+str(20 - int(timeElapsed)),True,Black)
        SCREEN.blit(countDown,(20,10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if bin.rect.y >0:
                bin.rect.y -= 5

        if keys[pygame.K_s]:
            if bin.rect.y <HEIGHT:
                bin.rect.y += 5
        
        if keys[pygame.K_d]:
            if bin.rect.x >0:
                bin.rect.x += 5
        
        if keys[pygame.K_a]:
            if bin.rect.x < WIDTH:
                bin.rect.x -= 5
        
        item_hit_list = pygame.sprite.spritecollide(bin,item_list,True)
        plastic_hit_list = pygame.sprite.spritecollide(bin,plastic_list,True)

        for item in item_hit_list:
            score += 1 
            text = myFont.render("Score :"+str(score),True,Black)
        
        for plastic in plastic_hit_list:
            score -= 2.5
            text = myFont.render("Score ="+ str(score),True,Black)
    
    SCREEN.blit(text,(20,50))
    all_sprites.draw(SCREEN)
    pygame.display.update()
pygame.quit()
