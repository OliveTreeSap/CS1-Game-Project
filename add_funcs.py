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
def RenderText(screen, x, y, text, color, font, center=False):
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    else:
        screen.blit(text_surface, (x, y))

