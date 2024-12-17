import sys
import pygame
import numpy as np
from button import Button
from slider import Slider
from add_screens import lose_screen, win_screen, incorrect_equation, pause_screen, congrats, tutorial
from add_funcs import ln, log2, log10, sin, cos, tan, sqrt, exp, RenderText
from levels import GetLevel, GetNumLevel


#Math constants
pi = np.pi
e = np.e


#Set up pygame
pygame.init()

#Set up the display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Load the fonts
base_font_1 = pygame.font.Font("Grand9K_Pixel.ttf", 40)
base_font_2 = pygame.font.Font("Grand9K_Pixel.ttf", 35)
base_font_3 = pygame.font.Font("Grand9K_Pixel.ttf", 30)
base_font_4 = pygame.font.Font("Grand9K_Pixel.ttf", 25)
base_font_5 = pygame.font.Font("Grand9K_Pixel.ttf", 20)
base_font_6 = pygame.font.Font("Grand9K_Pixel.ttf", 55)
base_font_7 = pygame.font.Font("Grand9K_Pixel.ttf", 15)

fonts = [base_font_1, base_font_2, base_font_3, base_font_4, base_font_5, base_font_6, base_font_7]

#Easy mode which lenghten the trajectory enough to reach the target
Difficulty = 0

#Initial volumn of music and sound effects
music_volume = 0.25
sfx_volume = 0.75
Volume = [music_volume, sfx_volume]

#Load the backgrounds
menu_background = pygame.image.load("images/backgrounds/menu_background.jpg").convert()
menu_background = pygame.transform.scale(menu_background, (1280, 720))

level_selector_background = pygame.image.load("images/backgrounds/level_selector_background.png").convert()
level_selector_background = pygame.transform.scale(level_selector_background, (1280, 720))

levels_background = []
for i in range(1, 7):
    level_background = pygame.image.load("images/backgrounds/background_lv_" + str(i) + ".png").convert()
    level_background = pygame.transform.scale(level_background, (1280, 720))
    levels_background.append(level_background)

title = pygame.image.load("images/backgrounds/title_background.jpg").convert()
title = pygame.transform.scale(title, (1280, 720))

#Load the button images
default_button = pygame.image.load("images/buttons/default_button.png").convert_alpha()
default_button = pygame.transform.scale(default_button, (250, 60))

default_button_short = pygame.image.load("images/buttons/default_button.png").convert_alpha()
default_button_short = pygame.transform.scale(default_button_short, (200, 60))

square_button = pygame.image.load("images/buttons/square_button.png").convert_alpha()
square_button = pygame.transform.scale(square_button, (120, 120))

on_button = pygame.image.load("images/buttons/easy_button.png").convert_alpha()
on_button = pygame.transform.scale(on_button, (150, 50))

off_button = pygame.image.load("images/buttons/hard_button.png").convert_alpha()
off_button = pygame.transform.scale(off_button, (150, 50))

#Load the character images
alde = pygame.image.load("images/character/alde.png").convert_alpha()
alde = pygame.transform.scale(alde, (100, 100))

alde_shoot = pygame.image.load("images/character/alde_side.png").convert_alpha()
alde_shoot = pygame.transform.scale(alde_shoot, (115.79, 115.79))

#Load the projectile image
bullet_1 = pygame.image.load("images/bullets/bullet_1.png").convert_alpha()
bullet_1 = pygame.transform.scale(bullet_1, (25, 25))

bullet_2 = pygame.image.load("images/bullets/bullet_2.png").convert_alpha()
bullet_2 = pygame.transform.scale(bullet_2, (25, 25))

bullets = [bullet_1, bullet_2]


