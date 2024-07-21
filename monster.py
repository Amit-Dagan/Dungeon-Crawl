from abc import ABC, ABCMeta, abstractmethod
from random import randint
from typing import Callable
from Character import *
from dice import die


class Monster(Character, metaclass=ABCMeta):
    def __init__(self, name, health, attack, defense, attack_strategy: AttackFn):
        super().__init__(name, health, attack, defense,attack_strategy)


class Goblin(Monster):
    def __init__(self):
        super().__init__(
            name= "Rat", health=5, attack=5, 
            defense=5, attack_strategy= poison_dart)


class Rat(Monster):
    def __init__(self):
        super().__init__(
            name="Rats", health=5, attack=5,
            defense=3, attack_strategy=bite)


class Bat(Monster):
    def __init__(self):
        super().__init__(
            name="Bats", health=5, attack=3,
            defense=5, attack_strategy=bite)
