# General / abstract class
class Weapons:
    """Initializes general Weapon attributes across games and weapon types"""
    def __init__(self):
        self.name = "" # item name, example: Dagger
        self.price = 0 # assuming in gold pieces
        self.expertise_category = "" # Simple, Martial, Exotic
        self.handling = "" # Light, One-Handed, Two-Handed
        self.damage = "" # example, 1d6
        self.damage_type = "" # Bludgeoning, Piercing, Slashing
        self.condition = "" # Broken, etc
        self.size_category = "M" # Small, Medium, Light ; usually Medium
        self.crit_threat = 20 # usually 20 unless otherwise specified
        self.crit_modifer = 2 # usually x2 on a crit hit unless otherwise noted
        self.attack_bonus = 0 # only modified for Masterwork and Magic weapons
