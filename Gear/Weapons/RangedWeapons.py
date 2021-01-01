# Extend Weapons.py
class RangedWeapons(Weapons):
    def __init__(self):
        """Initializes values specifically associated with ranged weapons"""
        self.range_increment = 0
        self.ammunition = 0
        self.name = ""
        self.price = 0
        self.expertise = ""
        self.handling = ""
        self.damage_type = ""
        self.damage_dice = ""
        self.size = ""
        self.condition = ""
