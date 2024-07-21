from abc import ABC, abstractmethod
from random import randint
from typing import Callable

from dice import die


class Character:
    def __init__(
            self, name, health, attack, defense,
            attack_strategy):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attack_strategy = attack_strategy
        self.resistence = {
            'poison': 0,
            'fire': 0,
            'cold': 0
        }
        self.status = {
            'poison': 0,
            'fire': 0,
            'cold': 0
        }


    def get_stats(self):
        return f"Character: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense} \n"

    def get_attack(self):
        return self.attack 

    def get_defense(self):
        return self.defense 
    
    def get_resistence(self, type):
        base_resistance = self.resistence[type]
        armor_resistance = self.armor.get_resistance(type) if self.armor else 0
        seord_resistance = self.sword.get_resistance(type) if self.sword else 0

        return base_resistance + armor_resistance + seord_resistance

    def attack_action(self, character):
        print(type(self.attack_strategy))
        self.attack_strategy(character, self.attack)


AttackFn = Callable[[Character, int], None]


def poison_dart(character: Character, attack_bonus):
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        character.health -= die(4)
        character.status['poison'] = 2


def bite(character: Character, attack_bonus):
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        character.health -= die(6)


