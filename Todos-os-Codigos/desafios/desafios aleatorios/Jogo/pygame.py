import pygame
from pygame import *

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visual Novel Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
background = pygame.image.load("background.jpg")
character = pygame.image.load("character.png")
font = pygame.font.Font(None, 36)

# Dialog data
dialog = [
    "Hello! Welcome to this visual novel.",
    "This is an example of how you can use Pygame.",
    "You can add choices and branching paths too!"
]
dialog_index = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:  # Advance dialog on spacebar
                dialog_index += 1
                if dialog_index >= len(dialog):
                    running = False

    # Draw background and character
    screen.blit(background, (0, 0))
    screen.blit(character, (50, 150))

    # Render dialog
    if dialog_index < len(dialog):
        text_surface = font.render(dialog[dialog_index], True, BLACK)
        screen.blit(text_surface, (50, 500))

    pygame.display.flip()

pygame.quit()