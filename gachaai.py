import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gacha")

# Class defining different classes
class archer:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50
        self.movement = 2
        self.range = 5

class warrior:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.damage = 30
        self.movement = 1
        self.range = 2

class horseman:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.damage = 40
        self.movement = 10
        self.range = 2
    
class rare_warrior:
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.damage = 40
        self.movement = 2
        self.range = 2

class rare_archer:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.damage = 60
        self.movement = 2
        self.range = 5

class rare_horseman:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.damage = 50
        self.movement = 10
        self.range = 2
class other:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = health
        self.damage = damage
        self.movement = movement
        self.range = range

# Dict creation for different characters
char_dict_common = {
            "soldier1" : warrior("soldier1"),
            "soldier2" : warrior("soldier2"),
            "soldier3" : warrior("soldier3"),
            "cavalry1" : horseman("cavalry1"),
            "cavalry2" : horseman("cavalry2"),
            "cavalry3" : horseman("cavalry3"),
            "ranger1" : archer("ranger1"),
            "ranger2" : archer("ranger2"),
            "ranger3" : archer("ranger3"),
             }
char_dict_rare = {
                "John" : rare_warrior("John"),
                "Paul" : rare_warrior("Paul"),
                "Richard" : rare_warrior("Richard"),
                "Xu Jin" : rare_horseman("Xu Jin"),
                "Yamato" : rare_horseman("Yamato"),
                "Yi Sun" : rare_horseman("Yi Sun"),
                "Gonzalez" : rare_archer("Gonzalez"),
                "Carlos" : rare_archer("Carlos"),
                "Jose" : rare_archer("Jose")
                 }

char_dict_epic = {
                "Leonidas" : other("Leonidas", 2,3,4,5),
                "Saladin" : other("Saladin", 2,3,4,5),
                "Takeda" : other("Takeda", 2,3,4,5),
                "Napoleon" : other("Napoleon", 2,3,4,5),
                "Joan of Arc" : other("Joan of Arc", 2,3,4,5),
                "Oda" : other("Oda", 2,3,4,5)
                  }
char_dict_legendary = {
                    "Julius Caesar" : other("Julius Caesar", 2,3,4,5),
                    "Alexander the Great" : other("Alexander the Great", 2,3,4,5),
                    "Genghis Khan" : other("Genghis Khan", 2,3,4,5),
                    "Dodge Washington" : other("Dodge Washington", 2,3,4,5)
                    }


# Gacha items
items = ["Common Item", "Rare Item", "Epic Item", "Legendary Item"]
item_probabilities = [0.5, 0.3, 0.15, 0.05]

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
                if rarity == "Common Item":
                    result = random.choice(list(char_dict_common.keys()))
                elif rarity == "Rare Item":
                    result = random.choice(list(char_dict_rare.keys()))
                elif rarity == "Epic Item":
                    result = random.choice(list(char_dict_epic.keys()))
                elif rarity == "Legendary Item":
                    result = random.choice(list(char_dict_legendary.keys()))


    screen.fill((0, 0, 0))  # Clear screen with black color

    # Display instructions
    draw_text("Press SPACE to pull gacha", font, (255, 255, 255), screen, 20, 20)

    # Display gacha result
    if result:
        draw_text(f"You got: {result}", font, (255, 255, 255), screen, 20, 60)

    pygame.display.update()

pygame.quit()