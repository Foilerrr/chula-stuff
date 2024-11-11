import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions (Currently only works with 800x600)
screen_width = 1700
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gacha Game")

# Font
font = pygame.font.Font(None, 36)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)
hover_color = (100, 100, 100)

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

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to roll gacha
def roll_gacha(times):
    results = []
    for _ in range(times):
        rarity = random.choices(
            ["Common Item", "Rare Item", "Epic Item", "Legendary Item"],
            [0.5, 0.3, 0.15, 0.05]
        )[0]
        if rarity == "Common Item":
            result = random.choice(list(char_dict_common.keys()))
        elif rarity == "Rare Item":
            result = random.choice(list(char_dict_rare.keys()))
        elif rarity == "Epic Item":
            result = random.choice(list(char_dict_epic.keys()))
        elif rarity == "Legendary Item":
            result = random.choice(list(char_dict_legendary.keys()))
        results.append(result)
    return results # Rolls n times (1 or 10) and makes a list of the results

# Main loop
running = True
result = None
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 1300 <= mouse_x <= 1500 and 850 <= mouse_y <= 900:
                result = roll_gacha(1)
            elif 1500 <= mouse_x <= 1700 and 850 <= mouse_y <= 900:
                result = roll_gacha(10)

    screen.fill(black)  # Clear screen with black color

    # Display instructions
    draw_text("Pull gacha", font, white, screen, 750, 100)

   # Display buttons with hover effect
    if 1300 <= mouse_x <= 1500 and 850 <= mouse_y <= 900:
        pygame.draw.rect(screen, white, (1300, 850, 200, 50))
        draw_text("Roll 1 Time", font, black, screen, 1330, 865)
    else:
        pygame.draw.rect(screen, gray, (1300, 850, 200, 50))
        draw_text("Roll 1 Time", font, black, screen, 1330, 865)

    if 1500 <= mouse_x <= 1700 and 850 <= mouse_y <= 900:
        pygame.draw.rect(screen, white, (1500, 850, 200, 50))
        draw_text("Roll 10 Times", font, black, screen, 1530, 865)
    else:
        pygame.draw.rect(screen, gray, (1500, 850, 200, 50))
        draw_text("Roll 10 Times", font, black, screen, 1530, 865)

    # Display gacha result
    if result:
        y_offset = 300
        for item in result:
            draw_text(f"You got: {item}", font, white, screen, 750, y_offset)
            y_offset += 40

    pygame.display.update()

pygame.quit()