from PyQt5.Qt import *


class Player(QPixmap):

    def __init__(self, picture_path, x, y):
        super().__init__(picture_path)

        self.x = x + 5
        self.y = y / 2

        self.x_speed = 0
        self.y_speed = 0

        self.speed_coef = 5

    def move(self, x_boost, y_boost):

        if x_boost == 0:
            self.x_speed -= 1
            if self.x_speed < 0:
                self.x_speed = 0
        else:
            self.x_speed += x_boost

        if y_boost == 0:
            self.y_speed -= 1
            if self.y_speed < 0:
                self.y_speed = 0
        else:
            self.y_speed += y_boost

        self.x += self.x_speed
        self.y += self.y_speed

