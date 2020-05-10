# Extend Weapons.py
class RangedWeapons(Weapons):
    def __init__(self):
        """Initializes values specifically associated with ranged weapons"""
        self.range_increment = 0
        self.ammunition = 0
