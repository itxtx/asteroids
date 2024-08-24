

import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def draw(self, dt):
        self.position += self.velocity * dt










