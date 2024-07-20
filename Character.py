from abc import ABC, abstractmethod
from random import randint


class Character:
    def __init__(
            self, name, health, attack, defense, armor, sword,
            attack_strategy, defense_strategy):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.armor = armor
        self.sword = sword
        self.attack_strategy = attack_strategy
        self.defense_strategy = defense_strategy
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
        return f"Character: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense} \n Resistance: {self.get_resistence('cold')}"

    def get_resistence(self, type):
        return self.resistence[type] + self.armor.get_resistence(type)

    def get_attack(self):
        return self.attack + self.sword.get_attack() + self.armor.get_attack()


    def get_defense(self):
        return self.defense + self.sword.get_defense() + self.armor.get_defense()

    def attack_action(self, ac):
        print(type(self.attack_strategy))
        if (isinstance(self.attack_strategy, HeavyAttack)):
            print("the monster in shock!")
        elif (isinstance(self.attack_strategy, MeleeAttack)):
            print("the moster is cut")

        return self.get_attack()*self.attack_strategy.execute(self.attack, ac=ac)

    def defense_action(self, dmg):
        return self.defense_strategy.execute(self.get_defense(), dmg)

    def update_sword(self, sword):
        self.sword = sword

    def update_armor(self, armor):
        self.armor = armor


class AttackStrategy(ABC):
    @abstractmethod
    def execute(self, attack_bonus, ac):
        pass

    def __str__(self):
        return self.__class__.__name__

class MeleeAttack(AttackStrategy):
    def execute(self, attack_bonus, ac):
        die = randint(1, 20)
        if die == 20:
            return 2
        if die + attack_bonus > ac:
            return 1
        return 0.5


class HeavyAttack(AttackStrategy):
    def execute(self, attack_bonus, ac):
        die = randint(1, 20)
        if die >= 19:
            return 2
        if die + attack_bonus > ac:
            return 1.5
        return 0


class DefenseStrategy(ABC):
    @abstractmethod
    def execute(self, defense_bonus, dmg):
        pass


class ShieldDefense(DefenseStrategy):
    def execute(self, defense_bonus, dmg):
        return max(dmg - defense_bonus, 0)


class DodgeDefense(DefenseStrategy):
    def execute(self, defense_bonus, dmg):
        die = randint(1, 10)
        if die + defense_bonus > dmg:
            return 0
        return dmg
