from PyQt5.Qt import *


class GameField(QWidget):

    def __init__(self, player, x, y):
        super().__init__()
        self.player = player

        self.init_ui(x, y)
        self.start()

    def start(self):
        pass

    def init_ui(self, x, y):

        self.resize(x, y)
        self.setWindowTitle("TNTD")
        self.center()
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.player.x, self.player.y, self.player)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Up:
            self.player.move(0, -1)
        elif event.key() == Qt.Key_Down:
            self.player.move(0, 1)
        elif event.key() == Qt.Key_Left:
            self.player.move(-1, -0)
        elif event.key() == Qt.Key_Right:
            self.player.move(1, 0)

        self.repaint()
