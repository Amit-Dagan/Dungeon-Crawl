from abc import ABC, ABCMeta, abstractmethod
from random import randint
from Character import *
from Equipment import *


class Player(Character, metaclass=ABCMeta):
    def __init__(
            self, name, health, attack, defense,
            attack_strategy, dextirity, wisdom, charisma):
        super().__init__(name, health, attack, defense,
                       attack_strategy, xp=0)
        self.dexterity = dextirity
        self.wisdom = wisdom
        self.charisma = charisma
        self.gold = 0
        self.inventory = []
        

    def get_inventory(self):
        return self.inventory
    
    def update_armor(self, armor):
        self.armor = armor

    def update_weapon(self, weapon):
        self.weapon = weapon
        self.attack_strategy = weapon.attack_strategy


class Fighter(Player):
    def __init__(self, name):
        self.sword = Sword()
        super().__init__(name, 25, 5, 5,
                         self.sword.sword_attack, 1, 0, 1)
        self.armor = Armor()
        
    def get_stats(self):
        return super().get_stats() + f"\n sword = {self.sword.get_name()} \n armor = {self.armor.get_name()}"


    def __name__():
        return "Fighter"
        
# Add to Player.py

class Wizard(Player):
    def __init__(self, name):
        self.staff = Staff()
        super().__init__(name, 15, 8, 3,
                         self.staff.staff_attack, 0, 3, 2)
        self.armor = Robe()
        self.mana = 20
        self.max_mana = 20

    def get_stats(self):
        return super().get_stats() + f"\n staff = {self.staff.get_name()} \n armor = {self.armor.get_name()} \n mana = {self.mana}/{self.max_mana}"

    def fireball(self, character):
        if self.mana >= 5:
            text = f"{self.name} casts Fireball at {character.name}!\n "
            attack_roll = die(20) + self.attack
            if attack_roll >= character.get_defense():
                dmg = die(8) + die(8)
                text += f"It hits for {dmg} damage!\n "
                character.health -= dmg
                character.status['fire'] = 2
                text += f"{character.name} is set on fire!\n "
            else:
                text += "The spell fizzles...\n "
            self.mana -= 5
            return text
        else:
            return f"{self.name} doesn't have enough mana to cast Fireball!"

    def heal(self, character):
        if self.mana >= 3:
            healing = die(8)
            text = f"{self.name} casts Healing on {character.name}!\n "
            text += f"{character.name} recovers {healing} health.\n "
            character.health += healing
            self.mana -= 3
            return text
        else:
            return f"{self.name} doesn't have enough mana to cast Heal!"

    def __name__():
        return "Wizard"


class Ranger(Player):
    def __init__(self, name):
        self.bow = Bow()
        super().__init__(name, 20, 6, 4,
                         self.bow.bow_attack, 3, 2, 1)
        self.armor = LeatherArmor()
        self.arrows = 20

    def get_stats(self):
        return super().get_stats() + f"\n bow = {self.bow.get_name()} \n armor = {self.armor.get_name()} \n arrows = {self.arrows}"

    def multishot(self, character):
        if self.arrows >= 3:
            text = f"{self.name} fires multiple arrows at {character.name}!\n "
            hits = 0
            total_damage = 0

            for i in range(3):
                attack_roll = die(20) + self.attack
                if attack_roll >= character.get_defense():
                    damage = die(4)
                    total_damage += damage
                    hits += 1

            if hits > 0:
                text += f"{hits} arrows hit for {total_damage} damage!\n "
                character.health -= total_damage
            else:
                text += "All arrows miss!\n "

            self.arrows -= 3
            return text
        else:
            return f"{self.name} doesn't have enough arrows for a multishot!"

    def __name__():
        return "Ranger"


class Cleric(Player):
    def __init__(self, name):
        self.mace = Mace()
        super().__init__(name, 22, 5, 6,
                         self.mace.mace_attack, 0, 2, 3)
        self.armor = ChainMail()
        self.faith = 15
        self.max_faith = 15

    def get_stats(self):
        return super().get_stats() + f"\n mace = {self.mace.get_name()} \n armor = {self.armor.get_name()} \n faith = {self.faith}/{self.max_faith}"

    def smite(self, character):
        if self.faith >= 4:
            text = f"{self.name} calls down divine smite on {character.name}!\n "
            attack_roll = die(20) + self.attack
            if attack_roll >= character.get_defense():
                dmg = die(6) + die(6) + 2
                text += f"It hits for {dmg} damage!\n "
                character.health -= dmg
            else:
                text += "The enemy resists the divine power...\n "
            self.faith -= 4
            return text
        else:
            return f"{self.name} doesn't have enough faith to smite!"

    def bless(self, character):
        if self.faith >= 3:
            text = f"{self.name} blesses {character.name}!\n "
            character.attack += 2
            character.defense += 2
            text += f"{character.name}'s attack and defense increase by 2!\n "
            self.faith -= 3
            return text
        else:
            return f"{self.name} doesn't have enough faith to bless!"

    def __name__():
        return "Cleric"


CLASSES = {"Fighter": Fighter, "Wizard": Wizard,
           "Ranger": Ranger, "Cleric": Cleric}
