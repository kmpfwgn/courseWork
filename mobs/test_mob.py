from PyQt5.QtGui import QPixmap
from math import sin


class TestMob(QPixmap):

    SPEED = 1
    PICTURE = 0

    def __init__(self, x, y, t):
        super().__init__(TestMob.PICTURE)

        self.x = x
        self.start_y = y
        self.y = y
        self.t = t

        self.need_to_delete = False

    def update(self):
        self.x -= TestMob.SPEED

        self.t += 0.05
        self.y = self.start_y + sin(self.t) * 30
