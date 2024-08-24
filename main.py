from constants import *
import pygame


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    t = pygame.time.Clock()
    dt = 0

    while True:
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()
        
        t.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.quit():
                return





if __name__ == "__main__":
    main()










