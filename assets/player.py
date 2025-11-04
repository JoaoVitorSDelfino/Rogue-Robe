import pygame

class Player:
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y
        # Size
        self.width = 50
        self.height = 50
        # Color
        self.color = (0, 255, 0)  # green
        # Speed
        self.speed = 1
    
    def draw(self, screen):
        # Draw the player as a rectangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        # Move the player with arrow keys
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

Player