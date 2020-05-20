class Armor:
    """Initializes basic attributes of Armor"""
    def __init__(self):
        self.name = "" # name of item; example: Leather Armor
        self.masterwork = False # can move to Pathfinder exclusive armor if needed
        self.ac_bonus = 0
        self.weight = 0
        self.price = 0
        self.category = "" # Light, Medium, Heavy
        self.condition = "" # Broken, etc
        self.check_penalty = 0 # 0 or neg; applies to dex- and str-based skills
        self.arcane_failure_chance = 0 # percentage
        self.max_dex_modifer = 0
