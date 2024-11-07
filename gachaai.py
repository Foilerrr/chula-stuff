import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gacha")

# Class defining different classes
class archer:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = 100
        self.damage = 50
        self.movement = 2
        self.range = 5

class warrior:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = 200
        self.damage = 30
        self.movement = 1
        self.range = 2

class horseman:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = 150
        self.damage = 40
        self.movement = 10
        self.range = 2

class legendary:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = health
        self.damage = damage
        self.movement = movement
        self.range = range

# Dict creation for different characters


# Gacha items
items = ["Common Item", "Rare Item", "Epic Item", "Legendary Item"]
item_probabilities = [0.7, 0.2, 0.08, 0.02]  # Probabilities must sum to 1

# Font setup
font = pygame.font.Font(None, 36)

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to perform gacha pull
def gacha_pull():
    return random.choices(items, item_probabilities)[0]

# Game loop
running = True
result = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press space to pull gacha
                rarity = gacha_pull()
                if rarity = "Common Item":
                    
                result = 

    screen.fill((0, 0, 0))  # Clear screen with black color

    # Display instructions
    draw_text("Press SPACE to pull gacha", font, (255, 255, 255), screen, 20, 20)

    # Display gacha result
    if result:
        draw_text(f"You got: {result}", font, (255, 255, 255), screen, 20, 60)

    pygame.display.update()

pygame.quit()