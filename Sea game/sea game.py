import pygame,sys
import time
import random
from pygame.locals import *

screen_width=800
screen_height=700

pygame.init()

screen=pygame.display.set_mode([screen_width,screen_height])

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
pygame.mixer.init()

clock=pygame.time.Clock()
myFont=pygame.font.SysFont("Times New Roman",35)
smallFont=pygame.font.SysFont("Times New Roman",20)

def changeBackground(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))
    pygame.display.set_caption("Make Your Own Game")
    pygame.display.update()
#--------------------------------------------------------------
def welcomeScreen():
    pygame.mixer.music.load("startsound.mp3")
    pygame.mixer.music.play(-1)
    changeBackground("startscreen.jpg")
    text=myFont.render(" HELP THE TURTLE FIND STARFISH" ,True,RED)
    screen.blit(text,(100,70))
    text2=smallFont.render(" PRESS SPACE TO START THE GAME ",True,WHITE)
    screen.blit(text2,(20,300))
    text3=smallFont.render(" USE ARROW KEYS TO PLAY ",True,WHITE)
    screen.blit(text3,(20,325))
    text4=smallFont.render(" AVOID THE ENEMIES TO SAVE YOUR LIFE ",True,WHITE)
    screen.blit(text4,(20,350))
    text5=smallFont.render(" AVOID THE OBSTACLES AS THEY WILL RELOCATE YOU ",True,WHITE)
    screen.blit(text5,(20,375))
    text6=smallFont.render(" CLICK ON CROSS(X)TO QUIT ",True,RED)
    screen.blit(text6,(20,400))
    pygame.display.update()
    #capture events
    while True:
        for event in pygame.event.get():
            if (event.type==KEYDOWN) and (event.key==K_SPACE):
                startgame()
                return
            elif event.type==QUIT:
                pygame.quit()
                sys.exit()
                
#---------------------------------------------------------------
    
#define the player sprite
#player starts at (0,0) as default

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("player.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
            
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>screen_width:
            self.rect.right=screen_width
        if  self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>screen_height:
            self.rect.bottom=screen_height
#------------------------------------------------------------------------            
        
            
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("target.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.x=1
        self.rect.y=500
        #this determines target has to move left or right
        self.moveLeft=False
    def update(self):
        if self.moveLeft:
            self.rect.move_ip(-2,0)
            if self.rect.x<=5:
                self.moveLeft=False
        else:
            self.rect.move_ip(2,0)
            if self.rect.x>=screen_width-50:
                self.moveLeft=True
#---------------------------------------------------------------------                
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(screen_width)
        self.rect.y=random.randrange(screen_height)
        #speed is randomly generated
        self.speed=random.randint(1,4)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()
#----------------------------------------------------------------------
class Obstacles(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(screen_width)
        self.rect.y=random.randrange(screen_height)
    def update(self):
        self.rect.move_ip(random.randint(-3,3),random.randint(-1,1))
        if self.rect.right<0:
            self.kill()
#---------------------------------------------------------------------        
enemies=["enemy1.png","enemy2.png","enemy3.png","enemy4.png"]
obstacles=["obstacle1.png","obstacle2.png","obstacle3.png","obstacle4.png"]

#create groups to hold sprites
enemy_group=pygame.sprite.Group()
obstacle_group=pygame.sprite.Group()
allsprites=pygame.sprite.Group()

def createEnemy():
    new_enemy=Enemy(random.choice(enemies))
    enemy_group.add(new_enemy)
    allsprites.add(new_enemy)
    return new_enemy

def createObstacle():
    new_Obstacle=Obstacles(random.choice(obstacles))
    obstacle_group.add(new_Obstacle)
    allsprites.add(new_Obstacle)
    return new_Obstacle

def createPlayerTarget():
    player=Player()
    target=Target()
    allsprites.add(player)
    allsprites.add(target)
    return player,target
def bounce(obj):
    pygame.mixer.music.load("bounce.mp3")
    pygame.mixer.music.play()
    obj.rect.move_ip(random.randint(-30,30),random.randint(-30,30))
    
def endScreen(sound,img,text):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    changeBackground(img)
    screen.blit(text,(150,50))

    text1=smallFont.render(" PRESS SPACE TO RESTART ",True,WHITE)
    screen.blit(text1,(20,200))
    
    text2=smallFont.render(" CLICK ON CROSS(X)TO QUIT ",True,RED)
    screen.blit(text2,(20,240))
    pygame.display.update()
    #capture events
    while True:
        for event in pygame.event.get():
            if (event.type==KEYDOWN) and (event.key==K_SPACE):
                welcomeScreen()
                return
            elif event.type==QUIT:
                pygame.quit()
                sys.exit()
    
#-----------------------------------------------------------------------
def startgame():
    ADD_ENEMY=pygame.USEREVENT+1
    pygame.time.set_timer(ADD_ENEMY,600)

    ADD_OBSTACLE=pygame.USEREVENT+2
    pygame.time.set_timer(ADD_OBSTACLE,1000)
    

    PLAYER,TARGET=createPlayerTarget()
    #createEnemy()
    #createObstacle()
    life=20
    clock.tick(30)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                return
            elif event.type==ADD_ENEMY:
                createEnemy()
            elif event.type==ADD_OBSTACLE:
                createObstacle()
                
        pressed_keys=pygame.key.get_pressed()
        PLAYER.update(pressed_keys)

        if pygame.sprite.spritecollideany(PLAYER,enemy_group):
            bounce(PLAYER)
            life=life-1
            if life==0:
                sound="losesound.mp3"
                img="endscreen.jpg"
                text=myFont.render("You Lost........try again next time",True,RED)
                endScreen(sound,img,text)
                return
            
        if pygame.sprite.spritecollideany(PLAYER,obstacle_group):
            bounce(PLAYER)
        if pygame.sprite.collide_rect(PLAYER,TARGET):
            sound="winsound.mp3"
            img="endscreen.jpg"
            text=myFont.render("You Won........play and enjoy",True,RED)
            endScreen(sound,img,text)
            return

        enemy_group.update()
        obstacle_group.update()
        TARGET.update()
        image=pygame.image.load("background.jpg")
        screen.blit(image,(0,0))
        #draw the life strip on screen
        pygame.draw.rect(screen,RED,(500,10,life*10,10))
    
        
        allsprites.draw(screen)
        pygame.display.update()

welcomeScreen()
pygame.quit()
    
    
        
        
        
