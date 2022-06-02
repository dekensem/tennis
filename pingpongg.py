#создай игру "Лабиринт"!
from pygame import *
from random import randint, randrange 
from time import time as t

window=display.set_mode((700,500))
display.set_caption("Пингпогн ")
background=transform.scale(image.load('tableee.jpg'),(700,500))   
FPS=60

font.init()
font=font.SysFont("century gothic",70)
win=font.render("YOU WIN!", True, (215, 119, 247))

lose=font.render("YOU LOSER!", True, (215, 119, 247))
wait = 60

clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, p_width, p_height):
         super().__init__()
         self.image=transform.scale(image.load(p_image),(p_width, p_height))
         self.speed=p_speed
         self.rect=self.image.get_rect()
         self.rect.x=p_x
         self.rect.y=p_y
         self.width= p_width
         self.height=p_height
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 320:
            self.rect.y += self.speed
        
    def update1(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 320:
            self.rect.y += self.speed



    
raketka1=Player("raketkalefttt.jpg", 10, 250, 5, 50, 175)
raketka2=Player("raketkarighttt.jpg", 630, 250, 5, 50, 175)

class Enemyy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y>500:
            self.rect.x=randint(0, 430)
            self.rect.y=0
            self.speed=randint(1, 3)



game=True
finish=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False

    if finish != True:
        window.blit(background,(0,0))
        raketka1.reset()
        raketka2.reset()
        raketka1.update1()
        raketka2.update()

    
    if wait>0:
        wait=wait-1
    if wait==0:
        finish=False
        wait=-1


    
    clock.tick(FPS)
    display.update()