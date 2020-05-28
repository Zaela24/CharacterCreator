class ImprovisedWeapons(Weapons):
    """Initializes values specifically associated with improvised weapons"""
    def __init__(self):
        self.throwable = False
        self.range = 0

    def makeThrowable(self, range):
        """ Makes improvised weapons throwable with specified range increment"""
        self.throwable = True
        self.range = range
