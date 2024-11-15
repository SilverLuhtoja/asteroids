import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def printGameData():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    printGameData()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update objects
        for obj in updatable:
            obj.update(dt)

        # draw objects in every frame
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # check player collision to asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()
                

        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
