from Equipment import Sword, Armor, FireDecorator, ColdDecorator
from Character import Character, HeavyAttack, MeleeAttack, DodgeDefense, ShieldDefense
from dungeon import *


def fight(monsters, character) -> bool:
    character_initiative = [die(20), character]
    monster_initiative = [[die(20), monster] for monster in monsters]
    initiative = monster_initiative + [character_initiative]
    initiative.sort(reverse=True, key=lambda x: x[0])

    print(f'initiative order')

    while (monsters):
        monster_names = {i: f'{monster.name}, health {
            monster.health}' for i, monster in enumerate(monsters)}
        monster_info = {i: f'{monster.get_stats()}' for i,
                        monster in enumerate(monsters)}

        for init in initiative:
            print(f'{init[0]}, {init[1].name}')
            if type(init[1]) is Monster:
                init[1].attack_action(character)
            if type(init[1]) is Character:
                print(f"you are fighting {monster_names}")
                print("choose a monster to attack")
                x = input()
                character.attack_action(monsters[int(x)-1])

    return True


# Example usage
room_factories = [EncounterRoomFactory, MonsterRoomFactory]
dungeon = Dungeon("First lavel", room_factories)

sword = Sword("Sword", 0, 10, 0)
armor = Armor("Armor", 0, 0, 5)
fire_sword = FireDecorator(sword)
fire_armor = FireDecorator(armor)
fire_and_ice_armor = ColdDecorator(fire_armor)
character_a = Character(
    "Warrior", 100, 10, 5, sword=sword, armor=fire_armor,
    attack_strategy=MeleeAttack(), defense_strategy=DodgeDefense())
character_b = Character(
    "Warrior", 100, 10, 5,
    sword=fire_sword, armor=fire_and_ice_armor,
    attack_strategy=HeavyAttack(), defense_strategy=ShieldDefense())


while True:
    current_room = dungeon.create_room()
    match current_room:
        case MonsterRoom():
            print(current_room.name)
            if (fight(current_room.monsters, character_a)):
                print("hey")
                # choose_treature()
            # break
        case EncounterRoom():
            print(current_room.name)


"""
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
"""

"""
enter a room
monster room
choose a monster
choose an attack
while monster alive:
    attack roll:
        success:
            attack action
            dead?:
                treature
        failure -> maybe something?  

    each monster attack:
        success:
            attack action
            charecter dead?:
                End
        failure -> maybe something?   
    
        
enter a room
encounet room
print info
choose an action
roll:
    success:
        treature
    failure:
        something     
"""
