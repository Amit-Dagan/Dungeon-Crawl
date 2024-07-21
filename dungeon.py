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
            self, name, room_factories):
        self.name = name
        self.room_factories = room_factories
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
        self.monsters = monsters
    def describe(self):
        return "This room is filled with monsters."



def EncounterRoomFactory() -> EncounterRoom:
    name = "Dark Room"
    info = "Old man in the room"
    treature = "old ring"
    return EncounterRoom(name, info, treature)


def MonsterRoomFactory() -> MonsterRoom:
    name = "Scary Room"
    monster = "Goblin"
    treature = "10 gold"
    rat1 = Rat()
    rat2 = Rat()
    monsters = [rat1, rat2]
    return MonsterRoom(name, monsters, treature)
