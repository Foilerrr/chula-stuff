import pygame

pygame.init()

# screennnn
screen = pygame.display.set_mode((800,600)) # ( width , height )

# title
pygame.display.set_caption("Gacha")

# player
playerImg = pygame.image.load()

# game loop
running = True
while running:
    # pygame.event.get() is kinda just every event happening in this main here (eg. mouse clicks, key presses etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0)) # R G B color
    pygame.display.update()
