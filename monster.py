from abc import ABC, abstractmethod
from random import randint
from Character import Character
from dice import die

class Monster(ABC):
    def __init__(
            self, name, health, attack, defense,
            attack_strategy,):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attack_strategy = attack_strategy

    def get_stats(self):
        return f"Character: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def get_attack(self):
        return self.attack 

    def get_defense(self):
        return self.defense

    def attack_action(self, ac):
        print(type(self.attack_strategy))
        return self.get_attack()*self.attack_strategy.execute(self.attack, ac=ac)

def PoisonDart(character: Character):
    character.health -= die(4)
    character.status['poison'] = 2
