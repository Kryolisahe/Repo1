import pygame
import random
from pygame.locals import *
import time

def change_background(img):
    backgrounds=pygame.image.load(img)
    background=pygame.transform.scale(backgrounds,(screen_width,screen_height))
    screen.blit(background,(0,0))
pygame.init()
pygame.display.set_caption("Bees")

screen_width=800
screen_height=600

screen=pygame.display.set_mode([screen_width,screen_height])

class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("cartoonbee.jpg").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
        
class Flowers(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
        
images=("flower 1.jpg","flower 2.png","flower 3.png")

#create sprite groups
flower_list=pygame.sprite.Group()
allsprites=pygame.sprite.Group()

bee=Bee()
allsprites.add(bee)

for i in range(100):
    flowers=Flowers(random.choice(images))
    flowers.rect.x=random.randrange(screen_width)
    flowers.rect.y=random.randrange(screen_height)
    flower_list.add(flowers)
    allsprites.add(flowers)

WHITE=(255,255,255)
RED=(255,0,0)

playing=True
score=0

clock=pygame.time.Clock()
start_time=time.time()

myFont=pygame.font.SysFont("Times New Roman",40)
text=myFont.render("Score="+str(0),True,WHITE)
timing_font=pygame.font.SysFont("Times New Roman",70)


while playing:
    clock.tick(30)#refreshed the screen 30 times in a second
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    time_elapsed=time.time()-start_time
    if time_elapsed>=30:
        text=myFont.render("   Game over and the score is    "+str(score),True,WHITE)
        screen.blit(text,(280,40))
    else:
        change_background("background.jpg")
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if cartoonbee.rect.y>0:
                cartoonbee.rect.y-=5
        if keys[pygame.K_DOWN]:
            if cartoonbee.rect.y<630:
                cartoonbee.rect.y+=5
        if keys[pygame.K_LEFT]:
            if cartoonbee.rect.x>0:
                cartoonbee.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if cartoonbee.x<850:
                cartoonbee.rect.x+=5
                
        stone_hit_list=pygame.sprite.spritecollide(cartoonbee,flower_list,True)
        for flower in stone_hit_list:
            score=score+1
            text=myFont.render("score="+str(score),True,WHITE)
        screen.blit(text,(730,80))
        allsprites.draw(screen)
    pygame.display.update()
       
            
pygame.quit()
