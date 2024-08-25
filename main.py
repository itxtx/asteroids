from asteroids import Asteroid
from constants import *
import pygame
from player import  Player
from asteroidfield import AsteroidField
import sys
from shoot import Shot
from score import Score


def main():
    print("Starting asteroids!")
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
   # print(f"{pygame.font.get_fonts()}")
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    t = pygame.time.Clock()
    dt = 0

    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =  pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Score.containers = drawable
    score = Score(SCREEN_WIDTH-105, SCREEN_HEIGHT-40)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)
        
        for a in asteroids:
            if a.collision(player):
                print("Game Over!")
                sys.exit()

        for b in asteroids:
            for s in shots:
                if b.collision(s):
                    s.kill()
                    b.split()
                    score.add()

        screen.fill("black")

        score.draw(screen) 
        for j in drawable:
            j.draw(screen)

        pygame.display.flip()
        
        dt = t.tick(60) / 1000









if __name__ == "__main__":
    main()










