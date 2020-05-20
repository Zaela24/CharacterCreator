class Kits:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.weight = 0
        self.contents = list()

class Tools:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.quality = "" # Common, Masterwork, sometimes Concealable
        self.adjustment = "" # describes circumstance bonuses, etc
        ## may want to think of way to autoadd these to Character based on description
