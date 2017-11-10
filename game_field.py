from PyQt5.Qt import *
from mobs_generator import MobsGenerator


class GameField(QWidget):

    def __init__(self, player, x, y, game_speed):
        super().__init__()

        oImage = QImage("src/space.jpg")
        sImage = oImage.scaled(QSize(800, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.player = player
        self.bullets = []

        self.mobs = []
        self.mobs_generator = MobsGenerator()
        self.mobs_generator_timer = 0

        self.init_ui(x, y)

        self.game_speed = game_speed
        self.timer = self.startTimer(self.game_speed)

    def init_ui(self, x, y):

        self.resize(x, y)
        self.setWindowTitle("TNTD")
        self.center()
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.player.x, self.player.y, self.player)

        for bullet in self.bullets:
            painter.drawPixmap(bullet.x, bullet.y, bullet)

        for mob in self.mobs:
            painter.drawPixmap(mob.x, mob.y, mob)

    def timerEvent(self, event):
        self.player.update()

        if self.player.shooting and self.player.reloading_time == 0:
            self.bullets.append(self.player.shot())

        for bullet in self.bullets:
            bullet.update()
            if bullet.need_to_delete:
                self.bullets.remove(bullet)

        if self.mobs_generator_timer == 0:
            self.mobs.extend(self.mobs_generator.generate_mobs())
            self.mobs_generator_timer = 500
        else:
            self.mobs_generator_timer -= 1

        for mob in self.mobs:
            mob.update()

        self.repaint()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Up:
            self.player.move_y(-1)
        elif event.key() == Qt.Key_Down:
            self.player.move_y(1)
        elif event.key() == Qt.Key_Left:
            self.player.move_x(-1)
        elif event.key() == Qt.Key_Right:
            self.player.move_x(1)

        if event.key() == Qt.Key_Space:
            self.player.start_shooting()

    def keyReleaseEvent(self, event):

        if event.key() == Qt.Key_Up:
            self.player.move_y(0)
        elif event.key() == Qt.Key_Down:
            self.player.move_y(0)
        elif event.key() == Qt.Key_Left:
            self.player.move_x(0)
        elif event.key() == Qt.Key_Right:
            self.player.move_x(0)

        if event.key() == Qt.Key_Space:
            self.player.stop_shooting()
