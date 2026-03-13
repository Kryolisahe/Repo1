import pygame
import random
from pygame.locals import *
import time

def change_background(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))
pygame.init()
pygame.display.set_caption("Treasure Hunt!!")

screen_width=900
screen_height=700

screen=pygame.display.set_mode([screen_width,screen_height])

class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pirate.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
        
class Stone(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,30))
        self.rect=self.image.get_rect()
        
images=("stone1.png","stone2.png","stone3.png")

#create sprite groups
stone_list=pygame.sprite.Group()
allsprites=pygame.sprite.Group()

pirate=Pirate()
allsprites.add(pirate)

for i in range(100):
    stone=Stone(random.choice(images))
    stone.rect.x=random.randrange(screen_width)
    stone.rect.y=random.randrange(screen_height)
    stone_list.add(stone)
    allsprites.add(stone)

WHITE=(255,255,255)
RED=(255,0,0)

playing=True
score=0

clock=pygame.time.Clock()
start_time=time.time()

myFont=pygame.font.SysFont("Times New Roman",40)
text=myFont.render("Score="+str(0),True,WHITE)
timing_font=pygame.font.SysFont("Times New Roman",70)

#main program loop

while playing:
    clock.tick(30)#refreshed the screen 30 times in a second
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    time_elapsed=time.time()-start_time
    if time_elapsed>=30:
        change_background("losescreen.jpg")
        text=myFont.render("   Game over and the score is    "+str(score),True,WHITE)
        screen.blit(text,(280,40))
    else:
        change_background("b1.jpg")
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate.rect.y>0:
                pirate.rect.y-=5
        if keys[pygame.K_DOWN]:
            if pirate.rect.y<630:
                pirate.rect.y+=5
        if keys[pygame.K_LEFT]:
            if pirate.rect.x>0:
                pirate.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if pirate.rect.x<850:
                pirate.rect.x+=5
                
        stone_hit_list=pygame.sprite.spritecollide(pirate,stone_list,True)
        for stone in stone_hit_list:
            score=score+1
            text=myFont.render("score="+str(score),True,WHITE)
        screen.blit(text,(730,80))
        allsprites.draw(screen)
    pygame.display.update()
       
            
pygame.quit()

    

    

        
                              
                              
