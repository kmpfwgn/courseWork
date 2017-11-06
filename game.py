from PyQt5.Qt import *
from game_field import GameField
from player import Player


class Game(QMainWindow):

    def __init__(self, WINDOW_X, WINDOW_Y):
        super().__init__()

        self.window_x = WINDOW_X
        self.window_y = WINDOW_Y