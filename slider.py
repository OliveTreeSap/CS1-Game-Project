import pygame
from add_funcs import RenderText


pygame.init()


class Slider():

    
    #Initialize the slider and its properties
    def __init__(self, center, size, initial_val, min_val, max_val, label, label_font, value_font):
        self.center = center
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.label = label
        self.label_font = label_font
        self.value_font = value_font

        self.top_pos = self.center[1] - self.size[1]/2
        self.left_pos = self.center[0] - self.size[0]/2

        self.initial_val = self.size[0]*initial_val

        self.container_rect = pygame.Rect(self.left_pos, self.top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.left_pos + self.initial_val - 12.5, self.top_pos, 25, self.size[1])


    #Move the slider button
    def MoveSlider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]

    
    #Display the slider
    def UpdateSlider(self, screen):
        pygame.draw.rect(screen, "black", self.container_rect)
        pygame.draw.rect(screen, "lightgray", self.button_rect)


    #Get the value from the slider
    def GetValue(self):
        val_range = self.size[0] - 1
        button_val = self.button_rect.centerx - self.left_pos

        return (button_val/val_range)*(self.max_val-self.min_val)+self.min_val
    

    #Display the label of the slider
    def DisplayLabel(self, screen):
        RenderText(screen, self.container_rect.centerx, self.top_pos-35, self.label, "black", self.label_font, center=True)
    

    #Display the value next to the slider
    def DisplayValue(self, screen):
        RenderText(screen, self.left_pos + self.size[0] + 50, self.container_rect.centery, "{:.2f}".format(self.GetValue()), "black", self.value_font, center=True)