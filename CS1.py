import pygame, sys
from button import Button
import numpy as np

#set up pygame
pygame.init()

#text render function
def RenderText(x, y, text, color, size):
    font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

#mathematical functions
def ln(x):
    return np.log(x) 

def log2(x):
    return np.log2(x)

def log10(x):
    return np.log10(x)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def sqrt(x):
    return np.sqrt(x)

def exp(x, a):
    return x ** a

#set up the display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

#clock/fps
clock = pygame.time.Clock()

#user input
user_input = ""
input_box = pygame.Rect(100, 650, 1020, 60)
active_input = False

#window border
top_rect = pygame.Rect(0, -1000000, 1280, 1000000)
bottom_rect = pygame.Rect(0, 640, 1280, 1000080)
left_rect = pygame.Rect(-1000000, 0, 1000000, 720)
right_rect = pygame.Rect(1280, 0, 1000000, 720)

#target
target = pygame.Rect(-50, -50, 25, 25)
target.center = (1100, 320)


fire_img = pygame.image.load("CS1\images\\pixilart-drawing.png")
fire_img = pygame.transform.scale(fire_img, (60, 60))
fire_button = Button(image=fire_img, 
                     x_pos=1200, y_pos=680, text_input="F")
fire = False
attepmt = True
fire_animation = False
fire_loop = 0




#main loop
while True:

    #win and fail variables
    fail = False
    win = False

    #background color
    screen.fill((202,228,241))

    #draw the window border
    pygame.draw.rect(screen, "white", top_rect)
    pygame.draw.rect(screen, "white", bottom_rect)
    pygame.draw.rect(screen, "white", left_rect)
    pygame.draw.rect(screen, "white", right_rect)

    #draw the target
    pygame.draw.rect(screen, "red", target)


    #event handler
    for event in pygame.event.get():


        #quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #track mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active_input = True
            else:
                active_input = False
            
            if fire_button.CheckForInput(event.pos) and (attepmt == True):
                fire = True

        #track keyboard input
        if event.type == pygame.KEYDOWN:
            if active_input == True:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

    #Check for fire input and initialize coordinates for the projectile
    if fire:
        fire = attempt = False
        fire_animation = True
        x = np.linspace(50, 1280, 1280)
        try:
            y = eval(user_input)+320
        except:
            attempt = True
            fire_animation = False

    #animating the projectile
    if fire_animation:
        projectile = pygame.Rect(-25, -25, 25, 25)
        projectile.center = (x[fire_loop], y[fire_loop])
        pygame.draw.rect(surface=screen, color="green", rect=projectile)
        fire_loop += 1
        if fire_loop > 1280:
            fail = True

        
        #collisions detection
        if projectile.colliderect(top_rect):
            fail = True
        elif projectile.colliderect(bottom_rect):
            fail = True
        elif projectile.colliderect(left_rect):
            fail = True
        elif projectile.colliderect(right_rect):
            fail = True

        if fail:
            fail_screen = pygame.Rect(100, 100, 500, 300)
            pygame.draw.rect(surface=screen, color="red", rect=fail_screen)

        if target.colliderect(projectile):
            win = True
        
        if win:
            win_screen = pygame.Rect(100, 100, 500, 300)
            pygame.draw.rect(surface=screen, color="green", rect=win_screen)


    #render text and text box
    if active_input:
        input_box_color = "green"
    else:
        input_box_color = "black"

    fire_button.Update(screen)
    fire_button.ChangeColor(pygame.mouse.get_pos())

    pygame.draw.rect(screen, input_box_color, input_box, 2)
    RenderText(input_box.x + 15, input_box.y + 5, user_input, "black", size=32)
    RenderText(input_box.x - 60, input_box.y + 5, "y =", "black", size=32)

    
    #set fps
    clock.tick(120)


    #update the screen
    pygame.display.update()

