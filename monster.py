from abc import ABC, ABCMeta, abstractmethod
import random
from typing import Callable
from Character import *
from dice import die


class Monster(Character, metaclass=ABCMeta):
    def __init__(self, name, health, attack, defense, attack_strategy: AttackFn, xp):
        super().__init__(name, health, attack, defense, attack_strategy, xp)


class Goblin(Monster):
    def __init__(self):
        super().__init__(
            name= "Rat", health=5, attack=5, 
            defense=5, attack_strategy= poison_dart, xp= 200)


class Rat(Monster):
    def __init__(self):
        super().__init__(
            name="Rats", health=5, attack=5,
            defense=3, attack_strategy=bite,xp= 100)


class Bat(Monster):
    def __init__(self):
        super().__init__(
            name="Bats", health=5, attack=3,
            defense=5, attack_strategy=bite, xp= 150)

def MonsterFactory() -> Monster:
    monsters = [Goblin, Rat, Bat]
    return random.choice(monsters)()

bat = Bat()
rat = Rat()
text = bat.attack_action(rat)
print(text)