import sys
import pygame
from button import Button
from add_funcs import RenderText


#Set up pygame
pygame.init()


def lose_screen(screen, volume, font):

    run = True
    #Return if the user want to restart or not
    restart = False

    #Set up the lose screen
    lose_screen = pygame.Rect(-1000, -1000, 640, 360)
    lose_screen.center = (640, 360)

    #Set up the restart and quit button
    restart_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640-25, y_pos=360, text_input="R", font=font[2], volume=volume[1])
    quit_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640+25, y_pos=360, text_input="Q", font=font[2], volume=volume[1])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        #Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the restart or quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.CheckForInput(mouse_pos):
                    restart = True
                    run = False
                elif quit_button.CheckForInput(mouse_pos):
                    restart = False
                    run = False

        #Display the lose screen
        pygame.draw.rect(surface=screen, color="red", rect=lose_screen)
        
        #Update the restart and quit button
        for button in [restart_button, quit_button]:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Update the screen
        pygame.display.update()

    return restart


def win_screen(screen, volume, font):
    
    run = True

    #Set up the win screen
    win_screen = pygame.Rect(-1000, -1000, 768, 432)
    win_screen.center = (640, 360)

    #Set up the return to main menu  and continue to next level buttons
    home_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=400, text_input="Main menu", font=font[2], volume=volume[1])

    continue_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=320, text_input="Next level", font=font[2], volume=volume[1])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        #Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the home
            if event.type == pygame.MOUSEBUTTONDOWN:
                if home_button.CheckForInput(mouse_pos):
                    home = True
                    run = False

                if continue_button.CheckForInput(mouse_pos):
                    home = False
                    run = False

        #Display the win screen
        pygame.draw.rect(surface=screen, color="lightgreen", rect=win_screen)
        
        #Update the buttons
        for button in [home_button, continue_button]:
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Update the screen
        pygame.display.update()

    return home


def incorrect_equation(screen, volume, font):

    run = True

    #Set up the correction screen
    incorrect_equation = pygame.Rect(-1000, -1000, 768, 432)
    incorrect_equation.center = (640, 360)

    #Set up the ok button
    ok_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=360+25, text_input="K", font=font[2], volume=volume[1])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        #Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the home
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.CheckForInput(mouse_pos):
                    run = False

        #Display the correction screen
        pygame.draw.rect(surface=screen, color="white", rect=incorrect_equation)
        
        #Update the ok button
        ok_button.ChangeColor(mouse_pos)
        ok_button.Update(screen)

        #Display text warning the user
        RenderText(screen, 640, 360-50, "You inputted an incorrect equation", "Black", font=font[2], center=True)

        #Update the screen
        pygame.display.update()


def pause_screen(screen, volume, font):

    run = True
    #Return the user actions
    resume = False

    #Set up the pause screen
    pause_screen = pygame.Rect(-1000, -1000, 768, 432)
    pause_screen.center = (640, 360)

    #Set up the resume and quit button
    resume_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640-25, y_pos=360, text_input="R", font=font[2], volume=volume[1])
    quit_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640+25, y_pos=360, text_input="Q", font=font[2], volume=volume[1])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        #Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the resume or quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.CheckForInput(mouse_pos):
                    resume = True
                    run = False
                elif quit_button.CheckForInput(mouse_pos):
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
            button.ChangeColor(mouse_pos)
            button.Update(screen)

        #Update the screen
        pygame.display.update()

    return resume


def congrats(screen, volume, font):

    run = True

    #Set up the correction screen
    congrats = pygame.Rect(-1000, -1000, 768, 432)
    congrats.center = (640, 360)

    #Set up the ok button
    ok_button = Button(image=pygame.image.load("images\\pixilart-drawing.png"), x_pos=640, y_pos=360+25, text_input="Ok", font=font[2], volume=volume[1])

    #blur the background
    blur = pygame.image.load("images\\transparent_background.png").convert_alpha()
    screen.blit(blur, (0, 0))

    while run:

        #Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check if the user clicked the home
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.CheckForInput(mouse_pos):
                    run = False

        #Display the correction screen
        pygame.draw.rect(surface=screen, color="lightyellow", rect=congrats)
        
        #Update the ok button
        ok_button.ChangeColor(mouse_pos)
        ok_button.Update(screen)

        #Display text warning the user
        RenderText(screen, 640, 360-50, "Congratulations, you've beaten the game!", "Black", font=font[2], center=True)

        #Update the screen
        pygame.display.update()


