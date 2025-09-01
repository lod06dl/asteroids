import pygame, random
from constants import * 
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, color='white', center=self.position, radius=self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            asteroid_1, asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS), Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS),
            asteroid_1.velocity, asteroid_2.velocity = self.velocity.rotate(angle)*1.2, self.velocity.rotate(-angle)*1.2