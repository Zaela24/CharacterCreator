# Extend Weapons.py
class MeleeWeapons(Weapons):
    """Initializes values specifically associated with melee weapons"""
    def __init__(self):
        self.throwable = False
        self.range = 0

    def makeThrowable(self, range):
        """Makes weapons throwable with specified range increment"""
        self.throwable = True
        self.range = range
