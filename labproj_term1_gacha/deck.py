import pygame
import os
from shared_data import player_deck
from shared_data import char_dict_player1
from shared_data import char_dict_player2

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1700
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Deck")

# Font
font = pygame.font.Font(None, 36)

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
    "soldier1": warrior("soldier1"),
    "soldier2": warrior("soldier2"),
    "soldier3": warrior("soldier3"),
    "cavalry1": horseman("cavalry1"),
    "cavalry2": horseman("cavalry2"),
    "cavalry3": horseman("cavalry3"),
    "ranger1": archer("ranger1"),
    "ranger2": archer("ranger2"),
    "ranger3": archer("ranger3"),
}

char_dict_rare = {
    "Xu Jin": rare_horseman("Xu Jin"),
    "Yamato": rare_horseman("Yamato"),
    "Yi Sun": rare_horseman("Yi Sun"),
    "Gonzalez": rare_archer("Gonzalez"),
    "Carlos": rare_archer("Carlos"),
    "Jose": rare_archer("Jose")
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

char_dict_all = char_dict_common | char_dict_rare | char_dict_epic | char_dict_legendary

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_deck_screen(surface, selected_rarity):
    surface.fill(black)
    y_offset = 50
    x_offset = 50
    max_width = screen_width - 250  # Leave space for the buttons and selected characters
    characters = []

    if selected_rarity == "Common":
        characters = [char.name for char in char_dict_common.values() if char.name in player_deck]
    elif selected_rarity == "Rare":
        characters = [char.name for char in char_dict_rare.values() if char.name in player_deck]
    elif selected_rarity == "Epic":
        characters = [char.name for char in char_dict_epic.values() if char.name in player_deck]
    elif selected_rarity == "Legendary":
        characters = [char.name for char in char_dict_legendary.values() if char.name in player_deck]

    character_positions = {}  # Dictionary to store character positions

    for character_name in characters:
        profile_image_path = os.path.join('game files', 'Profile', f'L - {character_name}_Profile (2).png')
        if os.path.exists(profile_image_path):
            profile_image = pygame.image.load(profile_image_path)
            surface.blit(profile_image, (x_offset, y_offset))
            character_positions[character_name] = (x_offset, y_offset)  # Store position
            x_offset += profile_image.get_width() + 10
            if x_offset + profile_image.get_width() > max_width:
                x_offset = 50
                y_offset += profile_image.get_height() + 10
        else:
            draw_text(f"Image not found for {character_name}", font, white, surface, x_offset, y_offset)
            x_offset += 200  # Assuming a fixed width for missing images
            if x_offset + 200 > max_width:
                x_offset = 50
                y_offset += 40

    return character_positions  # Return character positions

def draw_selected_characters(surface, selected_characters):
    surface.fill(black)
    y_offset = 50
    x_offset = 50
    max_width = screen_width - 100

    for character_name in selected_characters:
        profile_image_path = os.path.join('game files', 'Profile', f'L - {character_name}_Profile (2).png')
        if os.path.exists(profile_image_path):
            profile_image = pygame.image.load(profile_image_path)
            surface.blit(profile_image, (x_offset, y_offset))
            x_offset += profile_image.get_width() + 10
            if x_offset + profile_image.get_width() > max_width:
                x_offset = 50
                y_offset += profile_image.get_height() + 10
        else:
            draw_text(f"Image not found for {character_name}", font, white, surface, x_offset, y_offset)
            x_offset += 200  # Assuming a fixed width for missing images
            if x_offset + 200 > max_width:
                x_offset = 50
                y_offset += 40

def handle_selected_characters_click(event, selected_characters, player_deck):
    y_offset = 50
    x_offset = 50
    max_width = screen_width - 100

    for character_name in selected_characters:
        profile_image_path = os.path.join('game files', 'Profile', f'L - {character_name}_Profile (2).png')
        if os.path.exists(profile_image_path):
            profile_image = pygame.image.load(profile_image_path)
            rect = profile_image.get_rect(topleft=(x_offset, y_offset))
            if rect.collidepoint(event.pos):
                player_deck.append(character_name)
                del selected_characters[character_name]
                break
            x_offset += profile_image.get_width() + 10
            if x_offset + profile_image.get_width() > max_width:
                x_offset = 50
                y_offset += profile_image.get_height() + 10
        else:
            x_offset += 200  # Assuming a fixed width for missing images
            if x_offset + 200 > max_width:
                x_offset = 50
                y_offset += 40

def draw_rarity_buttons(surface):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rarities = ["Com", "Rare", "Epic", "Leg"]
    y_offset = 50

    for rarity in rarities:
        if 1600 <= mouse_x <= 1700 and y_offset <= mouse_y <= y_offset + 50:
            pygame.draw.rect(surface, white, (1600, y_offset, 100, 50))
            draw_text(rarity, font, black, surface, 1625, y_offset + 15)
        else:
            pygame.draw.rect(surface, gray, (1600, y_offset, 100, 50))
            draw_text(rarity, font, black, surface, 1625, y_offset + 15)
        y_offset += 60

def draw_player_buttons(surface):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    players = ["P1", "P2"]
    y_offset = 350
    x_offset = screen_width - 100  # Adjusted to fit the button width

    for player in players:
        if x_offset <= mouse_x <= x_offset + 100 and y_offset <= mouse_y <= y_offset + 50:
            pygame.draw.rect(surface, white, (x_offset, y_offset, 100, 50))
            draw_text(player, font, black, surface, x_offset + 25, y_offset + 15)
        else:
            pygame.draw.rect(surface, gray, (x_offset, y_offset, 100, 50))
            draw_text(player, font, black, surface, x_offset + 25, y_offset + 15)
        y_offset += 60

def start_deck(screen):
    running = True
    selected_rarity = "Common"
    selected_player = "Player 1"
#    char_dict_player1 = []
#    char_dict_player2 = []
    current_screen = "deck"

    while running:
        screen.fill(black)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == "deck":
                    if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                        return  # Return to main menu
                    elif 1600 <= mouse_x <= 1700:
                        if 50 <= mouse_y <= 100:
                            selected_rarity = "Common"
                        elif 110 <= mouse_y <= 160:
                            selected_rarity = "Rare"
                        elif 170 <= mouse_y <= 220:
                            selected_rarity = "Epic"
                        elif 230 <= mouse_y <= 280:
                            selected_rarity = "Legendary"
                        elif 350 <= mouse_y <= 400:
                            current_screen = "player1"
                        elif 410 <= mouse_y <= 460:
                            current_screen = "player2"
                    else:
                        character_positions = draw_deck_screen(screen, selected_rarity)
                        for character_name, (x, y) in character_positions.items():
                            profile_image_path = os.path.join('game files', 'Profile', f'L - {character_name}_Profile (2).png')
                            profile_image = pygame.image.load(profile_image_path)
                            rect = profile_image.get_rect(topleft=(x, y))
                            if rect.collidepoint(event.pos):
                                if event.button == 1 and len(char_dict_player1) < 10:  # Left mouse button for Player 1
                                    char_dict_player1[character_name] = char_dict_all[character_name]
                                    #char_dict_player1.append(character_name)
                                    player_deck.remove(character_name)
                                elif event.button == 3 and len(char_dict_player2) < 10:  # Right mouse button for Player 2
                                    char_dict_player2[character_name] = char_dict_all[character_name]
                                    #char_dict_player2.append(character_name)
                                    player_deck.remove(character_name)
                elif current_screen == "player1":
                    handle_selected_characters_click(event, char_dict_player1, player_deck)
                    if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                        current_screen = "deck"
                elif current_screen == "player2":
                    handle_selected_characters_click(event, char_dict_player2, player_deck)
                    if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                        current_screen = "deck"

        if current_screen == "deck":
            character_positions = draw_deck_screen(screen, selected_rarity)
            draw_rarity_buttons(screen)
            draw_player_buttons(screen)

            # Draw the "Back" button
            if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)
            else:
                pygame.draw.rect(screen, gray, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)
        elif current_screen == "player1":
            draw_selected_characters(screen, char_dict_player1)
            # Draw the "Back" button
            if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)
            else:
                pygame.draw.rect(screen, gray, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)
        elif current_screen == "player2":
            draw_selected_characters(screen, char_dict_player2)
            # Draw the "Back" button
            if 50 <= mouse_x <= 150 and 850 <= mouse_y <= 900:
                pygame.draw.rect(screen, white, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)
            else:
                pygame.draw.rect(screen, gray, (50, 850, 100, 50))
                draw_text("Back", font, black, screen, 75, 865)

        pygame.display.flip()