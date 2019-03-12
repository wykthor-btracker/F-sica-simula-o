import pygame
import time
import random
from pygame import Vector2 as Vec2
pygame.init()

display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 40

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
class Particle():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,pair):
        return(self.x + pair.x,self.y + pair.y)

    def aim(self,other):
        return(Vec2(other.x-self.x,other.y-self.y))


class Car(Particle):
    def __init__(self,x,y,vector: Vec2, display,path):
        super().__init__(x,y)
        self.img = pygame.image.load(path)
        self.vector = vector
        self.display = display
        self.show()

    def __str__(self):
        return("pos ({},{}) vec ({},{})".format(self.x,self.y,self.vector.x))
    def force(self,forceVector):
        self.vector += forceVector

    def move(self):
        self.x,self.y = self+self.vector
        self.show()

    def show(self):
        self.display.blit(self.img,(self.x,self.y))

def game_loop():
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    x_change = 0
    gameExit = False
    center = Particle(x,y)
    car = Car(x+10,y+10,Vec2(0,0),gameDisplay,"racecar.png")
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        car.x += x_change
        gameDisplay.fill(white)
        car.vector = car.aim(center)
        car.move()
        car.show()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
