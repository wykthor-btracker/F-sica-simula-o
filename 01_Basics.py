import pygame
from pygame import Vector2 as Vec2
from sys import argv
import math
pygame.init()

display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)

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
    def __init__(self,x,y, display,path, vectors=list()):
        super().__init__(x,y)
        self.img = pygame.image.load(path)
        self.vectors = vectors
        self.vector = Vec2()
        self.display = display

    def __str__(self):
        return "pos ({},{}) vec ({},{})".format(self.x,self.y,self.vector.x,self.vector.y)

    def newPos(self,radius,theta,center):
        self.x = center.x+radius*math.cos(theta)
        self.y = center.y+radius*math.sin(theta)
        self.show()

    def show(self):
        self.display.blit(self.img,(self.x,self.y))

def game_loop(radius = 50):
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    gameExit = False
    center = Car(x,y,gameDisplay,"racecar.png",[])
    gameDisplay.fill(white)
    center.show()
    radius = int(radius)
    car = Car(x,y-radius,gameDisplay,"racecar.png",[])
    theta = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        theta+=0.01
        car.newPos(radius,theta,center)
        pygame.display.update()
        clock.tick(60)


game_loop(argv[1])
pygame.quit()
quit()
