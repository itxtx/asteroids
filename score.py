



import pygame

from player import Player


class Score:

    def __init__(self, x,y):
        self.position = pygame.Vector2(x,y) #put it somewhere in a corner
        self.score = 0

    def draw(self, screen):
        #pygame.draw.circle(screen, 'white', self.position, self.radius, 2) #draw score
        font = pygame.font.SysFont('applesdgothicneo', 24)
        img = font.render(f'Score: {self.score}', True, 'green')
        screen.blit(img, self.position)

    def add(self):
        self.score += 1






