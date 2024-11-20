import pygame
import os
from gachafin import player_deck, char_dict_common, char_dict_rare, char_dict_epic, char_dict_legendary, screen_width, font, white, gray

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to draw the deck screen
def draw_deck_screen(surface, selected_rarity):
    surface.fill((0, 0, 0))
    y_offset = 50
    x_offset = 50
    max_width = screen_width - 200  # Leave space for the buttons
    characters = []

    if selected_rarity == "Common":
        characters = [char.name for char in char_dict_common.values() if char.name in player_deck]
    elif selected_rarity == "Rare":
        characters = [char.name for char in char_dict_rare.values() if char.name in player_deck]
    elif selected_rarity == "Epic":
        characters = [char.name for char in char_dict_epic.values() if char.name in player_deck]
    elif selected_rarity == "Legendary":
        characters = [char.name for char in char_dict_legendary.values() if char.name in player_deck]

    for character_name in characters:
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

# Function to draw rarity buttons
def draw_rarity_buttons(surface):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rarities = ["Common", "Rare", "Epic", "Legendary"]
    y_offset = 50

    for rarity in rarities:
        if 1600 <= mouse_x <= 1700 and y_offset <= mouse_y <= y_offset + 50:
            pygame.draw.rect(surface, white, (1600, y_offset, 100, 50))
            draw_text(rarity, font, (0, 0, 0), surface, 1625, y_offset + 15)
        else:
            pygame.draw.rect(surface, gray, (1600, y_offset, 100, 50))
            draw_text(rarity, font, (0, 0, 0), surface, 1625, y_offset + 15)
        y_offset += 60