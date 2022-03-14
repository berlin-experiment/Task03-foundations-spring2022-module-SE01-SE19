import random
import math


class Gladiator:
    """All fighter in the game share similiar attriubutes"""
    def __init__(self, name, hp, max_dmg):
        self.name = name
        self.hp = hp
        self.max_dmg = max_dmg

    def attack(self):
        """Calculate the HP remaining after an attack"""
        # Both player and opponent damage are dealt
        # The damage dealt should be a rand int between 1 and the max damage
        dmg = random.randint(1, self.max_dmg) 

        return dmg

    def defend(self):
        """Calculate the player HP remaining after an attack divided by 2"""
        # Only the damage dealt by the opponent is calucated (only player loses HPs)
        # The damage dealt should be a rand int between 1 and the max damage and then divided by 2
        dmg = random.randint(1, self.max_dmg) / 2
        if dmg < 1:
            dmg = 1
        else:
            dmg = int(math.ceil(dmg))

        return dmg
