from mobs import *


class MobsGenerator:
    def __init__(self):
        self.mobs = dict()

    def generate_mobs(self):
        mobs = []

        for i in range(5):
            new_mob = test_mob.TestMob(800 + i * test_mob.TestMob.PICTURE.width() + i*30,
                                       200,
                                       i * 0.7)
            mobs.append(new_mob)

        return mobs
