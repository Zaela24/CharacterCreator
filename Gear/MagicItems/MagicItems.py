# NOT weapons, armor, or wondrous items
class MagicItems:
    def __init__(self):
        self.name = ""
        self.type = "" # wand, rod, scroll, potion, etc
        self.spell = None
        self.charges = 0
        self.price = 0
        self.crafting_requirements = ""

    def set_type(self, type, charges=1): # default 1 charge ; can be more if staff or wand
        self.type = type.lower()
        self.charges = charges

    # if using pathfinder 1e staves, put spells and charges in a list in the
    # corresponding order so that each index matches
