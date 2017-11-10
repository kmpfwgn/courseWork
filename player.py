from PyQt5.QtGui import *
from weapon.bullet import Bullet


class Player(QPixmap):

    SPEED = 4
    RELOADING = 30
    WEAPON = {1: "Bullet", 2: "Rocket"}

    def __init__(self, picture_path, x, y):
        super().__init__(picture_path)

        self.WINDOW_X = x
        self.WINDOW_Y = y

        self.x = 5
        self.y = (y / 2) - (self.height() / 2)

        self.x_speed = 0
        self.y_speed = 0

        self.shooting = False
        self.current_weapon = 1
        self.reloading_time = 0

    def move_x(self, boost):

        self.x_speed = boost * Player.SPEED
        self.y_speed = 0

    def move_y(self, boost):

        self.y_speed = boost * Player.SPEED
        self.x_speed = 0

    def update(self):

        self.x += self.x_speed
        self.y += self.y_speed

        if self.reloading_time > 0:
            self.reloading_time -= 1

        if self.y < 0:
            self.y = 0
        elif self.y > (self.WINDOW_Y - self.height()):
            self.y = self.WINDOW_Y - self.height()

        if self.x < 0:
            self.x = 0
        elif self.x > (self.WINDOW_X / 2):
            self.x = self.WINDOW_X / 2

    def start_shooting(self):
        self.shooting = True

    def stop_shooting(self):
        self.shooting = False

    def shot(self):
        self.reloading_time += Player.RELOADING

        x = str(self.x + self.width())
        y = str(self.y + self.height()/2)
        new_shot = Player.WEAPON[self.current_weapon] + "(" + x + "," + y + ")"
        return eval(new_shot)





