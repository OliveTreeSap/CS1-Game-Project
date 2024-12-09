import sys
import pygame
import numpy as np
from button import Button
from add_screens import lose_screen, win_screen, incorrect_equation
from add_funcs import ln, log2, log10, sin, cos, tan, sqrt, exp, RenderText
from levels import GetLevel


#Math constants
pi = np.pi
e = np.e


#Set up pygame
pygame.init()

#Set up the display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Load the default font
base_font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", 32)


def MainMenu(screen, menu_font):

    #Set the window name to Menu
    pygame.display.set_caption("Menu")

    while True:

        #Set the background color
        screen.fill((202,228,241))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Display the main menu title/ game title
        RenderText(screen, 640, 100, "MAIN MENU", "black", 32, center=True)

        #Initialize the play, options and quit button
        play_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=250, text_input="PLAY")
        
        options_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=400, text_input="OPTIONS")
        
        quit_button = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"),
                             x_pos=640, y_pos=550, text_input="QUIT")
        
        #Update the visual of each button
        for button in [play_button, options_button, quit_button]:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Check if any of the three buttons is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Launch the main game
                if play_button.CheckForInput(pygame.mouse.get_pos()):
                    LevelSelector(screen, menu_font)
                #Switch to the options screen
                if options_button.CheckForInput(pygame.mouse.get_pos()):
                    Options(screen, menu_font)
                #Quit the game
                if quit_button.CheckForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def Options(screen, options_font):

    while True:

        #Back ground color
        screen.fill((202,228,241))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Display the options screen text
        RenderText(screen, 640, 260, "There is nothing here yet :(", "black", 32, center=True)

        #Initialize the back button
        options_back = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=640, y_pos=460, 
                            text_input="BACK")

        #Update the visual of the back button
        options_back.ChangeColor(mouse_pos)
        options_back.Update(screen)

        #Event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if the back button was clicked
                if options_back.CheckForInput(mouse_pos):
                    #Return to the main menu
                    MainMenu(screen, options_font)

        pygame.display.update()


def LevelSelector(screen, level_select_font):

    while True:

        #Back ground color
        screen.fill((202,228,241))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Set up the options screen text
        RenderText(screen, 640, 100, "Choose a level", "black", 32, center=True)

        #Initialize the back button
        level_select_back = Button(image=pygame.image.load("CS1\images\\pixilart-drawing.png"), x_pos=1180, y_pos=660, 
                            text_input="BACK")

        #Update the visual of the back button
        level_select_back.ChangeColor(mouse_pos)
        level_select_back.Update(screen)

        #list containing the level buttons
        level_buttons = []

        #Create each button for their respective levels
        for i in range(1, 7):
            button_image = pygame.image.load("CS1\images\\pixilart-drawing.png")
            button_image = pygame.transform.scale(button_image, (52, 52))
            level_buttons.append(Button(image=button_image, x_pos=182.857*i, y_pos=200, 
                            text_input=str(i)))
            
        #Update the visual of each level button
        for button in level_buttons:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                #Check if the back button was clicked
                if level_select_back.CheckForInput(mouse_pos):
                    #Return to the main menu
                    MainMenu(screen, level_select_font)
                
                #Check if any of the level button was clicked
                for button in level_buttons:
                    if button.CheckForInput(mouse_pos):
                        MainGameLogic(button.text_input)

        pygame.display.update()


def MainGameLogic(level):
    
    #Set up the display window
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1280

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("")

    #Rectangles for the window border
    top_rect = pygame.Rect(0, -1000000, 1280, 1000000)
    bottom_rect = pygame.Rect(0, 640, 1280, 1000080)
    left_rect = pygame.Rect(-1000000, 0, 1000000, 720)
    right_rect = pygame.Rect(1280, 0, 1000000, 720)

    #Initialize the clock
    clock = pygame.time.Clock()

    #Variables related to user input
    user_input = ""
    input_box = pygame.Rect(100, 650, 1020, 60)
    inputting = False

    #Set up the fire button
    fire_image = pygame.image.load("CS1\images\\pixilart-drawing.png")
    fire_image = pygame.transform.scale(fire_image, (60, 60))
    fire_button = Button(image=fire_image, x_pos=1200, y_pos=680, text_input="F")

    #Variables related to firing the projectile
    fire = False
    attepmt = True
    firing = False
    current_x = 0

    #Variables related to winning and losing
    lose = False
    win = False

    #Main loop of the game
    while True:

        #Set the background to a specific color
        screen.fill((202,228,241))

        #Draw the window border
        pygame.draw.rect(screen, "white", top_rect)
        pygame.draw.rect(screen, "white", bottom_rect)
        pygame.draw.rect(screen, "white", left_rect)
        pygame.draw.rect(screen, "white", right_rect)

        #Render the text box and input text
        if inputting:
            input_box_color = "green"
        else:
            input_box_color = "black"

        pygame.draw.rect(screen, input_box_color, input_box, 2)
        RenderText(screen=screen, x=input_box.x + 15, y=input_box.y + 5,
                text=user_input, color="black", size=32)
        RenderText(screen=screen, x=input_box.x - 60, y=input_box.y + 5,
                text="y =", color="black", size=32)

        #Update the state of the fire button
        fire_button.Update(screen)
        fire_button.ChangeColor(pygame.mouse.get_pos())

        #Load the level
        current_level = GetLevel(level)

        #Set up and display the target
        target = current_level[0]
        target.UpdateObject(screen)

        if len(current_level) > 1:
            for obstacle in current_level[1:]:
                obstacle.UpdateObject(screen)

        #The event handler
        for event in pygame.event.get():

            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Code to track mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    inputting = True
                else:
                    inputting = False
                
                if fire_button.CheckForInput(event.pos) and (attepmt == True):
                    fire = True

            #Code to track keyboard input
            if event.type == pygame.KEYDOWN:
                if inputting == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        #Check if the fire condition is True
        if fire:
            #Set attempt to False to avoid button spamming
            fire = attempt = False
            firing = True
            #Try to create the coordinates
            x = np.linspace(50, 1280, 1280)
            try:
                y = eval(user_input)+320
            #If not successful set attempt to True to allow reattempt from user
            except:
                attempt = True
                firing = False
                incorrect_equation(screen)


        #Animate the projectile
        if firing:
            projectile = pygame.Rect(-25, -25, 25, 25)
            projectile.center = (x[current_x], y[current_x])
            pygame.draw.rect(surface=screen, color="green", rect=projectile)
            current_x += 1
            #Code to check if the projectile is taking too long to reach the target
            if current_x > 1280:
                lose = True

            #Check if the projectile collided with the borders
            if projectile.colliderect(top_rect):
                lose = True
            elif projectile.colliderect(bottom_rect):
                lose = True
            elif projectile.colliderect(left_rect):
                lose = True
            elif projectile.colliderect(right_rect):
                lose = True

            #Check if the projectile collided with the obstacle(s)
            if len(current_level) > 1:
                for obstacle in current_level[1:]:
                    if obstacle.CheckColision(projectile):
                        lose = True

            #Check if the projectile collided with the target
            if target.CheckColision(projectile):
                win = True

            #Display the losing screen
            if lose:
                restart = lose_screen(screen)
                if restart:
                    MainGameLogic(level)
                else:
                    pygame.quit()
                    sys.exit()

            #Diplay the winning screen
            if win:
                if win_screen(screen):
                    LevelSelector(screen, base_font)

        #Set the speed of the game
        clock.tick(20000)

        #Update the screen
        pygame.display.update()


MainMenu(screen, base_font)