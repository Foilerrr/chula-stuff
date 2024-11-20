import pygame
import os
from shared_data import char_dict_player1, char_dict_player2, player_deck, gems
from gacha import start_gacha
from deck import start_deck

pygame.init()

char_dict_player1_L, char_dict_player2_L = char_dict_player1, char_dict_player2

char_dict_deck_all = char_dict_player1_L | char_dict_player2_L

screen_width = 1700
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Project: Recall")

root = os.getcwd()

clock = pygame.time.Clock()
running = True
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

    
class other:
    def __init__(self, name, health, damage, movement, range):
        self.name = name
        self.health = health
        self.damage = damage
        self.movement = movement
        self.range = range

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

char_dict_all = char_dict_common | char_dict_rare | char_dict_epic | char_dict_legendary

class Character_place:
    def __init__(self, name, image_path):
        self.name = name
        self.path = image_path
        self.ori_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.ori_image, (40, 40))
        self.placed = False
        self.x = 0
        self.y = 0

    def place(self, x, y):
        self.x = x
        self.y = y
        self.placed = True

    def remove(self):
        self.x = 0
        self.y = 0
        self.placed = False

class Grid:
    def __init__(self, column, row, size=40, gap=5):
        self.column = column
        self.row = row
        self.size = size
        self.gap = gap
        self.grid = []
        self.create_grid()

        self.grid_width = self.column * (self.size + self.gap) + self.gap
        self.grid_height = self.row * (self.size + self.gap) + self.gap

        self.grid_surface = pygame.Surface((self.grid_width, self.grid_height), pygame.SRCALPHA)
        self.grid_surface.fill((0, 0, 0, 0))

    def create_grid(self):
        for x in range(self.column):
            column = []
            for y in range(self.row):
                rect = pygame.Rect(x * (self.size + self.gap), y * (self.size + self.gap), self.size, self.size)
                cell = {'rect': rect,'color': (255, 255, 255, 130)}
                column.append(cell)
            self.grid.append(column)

    def draw(self):
        for x in range(self.column):
            for y in range(self.row):
                cell = self.grid[x][y]
                color = cell['color']
                rect = cell['rect']
                pygame.draw.rect(self.grid_surface, color, rect)

        screen.blit(self.grid_surface, (400, 25))
    
    def draw_prepare(self):
        ru = list(range(0,7)) + list(range(13,20))
        for x in range(self.column):
            for y in ru:
                cell = self.grid[x][y]
                color = (0,230,0,130)
                color = cell['color']
                rect = cell['rect']
                pygame.draw.rect(self.grid_surface, color, rect)

        screen.blit(self.grid_surface, (400, 25))

    def get_cell_at_pos(self, pos):
        adpos = (pos[0]-400,pos[1]-25)
        for x in range(self.column):
            for y in range(self.row):
                if self.grid[x][y]["rect"].collidepoint(adpos):
                    return x, y
        return None

    def highlight_cell(self, x, y, color=(0, 255, 0, 150)):
        if 0 <= x < self.column and 0 <= y < self.row:
            self.grid[x][y]['color'] = color
    
    def highlight_attack(self, x, y, color=(255, 0, 0, 150)):
        if 0 <= x < self.column and 0 <= y < self.row:
            if self.grid[x][y]['color'] != (0, 255, 0, 150):
                self.grid[x][y]['color'] = color

    def reset_highlights(self):
        for x in range(self.column):
            for y in range(self.row):
                cell = self.grid[x][y]
                cell['color'] = (255, 255, 255, 130) 
    
    def reset_grid(self):
        self.grid = []
        self.create_grid()
        self.grid_surface.fill((0, 0, 0, 0))
        

