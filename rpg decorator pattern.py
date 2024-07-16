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

    def get_name(self):
        return self.name


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


class FireDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Fire", 0, 3, 0, equipment)
        self.equipment = equipment
    def get_attack(self):
        return self.attack + self.equipment.get_attack()


class IceDecorator(EquipmentDecorator):
    def __init__(self, equipment):
        super().__init__("Ice", 0, 0, 3, equipment)
        self.equipment = equipment

    def get_attack(self):
        return self.attack + self.equipment.get_attack()


class Sword(Equipment):
    pass


class Armor(Equipment):
    pass


# Example usage
sword = Sword("Sword", 0, 10, 0)
armor = Armor("Armor", 0, 0, 5)
fire_sword = FireDecorator(sword)
fire_armor = FireDecorator(armor)
fire_and_ice_armor = IceDecorator(fire_armor)
character_a = Character("Warrior", 100, 10, 5, sword=sword, armor=fire_armor)
character_b = Character("Warrior", 100, 10, 5,
                        sword=fire_sword, armor=fire_and_ice_armor)

# Should show character stats without sword enhancements
print(character_a.get_stats())
print(f"Character Attack with Sword: {character_a.get_attack()}")
print(f"Character Defense with Armor: {character_a.get_defense()}")

# Should show character stats with fire sword enhancements
print(character_b.get_stats())
print(f"Character Attack with {character_b.sword.get_name()}: {character_b.get_attack()}")
print(f"Character Defense with {character_b.armor.get_name()}: {
      character_b.get_defense()}")
