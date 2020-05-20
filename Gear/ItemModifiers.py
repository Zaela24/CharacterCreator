# To store multiple functions for special materials, magic weapons/armor
#   weapon/armor special abilities, masterwork items, etc.

from ArmorAndShields import Armor, Shields
from Weapons import Weapons

def masterwork(equipment): # only for 1e Pathfinder
    if isinstance(equipment, Armor.Armor) or isinstance(equipment, Shields.Shields):
        if equipment.masterwork == False:
            if equipment.check_penalty < 0:
                equipment.check_penalty =+ 1 # reduce check penalty by 1
            equipment.price += 150 # add 150 gp to cost
            equipment.masterwork = True

    elif isinstance(equipment, Weapons.Weapons):
        if equipment.masterwork == False:
            equipment.attack_bonus += 1
            equipment.price += 300
            if "double" in equipment.special_qualities:
                equipment.price += 300 # doubles price inc. to 600 total
            equipment.masterwork = True
