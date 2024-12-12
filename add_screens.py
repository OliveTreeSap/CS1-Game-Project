import sys
import pygame
from button import Button
from add_funcs import RenderText


#Set up pygame
pygame.init()


def lose_screen(screen, volume):

    run = True
    #Return if the user want to restart or not
    restart = False

    #Set up the lose screen
    lose_screen = pygame.Rect(-1000, -1000, 640, 360)
    lose_screen.center = (640, 360)

    #Set up the restart and quit button
    restart_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640-25, y_pos=360, text_input="R", volume=volume[0])
    quit_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640+25, y_pos=360, text_input="Q", volume=volume[0])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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


def win_screen(screen, volume):
    
    run = True

    #Set up the win screen
    win_screen = pygame.Rect(-1000, -1000, 640, 360)
    win_screen.center = (640, 360)

    #Set up the return to home button
    home_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=360, text_input="H", volume=volume[0])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
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


def incorrect_equation(screen, volume):

    run = True

    #Set up the correction screen
    incorrect_equation = pygame.Rect(-1000, -1000, 640, 360)
    incorrect_equation.center = (640, 360)

    #Set up the ok button
    ok_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=360+25, text_input="K", volume=volume[0])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
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
        RenderText(screen, 640, 360-50, "You inputted an incorrect equation", "Black", 32, center=True)

        #Update the screen
        pygame.display.update()


def pause_screen(screen, volume):

    run = True
    #Return the user actions
    resume = False

    #Set up the pause screen
    pause_screen = pygame.Rect(-1000, -1000, 640, 360)
    pause_screen.center = (640, 360)

    #Set up the resume and quit button
    resume_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640-25, y_pos=360, text_input="R", volume=volume[0])
    quit_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640+25, y_pos=360, text_input="Q", volume=volume[0])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the resume or quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.CheckForInput(pygame.mouse.get_pos()):
                    resume = True
                    run = False
                elif quit_button.CheckForInput(pygame.mouse.get_pos()):
                    resume = False
                    run = False
            
            #Check if the user pressed the esc key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    resume = True
                    run = False

        #Display the pause screen
        pygame.draw.rect(surface=screen, color="white", rect=pause_screen)
        
        #Update the resume and quit button
        for button in [resume_button, quit_button]:
            button.ChangeColor(pygame.mouse.get_pos())
            button.Update(screen)

        #Update the screen
        pygame.display.update()

    return resume