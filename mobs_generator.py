from PyQt5.QtGui import QPixmap


class MobsGenerator:

    def __init__(self):

        self.mobs = dict()

        self.load_mobs()

    def load_mobs(self):

        self.mobs = {"test_mob1": QPixmap("src/test_mob1.jpg"),
                     "test_mob2": QPixmap("src/test_mob2.jpg")}
