import pygame
import sys
from assets.player import Player

# Initialize Pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Player Game Object Example")

player = Player(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()