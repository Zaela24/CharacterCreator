class Race:
    """Parent Race class, which initializes general race attributes"""
    def __init__(self):
        self.race_name = ""
        self.ability_score_bonuses = dict()
        self.racial_traits = list()
        self.m_weight_range = tuple() # figure out how to populate later
        self.m_height_range = tuple() #   want tuples so that values aren't
        self.f_weight_range = tuple() #   accidentally changed elsewhere
        self.f_height_range = tuple()
        self.age_range = tuple() # In Pathfinder there are actually 3 age
                                 #  ranges for every race, depending on the PC's
                                 #  first class. Not sure how you want to handle
                                 #  that.
        # Not sure if we want to store alternate racial traits / sub-races here
