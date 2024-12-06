import pygame

pygame.init()
base_font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", 32)


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = base_font.render(self.text_input, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def Update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def CheckForInput(self, position):
        if self.rect.collidepoint(position):
            print("button pressed")
            return True
    
    def ChangeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = base_font.render(self.text_input, True, "green")
        else:
            self.text = base_font.render(self.text_input, True, "black")