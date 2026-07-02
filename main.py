import pygame
import random
pygame.init()

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.dna = DNA(300)
        self.frame=0
        
    def update(self):
        if self.frame < len(self.dna.genes):
            gene=self.dna.genes[self.frame]
            self.ax,self.ay=gene
        
            self.vx=self.vx+self.ax
            self.vy=self.vy+self.ay
        
            self.x = self.x + self.vx
            self.y = self.y + self.vy
        
            self.frame = self.frame+1

    def draw(self, surface):
        pygame.draw.rect(surface,"white",(self.x,self.y,10,40))
        
class DNA:
    def __init__(self,size):
        self.genes = []
        for i in range(size):
            ax = random.uniform(-1,1)
            ay = random.uniform(-1,1)
            self.genes.append((ax,ay))

WIDTH = 600
HEIGHT = 600

rocket = Rocket(300,500)

surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Rocket GA')

color = "blue"
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    rocket.update()
            
    surface.fill(color)
    rocket.draw(surface)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()