from abc import ABC, ABCMeta, abstractmethod
from random import randint
from Character import *
from Equipment import Sword, Armor

class Player(Character, metaclass=ABCMeta):
    def __init__(
            self, name, health, attack, defense,
            attack_strategy):
        super().__init__(name, health, attack, defense,
                       attack_strategy)

class Fighter(Player):
    def __init__(self, name):
        super().__init__(name, 25, 5, 5,
                       Sword.sword_attack)
        self.armor = Armor()
        self.sword = Sword()
        
    def update_sword(self, sword):
        self.sword = sword

    def update_armor(self, armor):
        self.armor = armor


