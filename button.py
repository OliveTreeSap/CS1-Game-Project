import pygame
import numpy as np


pygame.init()
#Load the font
base_font = pygame.font.Font("Grand9K_Pixel.ttf", 32)


class Button():


    #Initialize the button class and its properties
    def __init__(self, image, x_pos, y_pos, text_input, volume, switch=False, state=False, alt_image=None):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = base_font.render(self.text_input, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        self.volume = volume
        self.sfx_1 = pygame.mixer.Sound("sounds/beep_1.wav")
        self.sfx_2 = pygame.mixer.Sound("sounds/beep_2.wav")
        self.sfx_3 = pygame.mixer.Sound("sounds/beep_3.wav")
        for sfx in [self.sfx_1, self.sfx_2, self.sfx_3]:
            pygame.mixer.Sound.set_volume(sfx, self.volume)

        self.switch = switch

        if self.switch:
            self.state = state
            self.alt_image = alt_image
            self.alt_rect = self.alt_image.get_rect(center=(self.x_pos, self.y_pos))


    def Update(self, screen):
        #Update the button visually
        if self.switch:
            if self.state:
                screen.blit(self.image, self.rect)
                screen.blit(self.text, self.text_rect)
            else:
                screen.blit(self.alt_image, self.alt_rect)
                screen.blit(self.text, self.text_rect)
        else:
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)


    def CheckForInput(self, position):
        #Check if the button was clicked
        if self.rect.collidepoint(position):
            [self.sfx_1, self.sfx_2, self.sfx_3][np.random.randint(0,3)].play()
            #Change the state of the button (on/off)
            if self.switch:
                self.state = not self.state
            return True


    def ChangeColor(self, position):
        #Change the color of the text when the cursor hovers over the button
        if self.rect.collidepoint(position):
            self.text = base_font.render(self.text_input, True, "green")
        else:
            self.text = base_font.render(self.text_input, True, "black")

