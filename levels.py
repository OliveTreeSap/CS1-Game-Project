import pygame
from objects import Object


pygame.init()

screen = pygame.display.set_mode((1280, 720))

#Load the image of the target and obstacles
boss = pygame.image.load("images/objects/boss.png").convert_alpha()
obstacle = pygame.image.load("images/objects/obstacle.png").convert_alpha()
obstacle_downward = pygame.image.load("images/objects/obstacle_down.png").convert_alpha()


level_1 = [Object(1130-12.5, 320-50, 150, 106, "red", image=boss)]

level_2 = [Object(1130-12.5, 320-50, 150, 106, "red", image=boss),
           Object(640, 320-12.5, 25, 125, "black", image=obstacle, moving=True,
                  speed_x=0, distance_x=0, speed_y=0.01, distance_y=250)]

level_3 = [Object(1130-12.5, 320-50, 150, 106, "red", image=boss),
           Object(590-25, 295, 25, 345, "black", image=obstacle)]

level_4 = [Object(1130-12.5, 320-50, 150, 106, "red", image=boss),
           Object(300-25, 295, 25, 345, "black", image=obstacle),
           Object(900-25, 295, 25, 345, "black", image=obstacle),
           Object(600-25, 0, 25, 295, "black", image=obstacle_downward)]

level_5 = [Object(1130-12.5, 320-50, 150, 106, "red", image=boss),
           Object(300-25, 295, 25, 345, "black", image=obstacle),
           Object(900-25, 295, 25, 345, "black", image=obstacle),
           Object(600-25, 295, 25, 345, "black", image=obstacle),
           Object(450-25, 0, 25, 295, "black", image=obstacle_downward),
           Object(750-25, 0, 25, 295, "black", image=obstacle_downward)]

level_6 = [Object(1130-12.5, 240-50, 150, 106, "red", image=boss),
           Object(600-25, 295, 25, 345, "black", image=obstacle),
           Object(540-25, 0, 25, 295, "black", image=obstacle_downward)]

levels = [level_1, level_2, level_3, level_4, level_5, level_6]


def GetNumLevel():
    return len(levels)


#Return the requested level
def GetLevel(level):
    return levels[int(level) - 1]

