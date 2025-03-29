# venv
# source venv/bin/activate

# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()
        screen.fill(000000, None, 0)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000

    # print("Starting Asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()