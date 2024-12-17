import pygame
import numpy as np


#Set up pygame
pygame.init()


class Object():
    

    #Initialize the obstacle or target and its properties
    def __init__(self, x, y, width, height, color, image, moving=False, speed_x=None, distance_x=None, speed_y=None, distance_y=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.moving = moving
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.moving:
            self.loop = 0
            self.speed_x = speed_x
            self.distance_x = distance_x
            self.speed_y = speed_y
            self.distance_y = distance_y


    #Update the obstacle visually
    def UpdateObject(self, screen):
        #If the moving is True then update the coordinates
        #and set x, y to be the center of the rectangle
        if self.moving:
            self.new_x = self.distance_x*np.sin(self.speed_x*self.loop) + self.x
            self.new_y = self.distance_y*np.sin(self.speed_y*self.loop) + self.y
            self.rect = pygame.Rect(self.new_x, self.new_y, self.width, self.height)
            self.rect.center = (self.new_x, self.new_y)
            # pygame.draw.rect(screen, self.color, self.rect)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            image_rect = self.image.get_rect()
            image_rect.center = (self.new_x, self.new_y)
            screen.blit(self.image, image_rect)
            self.loop += 1
        else:
            # pygame.draw.rect(screen, self.color, self.rect)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            image_rect = self.image.get_rect()
            image_rect.x, image_rect.y = self.x, self.y
            screen.blit(self.image, image_rect)


    #Check if the projectile have collided with the obstacle
    def CheckColision(self, projectile):
        if self.rect.colliderect(projectile):
            return True
        
        