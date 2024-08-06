from abc import ABC, abstractmethod
import random

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
        origin_name = self.equipment.get_name()
        if ("of" in origin_name):
            if ("and" in origin_name):
                parts = origin_name.split(" and ")
                new_string = parts[0] + f", {parts[1]} and {self.name}"
                return new_string
            else:
                return origin_name + ' and ' + self.name
        return origin_name + ' of ' + self.name

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


class MightDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Might", 0, 0, 3, equipment)
        self.equipment = equipment
        self.resistence['cold'] = 1


class LightDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Light", 0, 0, 3, equipment)
        self.equipment = equipment
        self.resistence['cold'] = 1


class Sword(Equipment):

    def __init__(self):
        super().__init__("Sword", 0, 8, 0)

    def sword_attack(self, character: Character, attack_bonus):
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus
        if (natural_roll == 20):
            print(f"It creets!")
            dmg = die(self.attack) + die(self.attack)
            print(f"{character.name} health = {
                character.health} - {dmg} = {character.health - dmg}")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            print(f"It secceeds!")
            dmg = die(self.attack)
            print(f"{character.name} health = {
                character.health} - {dmg} = {character.health - dmg}")
            character.health -= dmg
        else:
                print("It dose not secceeds!")


class Armor(Equipment):
    def __init__(self):
        super().__init__("Armor", 0, 8, 0)


def EquipmentFactory() -> Equipment:
    equipments = [Armor, Sword]
    return random.choice(equipments)()


def RareEquipmentFactory() -> Equipment:
    equipments = [Armor, Sword]
    decorators = [ColdDecorator, FireDecorator, MightDecorator, LightDecorator]
    equipment = random.choice(equipments)()
    return random.choice(decorators)(equipment)


def EpichEquipmentFactory() -> Equipment:
    equipments = [Armor, Sword]
    decorators = [ColdDecorator, FireDecorator, MightDecorator, LightDecorator]
    equipment = random.choice(equipments)()
    equipment = random.choice(decorators)(equipment)
    return random.choice(decorators)(equipment)



### testing ###

# sword = Sword()
# print(sword.get_name())
# sword = ColdDecorator(sword)
# print(sword.get_name())
# sword = FireDecorator(sword)
# print(sword.get_name())
# sword = MightDecorator(sword)
# print(sword.get_name())
# sword = LightDecorator(sword)
# print(sword.get_name())