def MainMenu(screen, menu_font, difficulty, volume):

    #Load and play the main menu music
    pygame.mixer.music.load("sounds\BitMenu.mp3")
    pygame.mixer.music.set_volume(volume[0])
    pygame.mixer.music.play(loops=-1, fade_ms=2500)

    #Set the window name to Menu
    pygame.display.set_caption("Menu")

    #Initialize the play, options and quit button
    play_button = Button(image=default_button,
                         x_pos=919.2, y_pos=350, text_input="PLAY", font=menu_font[2],volume=volume[1])
    
    options_button = Button(image=default_button,
                            x_pos=919.2, y_pos=435, text_input="OPTIONS", font=menu_font[2], volume=volume[1])
    
    quit_button = Button(image=default_button,
                         x_pos=919.2, y_pos=520, text_input="QUIT", font=menu_font[2], volume=volume[1])

    while True:

        #Set the background
        screen.blit(menu_background, (0, 0))
        screen.blit(title, (0, 0), (0, 0, 720, 187))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Display the main menu title/ game title
        RenderText(screen, 919.2, 250, "MAIN MENU", "black", font=menu_font[0], center=True)

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
                    LevelSelector(screen, menu_font, difficulty, volume)
                #Switch to the options screen
                if options_button.CheckForInput(pygame.mouse.get_pos()):
                    Options(screen, menu_font, difficulty, volume)
                #Quit the game
                if quit_button.CheckForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def Options(screen, options_font, difficulty, volume):

    #Initialize the back button
    options_back = Button(image=default_button_short, x_pos=919.2, y_pos=610, 
                          text_input="Back", font=options_font[3], volume=volume[1])
    
    tutorial_button = Button(image=default_button_short, x_pos=919.2, y_pos=530,
                             text_input="Tutorial", font=options_font[3], volume=volume[1])
    
    #Initialize the easy and hard mode switch
    easy_mode_button = Button(image=on_button, x_pos=919.2-100, y_pos=430, 
                              text_input="Easy Mode",switch=True, state=(True if difficulty == 1 else False),
                              alt_image=off_button, font=options_font[4], volume=volume[1])
    
    hard_mode_button = Button(image=on_button, x_pos=919.2+100, y_pos=430, 
                              text_input="Hard Mode",switch=True, state=(True if difficulty == -1 else False),
                              alt_image=off_button, font=options_font[4], volume=volume[1])
    
    music_slider = Slider((919.2-150, 325), (200, 25), volume[0], 0, 1, "Music volume: ", label_font=options_font[3], value_font=options_font[6])

    sfx_slider = Slider((919.2+130, 325), (200, 25), volume[1], 0, 1, "SFX volume: ", label_font=options_font[3], value_font=options_font[6])

    sliders = [music_slider, sfx_slider]

    while True:

        #Back ground color
        screen.blit(menu_background, (0, 0))

        #Display the options screen text
        RenderText(screen, 919.2, 245, "Options", "black", font=options_font[2], center=True)

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Update the buttons and switches
        for button in [easy_mode_button, hard_mode_button, options_back, tutorial_button]:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Update the visual of the sliders
        for slider in sliders:
            slider.UpdateSlider(screen)
            slider.DisplayValue(screen)
            slider.DisplayLabel(screen)

        #Render difficulty text and some information
        RenderText(screen, 919.2, 375, "Difficulty", "black", font=options_font[3], center=True)
        RenderText(screen, 919.2, 470, "Note: the most rencently clicked button will take priority!", "darkgray", font=options_font[6], center=True)

        
        #Event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Handles mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #Changes the difficulty
                if easy_mode_button.CheckForInput(mouse_pos):
                    difficulty = 1
                if hard_mode_button.CheckForInput(mouse_pos):
                    difficulty = -1
                if (not easy_mode_button.state) and (not hard_mode_button.state):
                    difficulty = 0

                if options_back.CheckForInput(mouse_pos):
                    #Return to the main menu
                    MainMenu(screen, options_font, difficulty, volume)

                if tutorial_button.CheckForInput(mouse_pos):
                    #Open the tutorial screen
                    tutorial(screen, volume, font=options_font)


        #Check if the user is holding down left click
        #and move the button of the slider to the appropriate location
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            for i in range(len(sliders)):
                if sliders[i].container_rect.collidepoint(mouse_pos):
                        sliders[i].MoveSlider(mouse_pos)
                        volume[i] = sliders[i].GetValue()


        pygame.display.update()


def LevelSelector(screen, level_select_font, difficulty, volume):

    #list containing the level buttons
    level_buttons = []

    #Initialize the back button
    level_select_back = Button(image=default_button, x_pos=1125, y_pos=670, 
                        text_input="BACK", font=level_select_font[2], volume=volume[1])
    
    #Create each button for their respective levels
    for i in range(1, 4):
        level_buttons.append(Button(image=square_button, x_pos=241*(i-1)+308.26, y_pos=290+8.55*(i-1), 
                        text_input=str(i), font=level_select_font[0], volume=volume[1]))
        
    for i in range(4, 7):
        level_buttons.append(Button(image=square_button, x_pos=241*(i-4)+428.53, y_pos=449.27+8.55*(i-4), 
                        text_input=str(i), font=level_select_font[0], volume=volume[1]))

    while True:

        #Display the back ground
        screen.blit(level_selector_background, (0, 0))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Set up the options screen text
        RenderText(screen, 502.25, 119, "Choose a level", "white", font=level_select_font[5], center=True)
        RenderText(screen, 498.25, 115, "Choose a level", "black", font=level_select_font[5], center=True)

        #Update the visual of the back button
        level_select_back.ChangeColor(mouse_pos)
        level_select_back.Update(screen)
            
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
                    MainMenu(screen, level_select_font, difficulty, volume)
                
                #Check if any of the level button was clicked
                for button in level_buttons:
                    if button.CheckForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        MainGameLogic(button.text_input, level_select_font,difficulty, volume)

        pygame.display.update()


