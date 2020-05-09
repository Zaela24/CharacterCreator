class Proficiences:
    """ A constructor for basic proficiencies"""
    def __init__(self, name, ability_mod):
        """
        args:
            name (str) - the name of the proficency
            ability_mod (int) - the relevant ability score modifier for the proficiency
        returns:
            A proficiencies object with the given name
        """
        self.name = name
        self.proficient = False # Initial
        self.ability_mod = ability_mod
        self.temp_mod = 0 # any temporary modifiers that may effect the proficiency
        self.misc_mod = 0 # any miscelaneous modifiers that may effect the proficiency
        
