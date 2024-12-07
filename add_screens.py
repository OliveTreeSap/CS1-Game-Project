import sys
import pygame
from button import Button
from add_funcs import RenderText


#Set up pygame
pygame.init()


def lose_screen(screen):

    run = True
    #Return if the user want to restart or not
    restart = False

    #Set up the lose screen
    lose_screen = pygame.Rect(-1000, -1000, 640, 360)
    lose_screen.center = (640, 360)

    #Set up the restart and quit button
    restart_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640-25, y_pos=360, text_input="R")
    quit_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640+25, y_pos=360, text_input="Q")

    #blur the background
    blur = pygame.image.load("CS1\images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        for event in pygame.event.get():

            #Check if the user clicked the restart or quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.CheckForInput(pygame.mouse.get_pos()):
                    restart = True
                    run = False
                elif quit_button.CheckForInput(pygame.mouse.get_pos()):
                    restart = False
                    run = False

        #Display the lose screen
        pygame.draw.rect(surface=screen, color="red", rect=lose_screen)
        
        #Update the restart and quit button
        for button in [restart_button, quit_button]:
            button.ChangeColor(pygame.mouse.get_pos())
            button.Update(screen)

        #Update the screen
        pygame.display.update()

    return restart


def win_screen(screen):
    
    run = True

    #Set up the win screen
    win_screen = pygame.Rect(-1000, -1000, 640, 360)
    win_screen.center = (640, 360)

    #Set up the return to home button
    home_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640, y_pos=360, text_input="H")

    #blur the background
    blur = pygame.image.load("CS1\images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the home
            if event.type == pygame.MOUSEBUTTONDOWN:
                if home_button.CheckForInput(pygame.mouse.get_pos()):
                    home = True
                    run = False

        #Display the win screen
        pygame.draw.rect(surface=screen, color="green", rect=win_screen)
        
        #Update the home button
        home_button.ChangeColor(pygame.mouse.get_pos())
        home_button.Update(screen)

        #Update the screen
        pygame.display.update()

    return home


def incorrect_equation(screen):

    run = True

    #Set up the correction screen
    incorrect_equation = pygame.Rect(-1000, -1000, 640, 360)
    incorrect_equation.center = (640, 360)

    #Set up the ok button
    ok_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640, y_pos=360+25, text_input="K")

    #blur the background
    blur = pygame.image.load("CS1\images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the home
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.CheckForInput(pygame.mouse.get_pos()):
                    run = False

        #Display the correction screen
        pygame.draw.rect(surface=screen, color="white", rect=incorrect_equation)
        
        #Update the ok button
        ok_button.ChangeColor(pygame.mouse.get_pos())
        ok_button.Update(screen)

        #Display text warning the user
        RenderText(screen, 350, 360-50, "You inputted an incorrect equation", "Black", 32)

        #Update the screen
        pygame.display.update()

