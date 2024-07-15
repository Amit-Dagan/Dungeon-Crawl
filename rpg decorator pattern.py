from abc import ABC

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


class Equipment(ABC):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_stats(self):
        return f"Equipment: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense


class EquipmentDecorator(Equipment):
    def __init__(self, name, health, attack, defense, equipment):
        super().__init__(name, health, attack, defense)
        self.equipment = equipment

    def get_attack(self):
        return self.attack + self.equipment.get_attack()

    def get_defense(self):
        return self.defense + self.equipment.get_defense()


class Sword(Equipment):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
    
    def get_defense(self):
        return self.defense

    def get_attack(self):
        return self.attack


class Armor(Equipment):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def get_defense(self):
        return self.defense

    def get_attack(self):
        return self.attack


# Example usage
sword = Sword("Sword", 0, 0, 0)
armor = Armor("Sword", 0, 0, 0)
fire_sword = EquipmentDecorator("fire", 0, 5, 0, sword)
character_a = Character("Warrior", 100, 10, 5, sword=sword, armor=armor)
character_b = Character("Warrior", 100, 10, 5, sword=fire_sword, armor=armor)

# Should show character stats without sword enhancements
print(character_a.get_stats())
print(f"Character Attack with Sword: {character_a.get_attack()}")
print(character_b.get_stats())
print(f"Character Attack with Sword: {character_b.get_attack()}")
