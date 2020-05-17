class DnD5e(chaacter): # D&D 5th edition
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
        # Saving Throws
        self.str_save = Proficiences("Strength", self.str)
        self.dex_save = Proficiences("Dexterity", self.dex)
        self.con_save = Proficiences("Constitution", self.con)
        self.int_save = Proficiences("Intelligence", self.int)
        self.wis_save = Proficiences("Wisdom", self.wis)
        self.cha_save = Proficiences("chaisma", self.cha)
        # skills
        self.acrobatics = Proficiences("Acrobatics", self.dex)
        self.animal_handling = Proficiences("Animal Handling", self.wis)
        self.arcana = Proficiences("Arcana", self.int)
        self.athletics = Proficiences("Athletics", self.str)
        self.deception = Proficiences("Deception", self.cha)
        self.history = Proficiences("History", self.int)
        self.insight = Proficiences("Insight", self.wis)
        self.intimidation = Proficiences("Intimidation", self.cha)
        self.investigation = Proficiences("Investigation", self.int)
        self.medicine = Proficiences("Medicine", self.wis)
        self.nature = Proficiences("Nature", self.int)
        self.perception =  Proficiences("Perception", self.wis)
        self.performance = Proficiences("Performance", self.cha)
        self.persuassion = Proficiences("Persuasion", self.cha)
        self.religion = Proficiences("Religion", self.wis)
        self.sleight_of_hand = Proficiences("Sleight of Hand", self.dex)
        self.stealth = Proficiences("Stealth", self.dex)
        self.survival = Proficiences("Survival", self.wis)
        self.passive_perception = 10 + self.wis
