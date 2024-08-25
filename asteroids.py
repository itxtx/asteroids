import random as rn


import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = rn.uniform(20,50)

            direct_1 = self.velocity.rotate(angle)
            direct_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(direct_1.x, direct_1.y, new_radius)
            asteroif_2 = Asteroid(direct_2.x, direct_2.y, new_radius)

            asteroid_1.velocity = direct_1 *  1.2
            asteroif_2.velocity = direct_2 *  1.2





