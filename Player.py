from abc import ABC, ABCMeta, abstractmethod
from random import randint
from Character import *


class Player(Character, metaclass=ABCMeta):
    def __init__(
            self, name, health, attack, defense, armor, sword,
            attack_strategy, defense_strategy):
        super.__init__(self, name, health, attack, defense,
                       attack_strategy)
        self.armor = armor
        self.sword = sword
        
    def update_sword(self, sword):
        self.sword = sword

    def update_armor(self, armor):
        self.armor = armor


    def get_attack(self):
        return self.attack + self.sword.get_attack() + self.armor.get_attack()

    def get_defense(self):
        return self.defense + self.sword.get_defense() + self.armor.get_defense()
