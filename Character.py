from abc import ABC, abstractmethod

class Character:
    def __init__(self, name, health, attack, defense, armor, sword):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.armor = armor
        self.sword = sword


    def get_stats(self):
        return f"Character: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def get_attack(self):
        return self.attack + self.sword.get_attack() + self.armor.get_attack()

    def get_defense(self):
        return self.defense + self.sword.get_defense() + self.armor.get_defense()

    def update_sword(self, sword):
        self.sword = sword




