from Equipment import Sword, Armor, FireDecorator, IceDecorator
from Character import Character

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
print(f"Character Attack with {character_b.sword.get_name()}: {
      character_b.get_attack()}")
print(f"Character Defense with {character_b.armor.get_name()}: {
      character_b.get_defense()}")
