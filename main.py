from asteroids import Asteroid
from constants import *
import pygame
from player import  Player
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    t = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =  pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        for i in updatable:
            i.update(dt)


        screen.fill("black")

        for j in drawable:
            j.draw(screen)

        pygame.display.flip()
        
        dt = t.tick(60) / 1000









if __name__ == "__main__":
    main()










