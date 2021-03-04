import pygame
import sys
import random
import numpy as np

FPC = 100
W = 600
H = 600
cell_w = 2
width = W // cell_w
height = H // cell_w

BLACK    =   (0, 0, 0)
WHITE    =   (255, 255, 255)
ORANGE   =   (255, 125, 0)
BLUE     =   (0, 70, 225)
YELLOW   =   (255, 255, 0)
GREEN    =   (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Life')

class World:
    def __init__(self,w,h):
        self.world_w = w
        self.world_h = h 
        self.x = w//2
        self.y = h//2
        self.nap = 0
        self.world = np.zeros((w,h))
        # for i in range(w*h//8):
        #     self.world[random.randint(1,self.world_w-2), random.randint(1,self.world_h-2)] = 1
    def worldLogic(self):
        if self.nap == 0:
            if self.world[self.x][self.y] == 0:
                self.world[self.x][self.y] = 1
                self.drawCell(self.x,self.y,1)
                self.x -= 1
                self.nap = 1
            elif self.world[self.x][self.y] == 1:
                self.world[self.x][self.y] = 2
                self.drawCell(self.x,self.y,2)
                self.x += 1
                self.nap = 3
            elif self.world[self.x][self.y] == 2:
                self.world[self.x][self.y] == 0
                self.drawCell(self.x,self.y,0)
                self.y -= 1
                self.nap = 0
        elif self.nap == 1:
            if self.world[self.x][self.y] == 0:
                self.world[self.x][self.y] = 1
                self.drawCell(self.x,self.y,1)
                self.y += 1
                self.nap = 2
            elif self.world[self.x][self.y] == 1:
                self.world[self.x][self.y] = 2
                self.drawCell(self.x,self.y,2)
                self.y -= 1
                self.nap = 0
            elif self.world[self.x][self.y] == 2:
                self.world[self.x][self.y] == 0
                self.drawCell(self.x,self.y,0)
                self.x -= 1
                self.nap = 1
        elif self.nap == 2:
            if self.world[self.x][self.y] == 0:
                self.world[self.x][self.y] = 1
                self.drawCell(self.x,self.y,1)
                self.x += 1
                self.nap = 3
            elif self.world[self.x][self.y] == 1:
                self.world[self.x][self.y] = 2
                self.drawCell(self.x,self.y,2)
                self.x -= 1
                self.nap = 1
            elif self.world[self.x][self.y] == 2:
                self.world[self.x][self.y] == 0
                self.drawCell(self.x,self.y,0)
                self.y += 1
                self.nap = 2
        elif self.nap == 3:
            if self.world[self.x][self.y] == 0:
                self.world[self.x][self.y] = 1
                self.drawCell(self.x,self.y,1)
                self.y -= 1
                self.nap = 0
            elif self.world[self.x][self.y] == 1:
                self.world[self.x][self.y] = 2
                self.drawCell(self.x,self.y,2)
                self.y += 1
                self.nap = 2
            elif self.world[self.x][self.y] == 2:
                self.world[self.x][self.y] == 0
                self.drawCell(self.x,self.y,0)
                self.x += 1
                self.nap = 3
    def drawWorld(self):
        if self.world[self.x][self.y] == 1:
            self.drawCell(self.x,self.y,1)
        else:
            self.drawCell(self.x,self.y,0)
    def drawCell(self, x, y, col=0):
        if col == 0:
            color = BLACK
        elif col == 1:
            color = WHITE
        elif col == 2:
            color = ORANGE
        pygame.draw.rect(sc, color, (x*cell_w, y*cell_w, cell_w, cell_w))

def main():
    sc.fill(BLACK)
    w1 = World(width, height)
    while True:    
        clock.tick(FPC)
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
        w1.worldLogic()
        # w1.drawWorld()
        #code

        pygame.display.update()

main()