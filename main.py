from constants import *
import pygame
from player import  Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    t = pygame.time.Clock()
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.quit():
                return

        

        screen.fill(color="black")



        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
        dt = t.tick(60) / 1000









if __name__ == "__main__":
    main()










