class Spells:
    """Initializes general spell attributes"""
    def __init__(self):
        self.spell_level = 0
        self.schools = list()
        self.spell_list = dict() # key=CharacterClass, value=ClassLevel
        self.spell_resist = True # defaults to allow spell resist
        self.duration = None # instantaneous, numer of rounds, permanent*, etc
        self.casting_time = None # standard action, full round action, etc
        self.effects = None
        self.range = "" # close, medium, far; has value based on caster level
        self.num_targets = 0
