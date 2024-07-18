from random import choice

class Dungeon:
    def __init__(
            self, name, room_factories):
        self.name = name
        self.room_factories = room_factories
        self.rooms = []
    
    def create_room(self):
        factory = choice(self.room_factories)
        self.rooms.append(factory())

class Room:
    def __init__(
            self, name, treature):
        self.name = name
        self.treature = treature

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

    return MonsterRoom(name, monster, treature)
