import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        for i in range(2):   
            random_angle  = random.uniform(20, 50)     
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            if i == 0:
                asteroid.velocity = self.velocity.rotate(random_angle) * 1.5
                continue
            asteroid.velocity = self.velocity.rotate(-random_angle) * 1.5
            
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt