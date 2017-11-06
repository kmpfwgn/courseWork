from PyQt5.Qt import *


class Player(QPixmap):

    def __init__(self, picture_path, x, y):
        super().__init__(picture_path)

        self.WINDOW_X = x
        self.WINDOW_Y = y

        self.x = 5
        self.y = (y / 2) - (self.height() / 2)

        self.x_speed = 0
        self.y_speed = 0

        self.speed_coef = 4

        self.shooting_speed = 500
        self.shooting_time = 0
        self.shooting_times = 0
        self.t = False

    def move(self, x_boost, y_boost):

        self.x_speed = x_boost * self.speed_coef
        self.y_speed = y_boost * self.speed_coef

    def update(self):

        self.x += self.x_speed
        self.y += self.y_speed

        if self.y < 0:
            self.y = 0
        elif self.y > (self.WINDOW_Y - self.height()):
            self.y = self.WINDOW_Y - self.height()

        if self.x < 0:
            self.x = 0
        elif self.x > (self.WINDOW_X / 2):
            self.x = self.WINDOW_X / 2

        if self.t:
            if self.shooting_speed == self.shooting_time:
                self.shooting_time = 0
                if self.shooting_times != 0:
                    self.shot()
                    self.shooting_times -= 1
                if self.shooting_times == 0:
                    self.shooting_times = 0
                    self.t = False

            self.shooting_time += 10

    def shot(self):
        print(1)

    def start_stop_shooting(self, value):
        # if value:
        #     self.shooting_times += 1
        #     self.t = True
        #

        if value:
            print(1)
        else:
            print(2)


