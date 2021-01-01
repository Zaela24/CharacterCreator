class ImprovisedWeapons(Weapons):
    """Initializes values specifically associated with improvised weapons"""
    def __init__(self):
        self.throwable = False
        self.range = 0
        self.name = ""
        self.range = ""
        self.expertise = ""
        self.handling = ""
        self.size = ""
        self.damage_type = ""
        self.damage_dice = ""
        condition = ""
    def makeThrowable(self, range):
        """ Makes improvised weapons throwable with specified range increment"""
        self.throwable = True
        self.range = range

    def setDamage(self, damage):
        self.damage = damage  # inherited from Weapons class; wrote setter so we don't forget about it
