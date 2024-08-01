from abc import ABC, ABCMeta, abstractmethod
from random import randint
from Character import *
from Equipment import *

class Player(Character, metaclass=ABCMeta):
    def __init__(
            self, name, health, attack, defense,
            attack_strategy, dextirity, wisdom, charisma):
        super().__init__(name, health, attack, defense,
                       attack_strategy)
        self.dextirity = dextirity
        self.wisdom = wisdom
        self.charisma = charisma

class Fighter(Player):
    def __init__(self, name):
        self.sword = Sword()
        super().__init__(name, 25, 5, 5,
                         self.sword.sword_attack, 1, 0, 1)
        self.armor = Armor()
        
    def update_sword(self, sword):
        self.sword = sword
        self.attack_strategy = sword.sword_attack

    def update_armor(self, armor):
        self.armor = armor

    def __name__():
        return "Fighter"
        

