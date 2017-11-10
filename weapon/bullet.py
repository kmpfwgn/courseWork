from PyQt5.QtGui import QPixmap


class Bullet(QPixmap):

    SPEED = 6
    WINDOW_X = 800
    PICTURE = 0

    def __init__(self, x, y):
        super().__init__(Bullet.PICTURE)

        self.x = x
        self.y = y

        self.need_to_delete = False

    def update(self):
        self.x += Bullet.SPEED

        if self.x > 800:
            self.need_to_delete = True

    def is_need_to_delete(self):
        return self.need_to_delete
