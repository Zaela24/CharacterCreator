# Extend Weapons.py
class MeleeWeapons(Weapons):
    """Initializes values specifically associated with melee weapons"""
    def __init__(self):
        self.name = ""
        self.throwable = False
        self.range = 0
        self.price = 0
        self.expertise = ""
        self.handling = ""
        self.size = ""
        self.damage_type = ""
        self.damage_dice = ""
        self.condition = ""

    def makeThrowable(self, range):
        """Makes weapons throwable with specified range increment"""
        self.throwable = True
        self.range = range
