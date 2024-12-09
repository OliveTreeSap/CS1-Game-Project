import numpy as np
import pygame


#Math functions
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


#text render function
def RenderText(screen, x, y, text, color, size, center=False):
    if center:
        font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    else:
        font = pygame.font.Font("CS1\Grand9K_Pixel.ttf", size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

