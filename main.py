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

#Load the default font
base_font = pygame.font.Font("Grand9K_Pixel.ttf", 32)

#Easy mode which lenghten the trajectory enough to reach the target
Difficulty = 0

#Initial volumn of music and sound effects
music_volume = 0.25
sfx_volume = 0.75
Volume = [music_volume, sfx_volume]


def MainMenu(screen, menu_font, difficulty, volume):

    #Load and play the main menu music
    pygame.mixer.music.load("sounds\BitMenu.mp3")
    pygame.mixer.music.set_volume(volume[0])
    pygame.mixer.music.play(loops=-1, fade_ms=2500)

    #Set the window name to Menu
    pygame.display.set_caption("Menu")

    #Initialize the play, options and quit button
    play_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(),
                         x_pos=640, y_pos=250, text_input="PLAY", volume=volume[1])
    
    options_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(),
                            x_pos=640, y_pos=400, text_input="OPTIONS", volume=volume[1])
    
    quit_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(),
                         x_pos=640, y_pos=550, text_input="QUIT", volume=volume[1])

    while True:

        #Set the background color
        screen.fill((202,228,241))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Display the main menu title/ game title
        RenderText(screen, 640, 100, "MAIN MENU", "black", 32, font=menu_font, center=True)

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
    options_back = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=640, y_pos=660, 
                          text_input="BACK", volume=volume[1])
    
    tutorial_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=640, y_pos=550,
                             text_input="Tutorial", volume=volume[1])
    
    #Initialize the easy and hard mode switch
    easy_mode_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=540, y_pos=410, 
                              text_input="Easy Mode",switch=True, state=(True if difficulty == 1 else False),
                              alt_image=pygame.image.load("images\\pixilart-drawing_2.png"), volume=volume[1])
    
    hard_mode_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=740, y_pos=410, 
                              text_input="Hard Mode",switch=True, state=(True if difficulty == -1 else False),
                              alt_image=pygame.image.load("images\\pixilart-drawing_2.png").convert(), volume=volume[1])
    
    music_slider = Slider((640, 175), (250, 25), volume[0], 0, 1, "Music volume: ", font=options_font)

    sfx_slider = Slider((640, 275), (250, 25), volume[1], 0, 1, "Sound effects volume: ", font=options_font)

    sliders = [music_slider, sfx_slider]

    while True:

        #Back ground color
        screen.fill((202,228,241))

        #Display the options screen text
        RenderText(screen, 640, 50, "Options", "black", 32, font=options_font, center=True)

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
        RenderText(screen, 640, 350, "Difficulty", "black", 32, font=options_font, center=True)
        RenderText(screen, 640, 450, "Note: the most rencently clicked button will take priority!", "darkgray", 18, font=options_font, center=True)

        
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
    level_select_back = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=1180, y_pos=660, 
                        text_input="BACK", volume=volume[1])
    
    #Create each button for their respective levels
    for i in range(1, 7):
        button_image = pygame.image.load("images\\pixilart-drawing.png").convert()
        button_image = pygame.transform.scale(button_image, (52, 52))
        level_buttons.append(Button(image=button_image, x_pos=182.857*i, y_pos=200, 
                        text_input=str(i), volume=volume[1]))

    while True:

        #Back ground color
        screen.fill((202,228,241))

        #Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Set up the options screen text
        RenderText(screen, 640, 100, "Choose a level", "black", 32, font=level_select_font, center=True)

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

    #Initialize the clock
    clock = pygame.time.Clock()

    #Variables related to user input
    user_input = ""
    input_box = pygame.Rect(100, 650, 1020, 60)
    inputting = False

    #Input cursor
    cursor = len(user_input)
    cursor_blink_timer = 0

    #Set up the fire button
    fire_image = pygame.image.load("images\\pixilart-drawing.png").convert()
    fire_image = pygame.transform.scale(fire_image, (60, 60))
    fire_button = Button(image=fire_image, x_pos=1200, y_pos=680, text_input="F", volume=volume[1])

    #Variables related to firing the projectile
    fire_sfx = pygame.mixer.Sound("sounds/fire.mp3")
    pygame.mixer.Sound.set_volume(fire_sfx, volume[0])
    fire = False
    attempt = True
    firing = False
    current_x = 0
    x = np.linspace(0, 1280, 1280)+50

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

    #Main loop of the game
    while True:

        #Set the background to a specific color
        screen.fill((202,228,241))

        #Calculate the coordinates of the trajectory of the projectile
        trajectory = False
        try:
            x_trajectory = x[:640*(1+difficulty):20]
            y_trajectory = (-1*eval(user_input)+320)[:640*(1+difficulty):20]
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
            pygame.draw.rect(screen, "white", border)

        #Changes the color of the input box if the user is typing
        if inputting:
            input_box_color = "green"
        else:
            input_box_color = "black"

        #Render the text box and input text
        pygame.draw.rect(screen, input_box_color, input_box, 2)
        RenderText(screen=screen, x=input_box.x - 60, y=input_box.y + 5,
                text="y =", color="black", size=32, font=game_font)
        RenderText(screen=screen, x=input_box.x + 15, y=input_box.y + 5,
                text=user_input[-50:], color="black", size=32, font=game_font)
        
        #Update the cursor_rect location
        cursor_pos = game_font.render(user_input[:cursor], True, "black").get_rect()
        cursor_rect = pygame.Rect(110 + cursor_pos[2], 660, 3, 40)

        #Draw the cursor blinking
        if cursor_blink_timer < 300:
            pygame.draw.rect(screen, "black", cursor_rect)
            cursor_blink_timer += 1
        elif cursor_blink_timer >= 300 and cursor_blink_timer < 600:
            pygame.draw.rect(screen, "lightgray", cursor_rect)
            cursor_blink_timer += 1
        else:
            cursor_blink_timer = 0
        
        #Update the state of the fire button
        fire_button.Update(screen)
        fire_button.ChangeColor(pygame.mouse.get_pos())

        #Load the level
        current_level = GetLevel(level)

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
                else:
                    inputting = False
                
                if fire_button.CheckForInput(event.pos) and (attempt == True):
                    fire = True

            #Code to track keyboard input
            if event.type == pygame.KEYDOWN:

                #Adjust the user input arcording to the keys pressed
                if inputting == True:
                    if event.key == pygame.K_BACKSPACE:
                        if cursor != 0:
                            user_input = user_input = user_input[:cursor-1] + user_input[cursor:]
                            cursor -= 1
                    elif event.key == pygame.K_LEFT:
                        if cursor != 0:
                            cursor -= 1
                    elif event.key == pygame.K_RIGHT:
                        if cursor != len(user_input):
                            cursor += 1
                    else:
                        if event.unicode:
                            user_input = user_input[:cursor] + event.unicode + user_input[cursor:]
                            cursor += 1

                #Display the pause if the user pressed the esc key
                if event.key == pygame.K_ESCAPE:
                    if pause_screen(screen, volume):
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
                incorrect_equation(screen, volume)

        #Animate the projectile
        if firing:
            projectile = pygame.Rect(-25, -25, 25, 25)
            projectile.center = (x[current_x], y[current_x])
            pygame.draw.rect(surface=screen, color="green", rect=projectile)
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
                restart = lose_screen(screen, volume)
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
                if win_screen(screen, volume):
                    pygame.mixer.music.stop()
                    #Reset the music
                    pygame.mixer.music.load("sounds\BitMenu.mp3")
                    pygame.mixer.music.set_volume(volume[0])
                    pygame.mixer.music.play(loops=-1, fade_ms=2500)
                    MainMenu(screen, base_font, difficulty, volume)
                else:
                    if int(level) == GetNumLevel():
                        congrats(screen, volume)
                        MainMenu(screen, game_font, difficulty, volume)
                    else:
                        MainGameLogic(str(int(level)+1), game_font, difficulty, volume)

        #Set the speed of the game
        clock.tick(360)

        #Update the screen
        pygame.display.update()


MainMenu(screen, base_font, Difficulty, Volume)