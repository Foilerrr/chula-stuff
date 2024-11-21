import pygame
import random
import os
from shared_data import player_deck, gems

# Initialize Pygame
pygame.init()

# Load the images
good_banner_image_path = os.path.join('game files', 'Banner', 'Banner Gacha', 'Banner.zip - Legendary Gacha_Banner.png')
bad_banner_image_path = os.path.join('game files', 'Banner', 'Banner Gacha', 'Banner.zip - Epic Gacha_Banner.png')

good_banner_image = pygame.image.load(good_banner_image_path)
bad_banner_image = pygame.image.load(bad_banner_image_path)

# Screen dimensions
screen_width = 1700
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gacha")

# Font
font = pygame.font.Font(os.path.join("Fonts","AncientModernTales-a7Po.ttf" ), 36)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)

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
                #"John" : rare_warrior("John"),
                #"Paul" : rare_warrior("Paul"),
                #"Richard" : rare_warrior("Richard"),
                "Xu Jin" : rare_horseman("Xu Jin"),
                "Yamato" : rare_horseman("Yamato"),
                "Yi Sun" : rare_horseman("Yi Sun"),
                "Gonzalez" : rare_archer("Gonzalez"),
                "Carlos" : rare_archer("Carlos"),
                "Jose" : rare_archer("Jose")
                 }

char_dict_epic = {
    "Leonidas": other("Leonidas", 300, 50, 5, 2),
    "Saladin": other("Saladin", 290, 55, 6, 3),
    "Takeda": other("Takeda", 285, 60, 7, 4),
    "Napoleon": other("Napoleon", 280, 65, 4, 5),
    "Joan of Arc": other("Joan of Arc", 295, 52, 5, 3),
    "Oda": other("Oda", 288, 58, 6, 4)
}

char_dict_legendary = {
    "Julius Caesar": other("Julius Caesar", 320, 70, 5, 3),
    "Alexander the Great": other("Alexander the Great", 310, 75, 6, 4),
    "Genghis Khan": other("Genghis Khan", 315, 80, 7, 5),
    "Dodge Washington": other("Dodge Washington", 305, 68, 5, 2)
}

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to roll gacha
def roll_gacha_goodbanner(times):
    results = []
    for _ in range(times):
        rarity = random.choices(
            ["Common", "Rare", "Epic", "Legendary"],
            [0.5, 0.3, 0.15, 0.05]
        )[0]
        if rarity == "Common":
            result = random.choice(list(char_dict_common.keys()))
        elif rarity == "Rare":
            result = random.choice(list(char_dict_rare.keys()))
        elif rarity == "Epic":
            result = random.choice(list(char_dict_epic.keys()))
        elif rarity == "Legendary":
            result = random.choice(list(char_dict_legendary.keys()))
        results.append(result)
        if result not in player_deck:  # Check for duplicates
            player_deck.append(result)  # Add character to player's deck
    return results

def roll_gacha_badbanner(times):
    results = []
    for _ in range(times):
        rarity = random.choices(
            ["Common", "Rare", "Epic"],
            [0.6, 0.3, 0.1]
        )[0]
        if rarity == "Common":
            result = random.choice(list(char_dict_common.keys()))
        elif rarity == "Rare":
            result = random.choice(list(char_dict_rare.keys()))
        elif rarity == "Epic":
            result = random.choice(list(char_dict_epic.keys()))
        results.append(result)
        if result not in player_deck:  # Check for duplicates
            player_deck.append(result)  # Add character to player's deck
    return results

def display_character_banner(surface, character_name):
    banner_image_path = os.path.join('game files', 'Banner', f'Banner.zip - {character_name}_Banner.png')
    banner_image = pygame.image.load(banner_image_path)
    surface.blit(banner_image, (0, 0))

# Function to display the good banner image
def display_good_banner(surface):
    surface.blit(good_banner_image, (0, 0))

# Function to display the bad banner image
def display_bad_banner(surface):
    surface.blit(bad_banner_image, (0, 0))

