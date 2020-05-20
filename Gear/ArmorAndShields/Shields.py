class Shields:
    """Initialize basic attributes of shields"""
    def __init__(self):
        self.name = "" # name of item; example: Heater shield
        self.ac_bonus = 0
        self.weight = 0
        self.price = 0
        self.condition = "" # Broken, etc.
        self.check_penalty = 0 #applies to dex- and str-based skills
        self.arcane_failure_chance = 0 # percentage
        self.max_dex_modifer = 0
