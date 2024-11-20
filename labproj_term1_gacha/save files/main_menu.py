import pygame
from gacha import start_gacha
from deck import start_deck

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1700
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)

# Font
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_home_screen(surface):
    surface.fill(black)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw the "Gacha" button
    if 700 <= mouse_x <= 900 and 400 <= mouse_y <= 450:
        pygame.draw.rect(surface, white, (700, 400, 200, 50))
        draw_text("Gacha", font, black, surface, 750, 415)
    else:
        pygame.draw.rect(surface, gray, (700, 400, 200, 50))
        draw_text("Gacha", font, black, surface, 750, 415)

    # Draw the "Deck" button
    if 700 <= mouse_x <= 900 and 500 <= mouse_y <= 550:
        pygame.draw.rect(surface, white, (700, 500, 200, 50))
        draw_text("Deck", font, black, surface, 750, 515)
    else:
        pygame.draw.rect(surface, gray, (700, 500, 200, 50))
        draw_text("Deck", font, black, surface, 750, 515)

def main():
    running = True
    current_screen = "home"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == "home":
                    if 700 <= pygame.mouse.get_pos()[0] <= 900 and 400 <= pygame.mouse.get_pos()[1] <= 450:
                        start_gacha(screen)
                        current_screen = "home"
                    elif 700 <= pygame.mouse.get_pos()[0] <= 900 and 500 <= pygame.mouse.get_pos()[1] <= 550:
                        start_deck(screen)
                        current_screen = "home"

        draw_home_screen(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()