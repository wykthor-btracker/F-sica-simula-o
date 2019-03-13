import pygame
from functools import reduce
from pygame import Vector2 as Vec2
from copy import deepcopy
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
        self.show()

    def __str__(self):
        return "pos ({},{}) vec ({},{})".format(self.x,self.y,self.vector.x,self.vector.y)

    def force(self, forceVector):
        self.vectors.append(forceVector)

    # def calcMove(self):

    def move(self):
        if self.vectors:
            self.vector = deepcopy(reduce(lambda x,y:x+y, self.vectors))
        if self.vector.length():
            self.vector /= self.vector.length()
        self.x, self.y = self+self.vector
        self.show()

    def show(self):
        self.display.blit(self.img,(self.x,self.y))
        # pygame.draw.line(self.display, black, (self.x, self.y),((self.x+self.vector.x),(self.y+self.vector.y)),5)

def game_loop():
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    gameExit = False
    center = Car(x,y,gameDisplay,"racecar.png",[])
    gameDisplay.fill(white)
    center.move()
    Orbital = Vec2(2500,0) # Substituir por radius**2
    car = Car(x,y-50,gameDisplay,"racecar.png",[Orbital])
    toCenter = car.aim(center)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        toCenter.x, toCenter.y = car.aim(center).x, car.aim(center).y
        Orbital.x, Orbital.y = Orbital+toCenter
        car.move()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
