from abc import ABC, abstractmethod
import random
from typing import Type

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

    def sword_attack(self, character: Character, attack_bonus) -> str:
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus
        text = f"You rolled {natural_roll} + {attack_bonus} = {attack_roll}\n"
        if (natural_roll == 20):
            text += (f"It creets!\n ")
            dmg = die(self.attack) + die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            text += (f"It secceeds!\n ")
            dmg = die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n ")
            character.health -= dmg
        else:
            text += ("It dose not secceeds!\n ")
        return text

class Armor(Equipment):
    def __init__(self):
        super().__init__("Armor", 0, 8, 0)


def EquipmentFactory(type = "normal") -> Equipment:
    equipments = [Armor, Sword]
    decorators = [ColdDecorator, FireDecorator, MightDecorator, LightDecorator]
    equipment = random.choice(equipments)()
    if (type == "rare"):
        equipment = random.choice(decorators)(equipment)
    elif (type == "epic"):
        decorators_copy = decorators[:]  # Copy to avoid duplicates
        decorator1: Type[Equipment] = random.choice(decorators_copy)
        equipment = decorator1(equipment)
        decorators_copy.remove(decorator1)
        decorator2: Type[Equipment] = random.choice(decorators_copy)
        equipment = decorator2(equipment)

    return equipment

# Add to Equipment.py


class Staff(Equipment):
    def __init__(self):
        super().__init__("Staff", 0, 5, 0)

    def staff_attack(self, character: Character, attack_bonus) -> str:
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus
        text = f"You cast a spell with your {self.name}!\n"
        text += f"You rolled {natural_roll} + {attack_bonus} = {attack_roll}\n "
        if (natural_roll == 20):
            text += (f"Critical spell hit!\n ")
            dmg = die(self.attack) + die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            text += (f"The spell hits!\n ")
            dmg = die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n ")
            character.health -= dmg
        else:
            text += ("The spell fizzles...\n ")
        return text


class Bow(Equipment):
    def __init__(self):
        super().__init__("Bow", 0, 6, 0)

    def bow_attack(self, character: Character, attack_bonus) -> str:
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus
        text = f"You fire an arrow from your {self.name}!\n"
        text += f"You rolled {natural_roll} + {attack_bonus} = {attack_roll}\n "
        if (natural_roll == 20):
            text += (f"Critical hit!\n ")
            dmg = die(self.attack) + die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            text += (f"The arrow hits!\n ")
            dmg = die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n ")
            character.health -= dmg
        else:
            text += ("The arrow misses!\n ")
        return text


class Mace(Equipment):
    def __init__(self):
        super().__init__("Mace", 0, 7, 0)

    def mace_attack(self, character: Character, attack_bonus) -> str:
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus
        text = f"You swing your {self.name}!\n"
        text += f"You rolled {natural_roll} + {attack_bonus} = {attack_roll}\n "
        if (natural_roll == 20):
            text += (f"Critical smash!\n ")
            dmg = die(self.attack) + die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            text += (f"The mace connects!\n ")
            dmg = die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n ")
            character.health -= dmg
        else:
            text += ("The attack misses!\n ")
        return text


