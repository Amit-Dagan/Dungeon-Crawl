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
        print(f"{self.name} attack!")
        self.attack_strategy(character=character, attack_bonus=self.attack)


AttackFn = Callable[[Character, int], None]


def poison_dart(character: Character, attack_bonus):
    print(f"He uses Poison Dart on {character.name}")
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        print(f"It secceeds!")
        dmg = die(4)
        print(f"{character.name} health = {
              character.health} - {dmg} = {character.health - dmg}")

        character.health -= dmg
        print(f"{character.name} is poisend!")
        character.status['poison'] = 2
    else:
        print("It dose not secceeds!")

def bite(character: Character, attack_bonus):
    print(f"He uses Bite on {character.name}")
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        print(f"It secceeds!")
        dmg = die(6)
        print(f"{character.name} health = {
              character.health} - {dmg} = {character.health - dmg}")

        character.health -= dmg
    else:
        print("It dose not secceeds!")


