from objects import Object


level_1 = [Object(1130-12.5, 320-12.5, 25, 25, "red")]

level_2 = [Object(1130-12.5, 320-12.5, 25, 25, "red"),
           Object(640, 320-12.5, 25, 125, "black", moving=True,
                  speed_x=0, distance_x=0, speed_y=0.01, distance_y=250)]

level_3 = [Object(1130-12.5, 320-12.5, 25, 25, "red"),
           Object(590-25, 295, 25, 345, "black")]

level_4 = [Object(1130-12.5, 320-12.5, 25, 25, "red"),
           Object(300-25, 295, 25, 345, "black"),
           Object(900-25, 295, 25, 345, "black"),
           Object(600-25, 0, 25, 295, "black")]

level_5 = [Object(1130-12.5, 320-12.5, 25, 25, "red"),
           Object(300-25, 295, 25, 345, "black"),
           Object(900-25, 295, 25, 345, "black"),
           Object(600-25, 295, 25, 345, "black"),
           Object(450-25, 0, 25, 295, "black"),
           Object(750-25, 0, 25, 295, "black")]

level_6 = [Object(1130-12.5, 240-12.5, 25, 25, "red"),
           Object(600-25, 295, 25, 345, "black"),
           Object(540-25, 0, 25, 295, "black")]

levels = [level_1, level_2, level_3, level_4, level_5, level_6]


def GetLevel(level):
    return levels[int(level) - 1]