def MainGameLogic(level, game_font, difficulty, volume):
    
    #Changes the title of the window
    pygame.display.set_caption("Level " + level)

    #Rectangles for the window border
    top_rect = pygame.Rect(0, -1000000, 1280, 1000000)
    bottom_rect = pygame.Rect(0, 640, 1280, 1000080)
    left_rect = pygame.Rect(-1000000, 0, 1000000, 720)
    right_rect = pygame.Rect(1280, 0, 1000000, 720)

    #Rectangle for platform
    platform = pygame.Rect(0, 356, 100, 15)

    #Initialize the clock
    clock = pygame.time.Clock()

    #Variables related to user input
    user_input = ""
    input_box = pygame.Rect(100, 650, 1020, 60)
    inputting = False

    #Input cursor
    cursor = len(user_input)
    cursor_color = "lightgray"

    #Set up the fire button
    fire_image = square_button
    fire_image = pygame.transform.scale(fire_image, (70, 70))
    fire_button = Button(image=fire_image, x_pos=1200, y_pos=680, text_input="F", font=game_font[2],volume=volume[1])

    #Variables related to firing the projectile
    fire_sfx = pygame.mixer.Sound("sounds/fire.mp3")
    pygame.mixer.Sound.set_volume(fire_sfx, volume[0])
    fire = False
    attempt = True
    firing = False
    current_x = 0
    x = np.linspace(0, 1280, 1280)+120

    #Variables related to winning and losing
    lose = False
    win = False

    #Losing and winning sound effects
    win_sfx = pygame.mixer.Sound("sounds/win.wav")
    lose_sfx = pygame.mixer.Sound("sounds/lose.mp3")
    pygame.mixer.Sound.set_volume(win_sfx, volume[0])
    pygame.mixer.Sound.set_volume(lose_sfx, volume[0])

    #Load and play the music of the game
    pygame.mixer.music.load("sounds\FunnyBit.mp3")
    pygame.mixer.music.set_volume(volume[0])
    pygame.mixer.music.play(loops=-1, fade_ms=2500)

    #Level background
    background = levels_background[int(level) - 1]

    bullet_randomizer = np.random.randint(0, 2)

    #Main loop of the game
    while True:

        #Set the background to a specific color
        screen.blit(background, (0, 0))

        #Calculate the coordinates of the trajectory of the projectile
        trajectory = False
        try:
            x_trajectory = x[:640*(1+difficulty):10]
            y_trajectory = (-1*eval(user_input)+320)[:640*(1+difficulty):10]
            trajectory = True
        except:
            trajectory = False

        #Draw the trajectory of the projectile
        if attempt and trajectory:
            for dot in range(len(y_trajectory)):
                pygame.draw.circle(screen, "black", (x_trajectory[dot], y_trajectory[dot]), 4)
                pygame.draw.circle(screen, "white", (x_trajectory[dot], y_trajectory[dot]), 2)

        #Draw the window border
        for border in [top_rect, bottom_rect, left_rect, right_rect]:
            pygame.draw.rect(screen, "azure2", border)

        #Changes the color of the input box if the user is typing
        if inputting:
            input_box_color = "green"
        else:
            input_box_color = "black"

        #Render the text box and input text
        pygame.draw.rect(screen, input_box_color, input_box, 2)
        RenderText(screen=screen, x=input_box.x - 60, y=input_box.y + 5,
                text="y =", color="black", font=game_font[2])
        RenderText(screen=screen, x=input_box.x + 15, y=input_box.y + 5,
                text=user_input[-50:], color="black", font=game_font[2])
        
        #Update the state of the fire button
        fire_button.Update(screen)
        fire_button.ChangeColor(pygame.mouse.get_pos())

        #Update the cursor_rect location
        cursor_pos = game_font[2].render(user_input[:cursor], True, "black").get_rect()
        cursor_rect = pygame.Rect(110 + cursor_pos[2], 660, 3, 40)

        #Draw the cursor
        pygame.draw.rect(screen, cursor_color, cursor_rect)

        #Load the level
        current_level = GetLevel(level)

        #Display the character and the platform
        pygame.draw.rect(screen, "black", platform)
        if not firing:
            screen.blit(alde, (20, 256))
        else:
            screen.blit(alde_shoot, (20, 260))

        #Set up and display the target
        target = current_level[0]
        target.UpdateObject(screen)

        #Load the obstacles
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
                    cursor_color = "black"
                else:
                    inputting = False
                    cursor_color = "lightgray"
                
                if fire_button.CheckForInput(event.pos) and (attempt == True):
                    fire = True

            #Code to track keyboard input
            if event.type == pygame.KEYDOWN:

                #Adjust the user input arcording to the keys pressed
                if inputting == True:
                    if event.key == pygame.K_BACKSPACE:
                        if cursor != 0:
                            user_input = user_input[:cursor-1] + user_input[cursor:]
                            cursor -= 1
                    elif event.key == pygame.K_DELETE:
                        user_input = user_input[:cursor] + user_input[cursor+1:]
                    elif event.key == pygame.K_HOME:
                        cursor = 0
                    elif event.key == pygame.K_END:
                        cursor = len(user_input)
                    elif event.key == pygame.K_LEFT:
                        if cursor != 0:
                            cursor -= 1
                    elif event.key == pygame.K_RIGHT:
                        if cursor != len(user_input):
                            cursor += 1
                    else:
                        if event.unicode :
                            user_input = user_input[:cursor] + event.unicode + user_input[cursor:]
                            cursor += 1

                #Display the pause if the user pressed the esc key
                if event.key == pygame.K_ESCAPE:
                    if pause_screen(screen, volume, font=game_font):
                        pass
                    else:
                        pygame.mixer.music.stop()
                        MainMenu(screen, game_font, difficulty, volume)

        #Check if the fire condition is True
        if fire:
            #Set attempt to False to avoid button spamming
            fire = attempt = False
            firing = True
            #Try to create the coordinates
            try:
                y = -1*eval(user_input)+320
                fire_sfx.play()
            #If not successful set attempt to True to allow reattempt from user
            except:
                attempt = True
                firing = False
                incorrect_equation(screen, volume, font=game_font)
            else:
                if "x" not in user_input:
                    attempt = True
                    firing = False
                    incorrect_equation(screen, volume, font=game_font)

        #Animate the projectile
        if firing:
            projectile = pygame.Rect(-25, -25, 25, 25)
            projectile.center = (x[current_x], y[current_x])
            projectile_image = bullets[bullet_randomizer]
            projectile_image_rect = projectile_image.get_rect()
            projectile_image_rect.center = (x[current_x], y[current_x])
            screen.blit(projectile_image, projectile_image_rect)
            # pygame.draw.rect(surface=screen, color="green", rect=projectile)
            
            current_x += 1
            #Code to check if the projectile is taking too long to reach the target
            if current_x > 1280:
                lose_sfx.play()
                lose = True

            #Check if the projectile collided with the borders
            for border in [top_rect, bottom_rect, left_rect, right_rect]:
                if border.colliderect(projectile):
                    lose_sfx.play()
                    lose = True

            #Check if the projectile collided with the obstacle(s)
            if len(current_level) > 1:
                for obstacle in current_level[1:]:
                    if obstacle.CheckColision(projectile):
                        lose_sfx.play()
                        lose = True

            #Check if the projectile collided with the target
            if target.CheckColision(projectile):
                win_sfx.play()
                win = True

            #Display the losing screen
            if lose:
                restart = lose_screen(screen, volume, game_font)
                if restart:
                    MainGameLogic(level, game_font, difficulty, volume)
                else:
                    pygame.mixer.music.stop()
                    #Reset the music
                    pygame.mixer.music.load("sounds\BitMenu.mp3")
                    pygame.mixer.music.set_volume(volume[0])
                    pygame.mixer.music.play(loops=-1, fade_ms=2500)
                    MainMenu(screen, game_font, difficulty, volume)

            #Diplay the winning screen
            if win:
                if win_screen(screen, volume, game_font):
                    pygame.mixer.music.stop()
                    #Reset the music
                    pygame.mixer.music.load("sounds\BitMenu.mp3")
                    pygame.mixer.music.set_volume(volume[0])
                    pygame.mixer.music.play(loops=-1, fade_ms=2500)
                    MainMenu(screen, game_font, difficulty, volume)
                else:
                    if int(level) == GetNumLevel():
                        congrats(screen, volume, game_font)
                        MainMenu(screen, game_font, difficulty, volume)
                    else:
                        MainGameLogic(str(int(level)+1), game_font, difficulty, volume)

        #Set the speed of the game
        clock.tick(360)

        #Update the screen
        pygame.display.update()


MainMenu(screen, fonts, Difficulty, Volume)