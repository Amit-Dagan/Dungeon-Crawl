from abc import ABC, abstractmethod

from Character import Character
from dice import die

class Equipment(ABC):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.resistence = {
            'poison': 0,
            'fire': 0,
            'cold': 0
        }
    def get_stats(self):
        return f"Equipment: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_name(self):
        return self.name

    def get_resistence(self, type):
        return self.resistence[type]


class EquipmentDecorator(Equipment):
    def __init__(self, name, health, attack, defense, equipment):
        super().__init__(name, health, attack, defense)
        self.equipment = equipment

    def get_attack(self):
        return self.attack + self.equipment.get_attack()

    def get_defense(self):
        return self.defense + self.equipment.get_defense()

    def get_name(self):
        return self.equipment.get_name() + ' of ' + self.name

    def get_resistence(self, type):
        return self.resistence[type] + self.equipment.get_resistence(type)


class FireDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Fire", 0, 3, 0, equipment)
        self.equipment = equipment
        self.resistence['fire'] = 1


class ColdDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Cold", 0, 0, 3, equipment)
        self.equipment = equipment
        self.resistence['cold'] = 1


class Sword(Equipment):
    def __init__(self):
        super().__init__("Sword", 0, 8, 0)
    def sword_attack(self, character: Character, attack_bonus):
        attack_roll = die(20) + attack_bonus
        if (attack_roll >= character.get_defense):
            character.health -= die(self.get_attack())


class Armor(Equipment):
    def __init__(self):
        super().__init__("Armor", 0, 8, 0)




