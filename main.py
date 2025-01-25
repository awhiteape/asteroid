import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    runflag = True

    clock = pygame.time.Clock()
    dt = 0.0

    #creating groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #adding player class to groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots,updateable,drawable)
    AsteroidField.containers = (updateable)
    player_char = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    field = AsteroidField()
    while(runflag):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runflag = False

        for obj in updateable:
            obj.update(dt)
        #player_char.update(dt)
        screen.fill("black") #black screen
        #player_char.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        
        for asteroid_obj in asteroids:
            if (asteroid_obj.check_collision(player_char)):
                print("Game Over!")
                runflag = False
            for bullet in shots:
                if asteroid_obj.check_collision(bullet):
                    asteroid_obj.kill()
                    bullet.kill()
                    asteroid_obj.split()
        
        if keys[pygame.K_ESCAPE]:
            runflag = False
        pygame.display.flip()
        dt = clock.tick(60)/1000

    pygame.quit()

#below this line is the end of file
if __name__ == "__main__":
    main()