class PathfinderCharacter(Character): # 1e Pathfinder
    def __init__(self):
        self.advancement_track = "" # Fast, Medium, or Slow exp track
        self.feats = dict()
        self.traits = dict()
        self.will = 0
        self.ref = 0
        self.fort = 0
        self.dr = 0
        self.sr = 0
        self.resistences = dict()
        self.spell_dc = dict()
        self.inventory = None # make inventory class to store items / gear
        self.armor = None
        self.shield = None
        self.weapons = list() # list of weapon objects
        self.cmb = 0
        self.cmd = 0
        self.touch_ac = 10
        self.flatfoot_ac = 10
        self.skills = list([]) # create matrix w/ ranks, class bonuses, etc

## Will only work on 1e Pathfinder for the time being
# class Pathfinder2Character(PathfinderCharacter): # 2e Pathfinder
#     def __init__(self):
#         self.ancestry = None
#         self.background = None
#         self.hero_points = 0
#         self.bulk = 0
