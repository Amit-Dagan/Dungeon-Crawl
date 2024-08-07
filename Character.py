from abc import ABC, abstractmethod
from random import randint
from typing import Callable

from dice import die


class Character:
    def __init__(
            self, name, health, attack, defense,
            attack_strategy, xp):
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
        self.xp = xp


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

    def attack_action(self, character) -> str:
        text = (f"{self.name} attack!") + '\n '
        text += self.attack_strategy(character=character, attack_bonus=self.attack)
        return text

AttackFn = Callable[[Character, int], None]


def poison_dart(character: Character, attack_bonus):
    text = f"He uses Poison Dart on {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"It secceeds!\n "
        dmg = die(4)
        text += f"{character.name} health = {
              character.health} - {dmg} = {character.health - dmg}\n "

        character.health -= dmg
        text += f"{character.name} is poisend!\n "
        character.status['poison'] = 2
    else:
        text += "It dose not secceeds!\n "
    return text

def bite(character: Character, attack_bonus):
    text = (f"He uses Bite on {character.name}\n ")
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += (f"It secceeds!\n ")
        dmg = die(6)
        text += (f"{character.name} health = {
              character.health} - {dmg} = {character.health - dmg}\n ")

        character.health -= dmg
    else:
        text += ("It dose not secceeds!\n ")
    return text


