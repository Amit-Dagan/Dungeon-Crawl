from abc import ABC
from random import choice
from monster import *

class Room(ABC):
    def __init__(
            self, name, treature):
        self.name = name
        self.treature = treature



class Dungeon:
    def __init__(
            self, name):
        self.name = name
        self.room_factories = [EncounterRoomFactory, MonsterRoomFactory]
        self.rooms = []
    
    def create_room(self) -> Room:
        factory = choice(self.room_factories)
        room = factory()
        self.rooms.append(room)
        return room

class EncounterRoom(Room):
    def __init__(self, name, info, treature):
        super().__init__(name, treature)
        self.info = info
    def describe(self):
        return "This room is filled with traps."


class MonsterRoom(Room):
    def __init__(self, name, monsters, treature):
        super().__init__(name, treature)
        num_of_monsters = randint(1, 3)
        monsters = [MonsterFactory() for _ in range(num_of_monsters)]
        self.monsters = monsters
    def describe(self):
        describtion = f"""
        This room is filled with {len(self.monsters)} monsters.
        """
        return describtion



def EncounterRoomFactory() -> EncounterRoom:
    name = "Dark Room"
    info = "Old man in the room"
    treature = "old ring"
    return EncounterRoom(name, info, treature)


def MonsterRoomFactory() -> MonsterRoom:
    name = "Scary Room"
    treature = "10 gold"
    rat1 = Rat()
    rat2 = Rat()
    monsters = [rat1, rat2]
    return MonsterRoom(name, monsters, treature)
