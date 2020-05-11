class DnD5e(Character): # D&D 5th edition
    def __init__(self):
        self.ideals = dict()
        self.bonds = dict()
        self.flaws = dict()
        self.background = dict()
        self.passive_wis = 0
        self.allies_and_orgs = dict()
        self.spellcasting_ability = ""
        self.spell_save_dc = 0
        self.spell_attk_bonus = 0
        self.feats = dict()
        self.prof_bonus = 0
        self.attuned_items = dict()
