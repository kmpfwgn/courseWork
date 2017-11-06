from PyQt5.Qt import *
import sys
from game_field import GameField
from player import Player


def main():

    WINDOW_X = 800
    WINDOW_Y = 400

    app = QApplication(sys.argv)
    player = Player("src/player.jpg", WINDOW_X, WINDOW_Y)
    field = GameField(player, WINDOW_X, WINDOW_Y, 10)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
