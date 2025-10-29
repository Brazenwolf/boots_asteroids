import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000        
        updatable.update(dt)
        for a in asteroids:
            if a.collision_check(player):
                sys.exit("Game over!")
        for b in asteroids:
            for s in shots:
                if s.collision_check(b):
                    b.split()
                    s.kill()                
        screen.fill((0,0,0))        
        for to_draw in drawable:
            to_draw.draw(screen)        
        pygame.display.flip()
        
    
    


if __name__ == "__main__":
    main()
