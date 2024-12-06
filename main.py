import pygame, sys
from button import Button


pygame.init()

#set up screen resolution and surface
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set up game font
base_font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", 32)


def MainMenu(screen, menu_font):
    pygame.display.set_caption("Menu")

    while True:
        screen.fill((202,228,241))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = menu_font.render("MAIN MENU", True, "black")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=250, text_input="PLAY")
        
        options_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=400, text_input="OPTIONS")
        
        quit_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=550, text_input="QUIT")
        
        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.CheckForInput(pygame.mouse.get_pos()):
                    Play(screen, menu_font)
                if options_button.CheckForInput(pygame.mouse.get_pos()):
                    Options(screen, menu_font)
                if quit_button.CheckForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def Options(screen, options_font):
    while True:
        screen.fill((202,228,241))

        mouse_pos = pygame.mouse.get_pos()

        options_text = options_font.render("This is the OPTIONS screen.", True, "Black")
        options_rect = options_text.get_rect(center=(640, 260))
        screen.blit(options_text, options_rect)

        options_back = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640, y_pos=460, 
                            text_input="BACK")

        options_back.ChangeColor(mouse_pos)
        options_back.Update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.CheckForInput(mouse_pos):
                    MainMenu(screen, options_font)

        pygame.display.update()

def Play(screen, game_font):
    while True:
        screen.fill((202,228,241))

        mouse_pos = pygame.mouse.get_pos()

        play_text = game_font.render("This is the PLAY screen.", True, "White")
        play_rect = play_text.get_rect(center=(640, 260))
        screen.blit(play_text, play_rect)

        play_back = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640, y_pos=460, 
                            text_input="BACK")

        play_back.ChangeColor(mouse_pos)
        play_back.Update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.CheckForInput(mouse_pos):
                    MainMenu(screen, game_font)

        pygame.display.update()


MainMenu(screen, base_font)