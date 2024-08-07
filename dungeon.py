from abc import ABC
from random import choice
from monster import *
from Equipment import EquipmentFactory

class Room(ABC):
    def __init__(
            self, name, treature):
        self.name = name
        self.treature = treature

    @abstractmethod
    def describe(self):
        pass

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
    def __init__(self, name, info, treature, options):
        super().__init__(name, treature)
        self.info = info
        self.name = name
        self.options = options

    def describe(self):
        description = f"{self.info}\nOptions:"
        for i, option in enumerate(self.options, start=1):
            description += f"\n{i}. {option['text']
                                     } (DC {option['DC']} {option['type']})"
        return description
    


class MonsterRoom(Room):
    def __init__(self, name, treature, monsters):
        super().__init__(name, treature)
        self.monsters = monsters
    def describe(self):
        describtion = f"""
        This room is filled with {len(self.monsters)} monsters.
        """
        return describtion



def EncounterRoomFactory() -> EncounterRoom:
    name = "Dark Room"
    info = "Old man in the room"
    treature = EquipmentFactory()
    option1 = {
        "text": "try to run away",
        "type": "Dexterity", 
        "DC": randint(8, 14),
        "succeed": "you got away!",
        "fail": "he got you, you loose somthing",
        "treature": None
        }
    option2 = {
        "text": "try to persuade",
        "type": "Charisma",
        "DC": randint(8, 14),
        "succeed": "he likes you!",
        "fail": "he dosent likes you!",
        "treature": None
    }
    option3 = {
        "text": "try to intinidate him",
        "type": "Charisma",
        "DC": randint(8, 14),
        "succeed": "he got scared and ran away!",
        "fail": "he lugh at you",
        "treature": None
    }
    options = [option1, option2, option3]

    return EncounterRoom(name, info, treature, options)


def MonsterRoomFactory() -> MonsterRoom:
    name = "Scary Room"
    treature = EquipmentFactory()
    monsters = [MonsterFactory() for _ in range(randint(1, 3))]
    return MonsterRoom(name, treature, monsters)
