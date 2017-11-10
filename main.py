from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import sys
from game_field import GameField
from player import Player
from weapon.bullet import Bullet
from mobs import *


def main():

    WINDOW_X = 800
    WINDOW_Y = 400

    app = QApplication(sys.argv)
    player = Player("src/spaceship.png", WINDOW_X, WINDOW_Y)
    Bullet.PICTURE = QPixmap("src/bullet.png")
    test_mob.TestMob.PICTURE = QPixmap("src/test_mob.png")
    field = GameField(player, WINDOW_X, WINDOW_Y, 10)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
