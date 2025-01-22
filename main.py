import pygame
import constants

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    runflag = True

    clock = pygame.time.Clock()
    dt = 0.0


    while(runflag):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runflag = False
        screen.fill("black") #black screen
        pygame.display.flip()
        dt = clock.tick(60)
        dt = dt/1000

    pygame.quit()

#below this line is the end of file
if __name__ == "__main__":
    main()