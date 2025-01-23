import pygame
import constants
import player

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

    player_char = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    while(runflag):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runflag = False

        player_char.update(dt)
        screen.fill("black") #black screen
        player_char.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

    pygame.quit()

#below this line is the end of file
if __name__ == "__main__":
    main()