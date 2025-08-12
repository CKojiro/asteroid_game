import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_pos_vec = self.velocity.rotate(angle)
            new_neg_vec = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_1steroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_2steroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_1steroid.velocity = new_pos_vec
            new_2steroid.velocity = new_neg_vec
            new_1steroid.velocity *= 1.2
            new_2steroid.velocity *= 1.2
