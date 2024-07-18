from Equipment import Sword, Armor, FireDecorator, IceDecorator
from Character import Character, HeavyAttack, MeleeAttack, DodgeDefense, ShieldDefense
from dungeon import Dungeon, Room, EncounterRoomFactory, MonsterRoomFactory

# Example usage
room_factories = [EncounterRoomFactory, MonsterRoomFactory]
dungeon = Dungeon("First lavel", room_factories)
dungeon.create_room()
for room in dungeon.rooms:
    print(room.name)

sword = Sword("Sword", 0, 10, 0)
armor = Armor("Armor", 0, 0, 5)
fire_sword = FireDecorator(sword)
fire_armor = FireDecorator(armor)
fire_and_ice_armor = IceDecorator(fire_armor)
character_a = Character(
    "Warrior", 100, 10, 5, sword=sword, armor=fire_armor,
    attack_strategy=MeleeAttack(), defense_strategy=DodgeDefense())
character_b = Character(
    "Warrior", 100, 10, 5,
    sword=fire_sword, armor=fire_and_ice_armor,
    attack_strategy=HeavyAttack(), defense_strategy=ShieldDefense())


print(character_a.get_stats())
print('\n')
print(f"Character Attack with {character_a.sword.get_name()} and deals {
      character_a.attack_action(14)}")
print(f"Character Defense with {character_a.armor.get_name()} and takes {
      character_a.defense_action(15)} damage")

print('\n')

print(character_b.get_stats())
print('\n')

print(f"Character Attack with {character_b.sword.get_name()} and deals {
      character_b.attack_action(14)}")
print(f"Character Defense with {character_b.armor.get_name()} and takes {
      character_b.defense_action(15)} damage")


print("""
       ____
      |    |_
      | @   _
      |____|
      """)