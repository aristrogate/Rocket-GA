import pygame
pygame.init()

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = -8
        self.ax = 0
        self.ay = 0.1

    def update(self):
        self.y = self.y+self.vy
        self.vy=self.vy+self.ay

    def draw(self, surface):
        pygame.draw.rect(surface,"white",(self.x,self.y,10,40))

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