# Input box class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = gray
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = white if self.active else gray
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def start_gacha(screen):
    running = True
    result = None
    current_banner = 1
    global gems
    current_character_index = 0
    input_box = InputBox(50, 50, 250, 50)

    while running:
        screen.fill(black)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if result is not None and current_character_index < len(result):
                    current_character_index += 1
                    if current_character_index >= len(result):
                        result = None
                        current_character_index = 0
                if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                    running = False
                elif current_banner == 1:
                    if 1000 <= mouse_x <= 1200 and 850 <= mouse_y <= 900:
                        if gems >= 10:
                            gems -= 10
                            result = roll_gacha_goodbanner(1)
                            current_character_index = 0
                        else:
                            result = ["Insufficient gems"]
                    elif 1200 <= mouse_x <= 1400 and 850 <= mouse_y <= 900:
                        if gems >= 100:
                            gems -= 100
                            result = roll_gacha_goodbanner(10)
                            current_character_index = 0
                        else:
                            result = ["Insufficient gems"]
                    elif 1600 <= mouse_x <= 1700 and 50 <= mouse_y <= 100:
                        current_banner = 2
                elif current_banner == 2:
                    if 1000 <= mouse_x <= 1200 and 850 <= mouse_y <= 900:
                        if gems >= 5:
                            gems -= 5
                            result = roll_gacha_badbanner(1)
                            current_character_index = 0
                        else:
                            result = ["Insufficient gems"]
                    elif 1200 <= mouse_x <= 1400 and 850 <= mouse_y <= 900:
                        if gems >= 50:
                            gems -= 50
                            result = roll_gacha_badbanner(10)
                            current_character_index = 0
                        else:
                            result = ["Insufficient gems"]
                    elif 1600 <= mouse_x <= 1700 and 50 <= mouse_y <= 100:
                        current_banner = 1

            code = input_box.handle_event(event)
            if code:
                if code == "SPECIALCODE":
                    gems += 1000
                    input_box.text = ''
                    input_box.txt_surface = font.render(input_box.text, True, input_box.color)

        if result is not None and current_character_index < len(result):
            display_character_banner(screen, result[current_character_index])
        else:
            if current_banner == 1:
                display_good_banner(screen)
            else:
                display_bad_banner(screen)

        # Display gem counter
        draw_text(f"Gems: {gems}", font, white, screen, 50, 10)

        # Draw the input box
        input_box.draw(screen)

        if current_banner == 1:
            # Display buttons with hover effect
            if 1000 <= mouse_x <= 1200 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (1000, 850, 200, 50))
                draw_text("Roll 1 Time", font, black, screen, 1030, 865)
            else:
                pygame.draw.rect(screen, gray, (1000, 850, 200, 50))
                draw_text("Roll 1 Time", font, black, screen, 1030, 865)

            if 1200 <= mouse_x <= 1400 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (1200, 850, 200, 50))
                draw_text("Roll 10 Times", font, black, screen, 1230, 865)
            else:
                pygame.draw.rect(screen, gray, (1200, 850, 200, 50))
                draw_text("Roll 10 Times", font, black, screen, 1230, 865)

            if 1600 <= mouse_x <= 1700 and 50 <= mouse_y <= 100:
                pygame.draw.rect(screen, white, (1600, 50, 100, 50))
                draw_text("Next", font, black, screen, 1625, 65)
            else:
                pygame.draw.rect(screen, gray, (1600, 50, 100, 50))
                draw_text("Next", font, black, screen, 1625, 65)

        # Draw the "Back" button
        if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
            pygame.draw.rect(screen, white, (50, 850, 100, 50))
            draw_text("Back", font, black, screen, 75, 865)
        else:
            pygame.draw.rect(screen, gray, (50, 850, 100, 50))
            draw_text("Back", font, black, screen, 75, 865)

        if current_banner == 2:
            # Display buttons with hover effect
            if 1000 <= mouse_x <= 1200 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (1000, 850, 200, 50))
                draw_text("Roll 1 Time", font, black, screen, 1030, 865)
            else:
                pygame.draw.rect(screen, gray, (1000, 850, 200, 50))
                draw_text("Roll 1 Time", font, black, screen, 1030, 865)

            if 1200 <= mouse_x <= 1400 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (1200, 850, 200, 50))
                draw_text("Roll 10 Times", font, black, screen, 1230, 865)
            else:
                pygame.draw.rect(screen, gray, (1200, 850, 200, 50))
                draw_text("Roll 10 Times", font, black, screen, 1230, 865)

            if 1600 <= mouse_x <= 1700 and 50 <= mouse_y <= 100:
                pygame.draw.rect(screen, white, (1600, 50, 100, 50))
                draw_text("Back", font, black, screen, 1625, 65)
            else:
                pygame.draw.rect(screen, gray, (1600, 50, 100, 50))
                draw_text("Back", font, black, screen, 1625, 65)

        pygame.display.flip()