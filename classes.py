# CLASSES

# Player has-a Force
class Player(object):

    def __init__(self):
        self.force = Force()

class Force(object):

    def __init__(self, level):
        self.level = level

class Scene(object):
    pass

class WeaponRoom(Scene):

    def enter(self):
        pass

class ArenaIntro(Scene):

    def enter(self):
        pass

class FirstMonster(Scene):

    def enter(self):
        pass

class SecondMonster(Scene):

    def enter(self):
        pass

class ArenaMaster(Scene):

    def enter(self):
        pass