class Dagger(Equipment):
    def __init__(self):
        super().__init__("Dagger", 0, 4, 0)

    def dagger_attack(self, character: Character, attack_bonus) -> str:
        natural_roll = die(20)
        attack_roll = natural_roll + attack_bonus + 2  # Daggers are easier to hit with
        text = f"You stab with your {self.name}!\n"
        text += f"You rolled {natural_roll} + {attack_bonus + 2} = {attack_roll}\n "
        if (natural_roll == 20 or natural_roll == 19):  # Daggers have higher crit chance
            text += (f"Critical stab!\n ")
            dmg = die(self.attack) + die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n")
            character.health -= dmg
        elif (attack_roll >= character.get_defense()):
            text += (f"The dagger strikes!\n ")
            dmg = die(self.attack)
            text += (f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n ")
            character.health -= dmg
        else:
            text += ("The attack misses!\n ")
        return text


class Robe(Equipment):
    def __init__(self):
        super().__init__("Robe", 0, 0, 2)
        self.resistence['fire'] = 1
        self.resistence['cold'] = 1


class LeatherArmor(Equipment):
    def __init__(self):
        super().__init__("Leather Armor", 0, 0, 4)
        self.resistence['poison'] = 1


class ChainMail(Equipment):
    def __init__(self):
        super().__init__("Chain Mail", 0, 0, 6)


class PlateMail(Equipment):
    def __init__(self):
        super().__init__("Plate Mail", 0, 0, 8)
        self.resistence['fire'] = 1


# New decorators for more equipment variety
class PoisonDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Poison", 0, 2, 0, equipment)
        self.equipment = equipment
        self.resistence['poison'] = 2

    def get_attack(self):
        # Special override for poison weapons
        base_attack = super().get_attack()
        if isinstance(self.equipment, Sword) or isinstance(self.equipment, Dagger):
            return base_attack + 1  # Extra bonus for bladed weapons
        return base_attack


class HolyDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Holy", 0, 2, 2, equipment)
        self.equipment = equipment


class ArcaneDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Arcane", 0, 3, 0, equipment)
        self.equipment = equipment
        # Arcane items boost spell effectiveness
        if isinstance(self.equipment, Staff):
            self.attack += 2


class VampiricDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Vampiric", 0, 1, 0, equipment)
        self.equipment = equipment
        # Vampiric items have life drain but are weaker against undead


# Expanded EquipmentFactory with more variety
def EquipmentFactory(type="normal") -> Equipment:
    equipment_types = {
        "weapon": [Sword, Staff, Bow, Mace, Dagger],
        "armor": [Armor, Robe, LeatherArmor, ChainMail, PlateMail]
    }

    decorators = {
        "common": [ColdDecorator, FireDecorator],
        "uncommon": [MightDecorator, LightDecorator, PoisonDecorator],
        "rare": [HolyDecorator, ArcaneDecorator, VampiricDecorator]
    }

    # Choose equipment category (weapon or armor)
    category = random.choice(list(equipment_types.keys()))

    # Choose specific equipment type from that category
    equipment_class = random.choice(equipment_types[category])
    equipment = equipment_class()

    # Add decorators based on rarity
    if type == "normal":
        # No decorators for normal equipment
        pass
    elif type == "uncommon":
        decorator = random.choice(decorators["common"])
        equipment = decorator(equipment)
    elif type == "rare":
        decorator = random.choice(
            decorators["common"] + decorators["uncommon"])
        equipment = decorator(equipment)
    elif type == "epic":
        # First decorator from common or uncommon
        decorator1 = random.choice(
            decorators["common"] + decorators["uncommon"])
        equipment = decorator1(equipment)

        # Second decorator from any category (avoid duplicate categories)
        all_decorators = []
        for decorator_list in decorators.values():
            all_decorators.extend(decorator_list)
        # Remove the already used decorator from choices
        all_decorators = [d for d in all_decorators if d != decorator1]
        decorator2 = random.choice(all_decorators)
        equipment = decorator2(equipment)
    elif type == "legendary":
        # First decorator from rare
        decorator1 = random.choice(decorators["rare"])
        equipment = decorator1(equipment)

        # Second decorator from any category
        all_decorators = []
        for decorator_list in decorators.values():
            all_decorators.extend(decorator_list)
        # Remove the already used decorator from choices
        all_decorators = [d for d in all_decorators if d != decorator1]
        decorator2 = random.choice(all_decorators)
        equipment = decorator2(equipment)

    return equipment

### testing ###
# normal_eq = EquipmentFactory()
# print(normal_eq.get_name())

# rare_eq = EquipmentFactory(type="rare")
# print(rare_eq.get_name())

# epic_eq = EquipmentFactory(type="epic")
# print(epic_eq.get_name())



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
