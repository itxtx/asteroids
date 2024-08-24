import pygame
from pygame.draw import line
from circleshape import CircleShape
from constants import *

class Player(CircleShape):

    def __init__(self, x ,y):
        self.x = x
        self.y = y

        self.circle = CircleShape(self.x,self.y, PLAYER_RADIUS) 

        self.position = pygame.Vector2(self.x, self.y)
        self.rotation = 0


           # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, color= "white", points=self.triangle(self), line(2))