def tutorial(screen, volume, font):

    run = True

    #Set up the tutorial background
    win_screen = pygame.Rect(-1280, -720, 1280, 720)
    win_screen.center = (640, 360)

    #Current y position
    y = 25

    while run:

        #Initialize the back button
        back_button = Button(image=pygame.image.load("images\\pixilart-drawing.png").convert(), x_pos=620, y_pos=-y+1350, text_input="Back", font=font[2], volume=volume[1])

        #Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        #Display the tutorial background
        pygame.draw.rect(screen, "#FEF5E2", win_screen)

        #Draw the container for the scroll wheel
        container = pygame.Rect(1260, 0, 20, 1280)
        pygame.draw.rect(screen, "black", container)

        #Draw the scroll wheel button
        scroll_wheel = pygame.Rect(1260, y, 20, 50)
        scroll_wheel.centery = y
        pygame.draw.rect(screen, "lightgray", scroll_wheel)

        #Display the back button
        back_button.ChangeColor(mouse_pos)
        back_button.Update(screen)

        #Render the tutorial text
        RenderText(screen, 620, -y+50, "Basic syntax", "#964B00", font=font[0], center=True)
        RenderText(screen, 700, -y+100, "Logarithmic Functions:",  "#A4550A", font=font[1])
        RenderText(screen, 700, -y+150, "ln(x): natual logarithm", "#4DE64D", font=font[2])
        RenderText(screen, 700, -y+200, "log2(x): base 2 logarithm", "#40D940", font=font[2])
        RenderText(screen, 700, -y+250, "log10(x): base 10 logarithm", "#33CC33", font=font[2])
        RenderText(screen, 700, -y+300, "Trigonometric Functions:",  "#A4550A", font=font[1])
        RenderText(screen, 700, -y+350, "sin(x): sine", "#4AE34A", font=font[2])
        RenderText(screen, 700, -y+400, "cos(x): cosine", "#60F960", font=font[2])
        RenderText(screen, 700, -y+450, "tan(x): tangent", "#30C930", font=font[2])
        RenderText(screen, 200, -y+100, "Operators:",  "#A4550A", font=font[1])
        RenderText(screen, 200, -y+150, "+: plus", "#4DE64D", font=font[2])
        RenderText(screen, 200, -y+200, "-: minus", "#40D940", font=font[2])
        RenderText(screen, 200, -y+250, "*: multiply", "#33CC33", font=font[2])
        RenderText(screen, 200, -y+300, "/: divide", "#4AE34A", font=font[2])
        RenderText(screen, 200, -y+350, "Other Functions:",  "#A4550A", font=font[1])
        RenderText(screen, 200, -y+400, "abs(x): absolute value", "#60F960", font=font[2])
        RenderText(screen, 200, -y+450, "sqrt(x): square root", "#30C930", font=font[2])
        RenderText(screen, 200, -y+500, "exp(x, a): exponent", "#009900", font=font[2])

        RenderText(screen, 620, -y+600, "Moving the graph", "#964B00", font=font[0], center=True)
        RenderText(screen, 620, -y+650, "Vertical and Horizontal Shifts:",  "#A4550A", font=font[1], center=True)
        RenderText(screen, 620, -y+700, "f(x) + c: shift the graph c pixels upward", "#66FF66", font=font[2], center=True)
        RenderText(screen, 620, -y+750, "f(x) - c: shift the graph c pixels downward", "#60F960", font=font[2], center=True)
        RenderText(screen, 620, -y+800, "f(x + c): shift the graph c pixels to the left", "#5AF35A", font=font[2], center=True)
        RenderText(screen, 620, -y+850, "f(x - c): shift the graph c pixels to the right", "#4DE64D", font=font[2], center=True)
        RenderText(screen, 620, -y+900, "Vertical and Horizontal Stretching and Reflecting:",  "#A4550A", font=font[1], center=True)
        RenderText(screen, 620, -y+950, "c*f(x): stretch the graph vertically by a factor of c", "#40D940", font=font[2], center=True)
        RenderText(screen, 620, -y+1000, "(1/c)*f(x): shrink the graph vertically by a factor of c", "#33CC33", font=font[2], center=True)
        RenderText(screen, 620, -y+1050, "f(c*x): shrink the graph horizontally by a factor of c", "#4AE34A", font=font[2], center=True)
        RenderText(screen, 620, -y+1100, "f(x/c): stretch the graph horizontally by a factor of c", "#60F960", font=font[2], center=True)
        RenderText(screen, 620, -y+1150, "-1*f(x): reflect the graph about the x-axis", "#30C930", font=font[2], center=True)
        RenderText(screen, 620, -y+1200, "f(-1*x): reflect the graph about the y-axis", "#009900", font=font[2], center=True)
        RenderText(screen, 620, -y+1250, "Remember to use brackets () to separate parts of the equation so they don't get mixed up", "#A4550A", font=font[4], center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check for mouse scroll wheel input
            if event.type == pygame.MOUSEWHEEL:
                y += -(event.y*20)
                if y < 25:
                    y = 25
                elif y > 695:
                    y = 695

            #Check for mouse input
            if event.type  == pygame.MOUSEBUTTONDOWN:
                #Check if the back button was clicked
                if back_button.CheckForInput(mouse_pos):
                    run = False
                
        #Check if the scroll wheel container was clicked
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if container.collidepoint(mouse_pos):
                y = mouse_pos[1]
                if y < 25:
                    y = 25
                elif y > 695:
                    y = 695
                scroll_wheel.centery = y
                
        #Update the screen
        pygame.display.update()

    return 