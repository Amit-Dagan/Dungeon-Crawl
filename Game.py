from Equipment import *
from Character import *
from dungeon import *
from Player import *
from screen import *


class Game:
    def __init__(self, stdscr):
        self.screen = Screen(stdscr)
        classes = {"Fighter": Fighter, "Monk": Fighter, "Wizard": Fighter}
        self.player = self.screen.choose("choose a hero", classes)("name")
        self.dungeon = Dungeon("First level")
        self.current_room = None

    def explore(self):
        self.current_room = self.dungeon.create_room()
        match self.current_room:
            case MonsterRoom():
                self.fight()
            case EncounterRoom():
                self.encounter()

    def encounter(self):
        self.screen.show_encounter(self.current_room)

    def fight(self):
        self.screen.animation_write_main(self.current_room.name)

def main(stdscr):

    game = Game(stdscr)
    game.explore()


def fight(monsters, player) -> bool:
    character_initiative = [die(20), player]
    monster_initiative = [[die(20), monster] for monster in monsters]
    initiative = monster_initiative + [character_initiative]
    initiative.sort(reverse=True, key=lambda x: x[0])
    monsters_health = sum([monster.health for monster in monsters])

    while (monsters_health > 0):
        monster_names = {i: f'{monster.name}, health {
            monster.health}' for i, monster in enumerate(monsters)}
        monster_info = {i: f'{monster.get_stats()}' for i,
                        monster in enumerate(monsters)}

        for roll, entity in initiative:
            screen.animation_write_main(f'{roll}, {entity.name}')
            if isinstance(entity, Monster):
                entity.attack_action(player)
            if isinstance(entity, Player):
                print(f"you are fighting {monster_names}")
                print("choose a monster to attack")
                x = input()
                player.attack_action(monsters[int(x)-1])

        monsters_health = sum([monster.health for monster in monsters])
    return True


if __name__ == "__main__":

    wrapper(main)
































# from Equipment import *
# from Character import *
# from dungeon import *
# from Player import *
# from screen import *


# def main():

#     room_factories = [EncounterRoomFactory, MonsterRoomFactory]
#     dungeon = Dungeon("First lavel", room_factories)

#     player = Fighter("Ser Holigan")

#     while True:
#         current_room = dungeon.create_room()
#         match current_room:
#             case MonsterRoom():
#                 print(current_room.describe())
#                 if (fight(current_room.monsters, player)):
#                     print("hey")
#                     # choose_treature()
#                 # break
#             case EncounterRoom():
#                 print(current_room.name)




# def fight(monsters, player) -> bool:
#     character_initiative = [die(20), player]
#     monster_initiative = [[die(20), monster] for monster in monsters]
#     initiative = monster_initiative + [character_initiative]
#     initiative.sort(reverse=True, key=lambda x: x[0])
#     monsters_health = sum([monster.health for monster in monsters])

#     while (monsters_health > 0):
#         monster_names = {i: f'{monster.name}, health {
#             monster.health}' for i, monster in enumerate(monsters)}
#         monster_info = {i: f'{monster.get_stats()}' for i,
#                         monster in enumerate(monsters)}

#         for roll, entity in initiative:
#             print(f'{roll}, {entity.name}')
#             if isinstance(entity, Monster):
#                 entity.attack_action(player)
#             if isinstance(entity, Player):
#                 print(f"you are fighting {monster_names}")
#                 print("choose a monster to attack")
#                 x = input()
#                 player.attack_action(monsters[int(x)-1])

#         monsters_health = sum([monster.health for monster in monsters])
#     return True



# if __name__ == "__main__":

#     main()


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
