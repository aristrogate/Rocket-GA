import pygame
import random
import math
pygame.init()

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.dna = DNA(300)
        self.frame=0
        self.fitness=0
        
    def calculate_fitness(self,target_x,target_y):
        distance = math.sqrt((target_x-self.x)**2+(target_y-self.y)**2)
        if distance == 0:
            self.fitness = float('inf')
            
        else:
            self.fitness = 1/distance
        
    def update(self):
        if self.frame < len(self.dna.genes):
            gene=self.dna.genes[self.frame]
            self.ax,self.ay=gene
        
            self.vx=self.vx+self.ax
            self.vy=self.vy+self.ay
        
            self.x = self.x + self.vx
            self.y = self.y + self.vy
        
            self.frame = self.frame+1

    def draw(self, surface,color="white"):
        pygame.draw.rect(surface,color,(self.x,self.y,10,40))
        
class DNA:
    def __init__(self,size):
        self.genes = []
        for i in range(size):
            ax = random.uniform(-temp,temp)
            ay = random.uniform(-temp,temp)
            self.genes.append((ax,ay))
            
    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0,len(self.genes))
        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes[i] = self.genes[i]
                
            else:
                child.genes[i] = partner.genes[i]
                
        return child
    
    def mutate(self,mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                ax = random.uniform(-temp,temp)
                ay = random.uniform(-temp,temp)
                self.genes[i] = (ax,ay)

class Population:
    def __init__(self,size):
        self.rockets = [Rocket(300,500) for i in range(size)]
        self.generation=0
        
    def update(self):
        for rocket in self.rockets:
            rocket.update()
        
    def draw(self,surface,target_x,target_y):
        for rocket in self.rockets:
            rocket.draw(surface)
            
        best = min(self.rockets,key=lambda r:math.sqrt((target_x-r.x)**2+(target_y-r.y)**2))
        best.draw(surface,color="green")
            
    def evaluate(self,target_x,target_y):
        for rocket in self.rockets:
            rocket.calculate_fitness(target_x,target_y)
            
    def all_done(self):
        for rocket in self.rockets:
            if rocket.frame < len(rocket.dna.genes):
                return False
        
        return True
    
    def next_generation(self):
        pool = []
        for rocket in self.rockets:
            n = int(rocket.fitness * 1000)
            for i in range(n):
                pool.append(rocket)
                
        new_rockets = []
        
        for i in range(len(self.rockets)):
            ParentA = random.choice(pool)
            ParentB = random.choice(pool)
            
            child_dna = ParentA.dna.crossover(ParentB.dna)
            
            child_dna.mutate(0.01)
            
            child = Rocket(300,500)
            child.dna = child_dna
            new_rockets.append(child)
            
        self.rockets = new_rockets
        self.generation += 1
        
WIDTH = 600
HEIGHT = 600
temp = 0.3

target_x,target_y = 300,50
population = Population(50)

surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Rocket GA')

color = "blue"
running = True
clock = pygame.time.Clock()

font = pygame.font.SysFont("monospace", 16)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    population.update()
    
    if population.all_done():
        population.evaluate(target_x,target_y)
        population.next_generation()
            
    surface.fill(color)
    text = font.render(f"Generation: {population.generation}", True, "white")
    surface.blit(text, (10, 10))
    pygame.draw.circle(surface,"red",(target_x,target_y),10)
    population.draw(surface,target_x,target_y)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()