class Game:
    def __init__(self):
        self.current_state = "menu"
        self.turn = 1
        self.selected_char = None
        self.selected_pic = None
        self.selected_target = None
        self.attacked_character = []
        self.font_path = {}
        self.placed_characters = []
        self.character_images = {}
        self.background_images = {}
        self.moved_character = []
        self.grid = Grid(20, 20)
        self.load_characters()
        self.load_background()
        self.load_font()

    def load_characters(self):
        for char in char_dict_all:
            path = self.find_file(root, f"L - {char}_Profile (2).png")
            if path:
                self.character_images[char] = Character_place(char, path)

    def load_font(self):
        font_names = ["AncientModernTales-a7Po","MadHackerItalic-8EOz"]
        for name in font_names:
            path0 = self.find_file(root, f"{name}.ttf")
            if path0:
                self.font_path[name] = path0
            
    def load_background(self):
        background_names = ['mainback',"dirt"]
        for back in background_names:
            path = self.find_file(root, f"{back}.png")
            if path:
                self.background_images[back] = pygame.transform.scale(pygame.image.load(path), (screen_width, screen_height))

    def find_file(self, start_path, file_name):
        for dirpath, dirnames, filenames in os.walk(start_path):
            if file_name in filenames:
                return os.path.join(dirpath, file_name)
        return None

    def select_char(self, char_name):
        self.selected_char = self.character_images.get(char_name)

    def select_pic(self,pos):
        if self.current_state == "battle":
            for char in self.placed_characters:
                self.char_rect = pygame.Rect(char.x * (self.grid.size + self.grid.gap) + 400,char.y * (self.grid.size + self.grid.gap) + 25,char.image.get_width(),char.image.get_height())
                if self.char_rect.collidepoint(pos):
                    if self.selected_pic != char.name:
                        self.selected_pic = char.name
                        self.grid.reset_highlights()
                        selected_character = char_dict_all.get(self.selected_pic)
                        if selected_character:
                            self.highlight_movement_range(self.selected_pic, selected_character.movement, selected_character.movement)

    def select_target(self,pos):
        if self.current_state == "battle":
            for char in self.placed_characters:
                self.char_rect = pygame.Rect(char.x * (self.grid.size + self.grid.gap) + 400,char.y * (self.grid.size + self.grid.gap) + 25,char.image.get_width(),char.image.get_height())
                if self.char_rect.collidepoint(pos):
                    if self.selected_target != char.name:
                        self.selected_target = char.name

    def place_char(self, pos):
        if self.selected_char:
            name = self.selected_char.name
            cell_pos = self.grid.get_cell_at_pos(pos)
            if cell_pos and not self.selected_char.placed:
                x, y = cell_pos
                if name in char_dict_player1_L and (13 <= y < 20):
                    self.selected_char.place(x, y)
                    self.placed_characters.append(self.selected_char)
                elif name in char_dict_player2_L and 0 <= y <  7:
                    self.selected_char.place(x, y)
                    self.placed_characters.append(self.selected_char)

    def remove_char(self, pos):
        if self.selected_char and self.selected_char.placed:
            cell_pos = self.grid.get_cell_at_pos(pos)
            if cell_pos:
                self.selected_char.remove()
                self.placed_characters.remove(self.selected_char)
    
    def remove_character(self, name, char_dict):
        character = char_dict.pop(name, None)
        if character and character in self.placed_characters:
            self.placed_characters.remove(character)
            print(f"{name} has been removed from the screen.")

    def draw(self):
        for char in self.placed_characters:
            screen.blit(char.image, (char.x * (self.grid.size + self.grid.gap) + 400, char.y * (self.grid.size + self.grid.gap) + 25))

    def run(self):
        global running, mouse, click
        while running:
            clock.tick(120)
            screen.fill((0, 0, 0)) 

            if self.current_state == "menu":
                self.draw_menu()
            elif self.current_state == "game":
                self.draw_game()
            elif self.current_state == "gacha":
                start_gacha(screen)
                self.current_state = "menu"
            elif self.current_state == "collection":
                start_deck(screen)
                self.current_state = "menu"
            elif self.current_state == "battle":
                self.draw_battle()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        if self.current_state == "game":
                            self.place_char(pygame.mouse.get_pos())
                        elif self.current_state == "battle":
                            if not self.selected_pic:
                                self.select_pic(pygame.mouse.get_pos())
                            elif self.selected_pic:
                                if self.selected_pic and self.selected_pic not in self.moved_character:
                                    cell_pos = self.grid.get_cell_at_pos(pygame.mouse.get_pos()) 
                                    self.move(self.selected_pic, cell_pos)  
                                    self.grid.reset_highlights()
                                elif self.selected_pic and self.selected_pic not in self.attacked_character:
                                    self.select_target(pygame.mouse.get_pos())
                                    self.attack(self.selected_pic,self.selected_target)
                                self.selected_pic = None
                    elif event.button == 3: 
                        if self.current_state == "game":
                            self.remove_char(pygame.mouse.get_pos())

    def draw_menu(self):
        background = self.background_images.get("mainback")
        fontz = self.font_path.get("AncientModernTales-a7Po")
        logo = pygame.font.Font(fontz,150) 
        screen.blit(background, (0, 0))
        self.draw_text("Project: Recall", logo, (255, 255, 255), screen, screen_width / 2, 125)
        self.create_button("Play", screen_width / 2 - 150, 250, 300, 100, (255, 255, 255), (0, 0, 0), 45, self.start_game)
        self.create_button("Gacha", screen_width / 2 - 150, 375, 300, 100, (255, 255, 255), (0, 0, 0), 45, self.start_gacha)
        self.create_button("Deck", screen_width / 2 - 150, 500, 300, 100, (255, 255, 255), (0, 0, 0), 45, self.start_collection)
        self.create_button("Quit", screen_width / 2 - 150, 750, 300, 100, (255, 255, 255), (0, 0, 0), 45, self.quit_game)

    def create_button(self, msg, x, y, w, h, ic, ac, k, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        fontz = self.font_path.get("AncientModernTales-a7Po")
        smallText = pygame.font.Font(fontz,40)

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))
            text_color = (255, 255, 255)
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
            text_color = (0, 0, 0)

        textSurf = smallText.render(msg, True, text_color)
        textRect = textSurf.get_rect()
        textRect.center = (x + (w / 2), y + (h / 2))
        screen.blit(textSurf, textRect)

    def create_butend(self, msg, x, y, w, h, ic, ac, k, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.event.get(pygame.MOUSEBUTTONUP)

        fontz = self.font_path.get("AncientModernTales-a7Po")
        smallText = pygame.font.Font(fontz,40)

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))
            text_color = (255, 255, 255)
            if click and action is not None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
            text_color = (0, 0, 0)

        textSurf = smallText.render(msg, True, text_color)
        textRect = textSurf.get_rect()
        textRect.center = (x + (w / 2), y + (h / 2))
        screen.blit(textSurf, textRect)

    def charbutton(self, msg, x, y, w, h, ic, ac, k, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        fontz = self.font_path.get("AncientModernTales-a7Po")
        smallText = pygame.font.Font(fontz,30)
        
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))
            text_color = (255, 255, 255)
            charfile = self.character_images.get(msg)
            if charfile is not None:
                charpho = pygame.transform.scale(charfile.ori_image,(250,300))
                screen.blit(charpho, (x,50))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
            text_color = (0, 0, 0)

        textSurf = smallText.render(msg, True, text_color)
        textRect = textSurf.get_rect()
        textRect.center = (x + (w / 2), y + (h / 2))
        screen.blit(textSurf, textRect)

    def stat_show(self, x, y, w, h, k, selected_character):

        fontz = self.font_path.get("AncientModernTales-a7Po")
        smallText = pygame.font.Font(fontz,40)

        title = smallText.render("Stats", True, (255,255,255))
        hp_text = smallText.render(f"HP: {selected_character.health}", True, (255,255,255))
        damage_text = smallText.render(f"Damage: {selected_character.damage}", True, (255,255,255))
        movement_text = smallText.render(f"Movement: {selected_character.movement}", True, (255,255,255))
        range_text = smallText.render(f"Range: {selected_character.range}", True, (255,255,255))
    
        pygame.draw.rect(screen, (0, 0, 0), [x, y, w, h]) 
        screen.blit(title, (x + 5, y + 5)) 
        screen.blit(hp_text, (x + 5, y + 35))  
        screen.blit(damage_text, (x + 5, y + 65))  
        screen.blit(movement_text, (x + 5, y + 95)) 
        screen.blit(range_text, (x + 5, y + 125))  
    
        pygame.draw.rect(screen, (255, 255, 255), [x, y, w, h], 2)

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def window(self):

        semi = pygame.Surface((250, 300), pygame.SRCALPHA)
        semi.fill((255, 255, 255, 125))

        self.rect1 = pygame.Rect(75,50,250,300)
        screen.blit(semi,self.rect1)

        self.rect2 = pygame.Rect(1375,50,250,300)
        screen.blit(semi,self.rect2)
    
    def highlight_attack_range(self,name):
        ranger = char_dict_all[name].range
        for char in self.placed_characters:
            if char.name == name:
                base_x, base_y = char.x, char.y
                break
        else:
            return

        for dx in range(-ranger,ranger+1):
            for dy in range(-ranger,ranger+1):
                if 0 <= base_x + dx < self.grid.column and 0 <= base_y + dy < self.grid.row:
                        self.grid.highlight_attack(base_x + dx, base_y + dy)

    def highlight_movement_range(self, name, move_x, move_y):
        self.grid.reset_highlights()  # Reset highlights before highlighting movement range
        if self.selected_pic not in self.moved_character:
            for char in self.placed_characters:
                if char.name == name:
                    base_x, base_y = char.x, char.y
                    break
            else:
                return

            for dx in range(-move_x, move_x + 1):
                for dy in range(-move_y, move_y + 1):
                    if 0 <= base_x + dx < self.grid.column and 0 <= base_y + dy < self.grid.row:
                        self.grid.highlight_cell(base_x + dx, base_y + dy)
    
    def attack(self, attacker, victim):
        if attacker not in self.attacked_character:
            if attacker in char_dict_player1_L:
                damage = char_dict_player1_L[attacker].damage
                if victim in char_dict_player2_L and victim != attacker:
                    char_dict_player2_L[victim].health -= damage
                    print(f"{attacker} attacked {victim} for {damage} damage. {victim}'s health is now {char_dict_player2_L[victim].health}.")
                    if char_dict_player2_L[victim].health <= 0:
                        self.remove_character(victim, char_dict_player2_L)
            elif attacker in char_dict_player2_L:
                damage = char_dict_player2_L[attacker].damage
                if victim in char_dict_player1_L and victim != attacker:
                    char_dict_player1_L[victim].health -= damage
                    print(f"{attacker} attacked {victim} for {damage} damage. {victim}'s health is now {char_dict_player1_L[victim].health}.")
                    if char_dict_player1_L[victim].health <= 0:
                        self.remove_character(victim, char_dict_player1_L)
        else:
            print(f"{attacker} has already attacked.")

    def remove_character(self, name, char_dict):
        character = char_dict[name]
        if character in self.placed_characters:
            self.placed_characters.remove(character)
            print(f"{name} has been removed from the screen.")
    
    def move(self, name, pos):
        if self.selected_pic not in self.moved_character:
            selected_character = self.character_images.get(name)
            if pos:
                x, y = pos
                cell_info = self.grid.grid[x][y]
                # Check if the cell is occupied by another character
                if (x, y) != (selected_character.x, selected_character.y) and any(char.x == x and char.y == y for char in self.placed_characters):
                    print(f"Cannot move {name} to ({x}, {y}): Cell is already occupied.")
                    return
                if selected_character in self.placed_characters and cell_info['color'] == (0, 255, 0, 150):
                    self.placed_characters.remove(selected_character)
                    selected_character.place(x, y)
                    self.placed_characters.append(selected_character)
                    self.moved_character.append(self.selected_pic)
                    self.grid.reset_highlights()
            else:
                pass
    
    def end_turn(self):
        if self.turn == 1:
            self.turn += 1
        elif self.turn == 2:
            self.turn -= 1
        self.moved_character.clear()
        self.attacked_character.clear()

    def start_menu(self):
        self.current_state = "menu"

    def start_menu_b(self):
        char_dict_player1_L.clear()
        char_dict_player2_L.clear()
        self.current_state = "menu"

    def start_game(self):
        self.grid.reset_grid()
        self.grid.draw_prepare()
        self.current_state = "game"
        self.turn = 1
        self.selected_char = None
        self.selected_pic = None
        self.selected_target = None
        self.attacked_character = []
        self.placed_characters = []
        self.moved_character = []

    def start_gacha(self):
        self.current_state = "gacha"

    def start_collection(self):
        self.current_state = "collection"

    def start_battle(self):
        self.current_state = "battle"

    def quit_game(self):
        pygame.quit()
        quit()

    def draw_game(self):
        self.grid.reset_grid()
        background = self.background_images.get("mainback") 
        screen.blit(background, (0, 0))
        self.grid.draw_prepare()
        self.window()
        self.draw()
        self.draw_deck()
        self.create_button("battle", 150, 10, 100, 30, (255,255,255), (0,0,0), 30, self.start_battle)
        self.create_button("back", 1450, 10, 100, 30, (255,255,255), (0,0,0), 30, self.start_menu_b)
        
    def draw_deck(self):
        deck1 = char_dict_player1_L
        charac_space = 400
        for charac in deck1:
            self.charbutton(str(charac), 75, charac_space, 250, 30, (255, 255, 255), (0, 0, 0), 30, lambda charac=charac: self.select_char(charac))
            charac_space += 50

        deck2 = char_dict_player2_L
        charac_space = 400
        for charac in deck2:
            self.charbutton(str(charac), 1375, charac_space, 250, 30, (255, 255, 255), (0, 0, 0), 30, lambda charac=charac: self.select_char(charac))
            charac_space += 50

    def draw_battle(self):
        char_dict_deck_all = char_dict_player1_L | char_dict_player2_L
        background = self.background_images.get("mainback") 
        screen.blit(background, (0, 0))
        self.window()
        self.grid.draw()
        self.draw()
        self.create_butend("End", 1450, 10, 100, 30, (255, 255, 255), (0, 0, 0), 30, self.end_turn)
        self.create_button(str(self.turn), 150, 10, 100, 30, (255, 255, 255), (0, 0, 0), 30, None)
        self.create_button("back", 1450, 900, 100, 30, (255,255,255), (0,0,0), 30, self.start_menu_b)
        
        for char in list(self.placed_characters): 
            if char_dict_deck_all[char.name].health <= 0:
                self.placed_characters.remove(char)
                if char.name in char_dict_player1_L:
                    del char_dict_player1_L[char.name]
                elif char.name in char_dict_player2_L:
                    del char_dict_player2_L[char.name]
            print(char.name)
    

       
        if len(char_dict_player1_L) == 0:
            self.display_win_screen("Player 2 Wins!")

        elif len(char_dict_player2_L) == 0:
            self.display_win_screen("Player 1 Wins!")
            

        if self.selected_pic:
            self.grid.reset_highlights()
            selected_character = char_dict_deck_all.get(self.selected_pic)
            image = self.character_images.get(self.selected_pic)
            if selected_character:
                scaled_image = pygame.transform.scale(image.ori_image, (250, 300))
                if scaled_image:
                    if self.selected_pic in char_dict_player1_L and self.turn == 1:
                        self.highlight_movement_range(self.selected_pic, 2, 2)
                        self.highlight_attack_range(self.selected_pic) 
                        screen.blit(scaled_image, (75, 50))
                        self.stat_show(100, 400, 200, 200, 20, selected_character)
                    elif self.selected_pic in char_dict_player2_L and self.turn == 2:
                        self.highlight_movement_range(self.selected_pic, 2, 2)
                        self.highlight_attack_range(self.selected_pic) 
                        screen.blit(scaled_image, (75, 50))
                        self.stat_show(100, 400, 200, 200, 20, selected_character)

        pygame.display.update()

    def display_win_screen(self, message):
        screen.fill((0, 0, 0))  
        font = pygame.font.Font(None, 74)
        text = font.render("WIN", True, (255, 255, 255))
        msg = font.render(message, True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
        screen.blit(msg, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2+150))
        self.moved_character.clear()
        self.attacked_character.clear()
        self.placed_characters.clear()
        char_dict_player2_L.clear()
        char_dict_player2_L.clear()
        self.start_menu()
        pygame.display.update()
        pygame.time.wait(3000)

        pygame.display.update()

game = Game()
game.run()