from abc import ABC, ABCMeta, abstractmethod
import random
from typing import Callable
from Character import *
from dice import die


class Monster(Character, metaclass=ABCMeta):
    def __init__(self, name, health, attack, defense, attack_strategy: AttackFn, xp):
        super().__init__(name, health, attack, defense, attack_strategy, xp)


class Goblin(Monster):
    def __init__(self):
        super().__init__(
            name= "Goblin", health=5, attack=5, 
            defense=5, attack_strategy= poison_dart, xp= 200)


class Rat(Monster):
    def __init__(self):
        super().__init__(
            name="Rats", health=5, attack=5,
            defense=3, attack_strategy=bite,xp= 100)


class Bat(Monster):
    def __init__(self):
        super().__init__(
            name="Bats", health=5, attack=3,
            defense=5, attack_strategy=bite, xp= 150)

def MonsterFactory() -> Monster:
    monsters = [Goblin, Rat, Bat]
    return random.choice(monsters)()

# Add to monster.py


class Skeleton(Monster):
    def __init__(self):
        super().__init__(
            name="Skeleton", health=8, attack=4,
            defense=6, attack_strategy=bone_strike, xp=200)


class Spider(Monster):
    def __init__(self):
        super().__init__(
            name="Spider", health=6, attack=7,
            defense=4, attack_strategy=web_attack, xp=250)


class Slime(Monster):
    def __init__(self):
        super().__init__(
            name="Slime", health=15, attack=3,
            defense=2, attack_strategy=acid_splash, xp=180)


class Zombie(Monster):
    def __init__(self):
        super().__init__(
            name="Zombie", health=12, attack=4,
            defense=3, attack_strategy=shamble_attack, xp=220)


class Orc(Monster):
    def __init__(self):
        super().__init__(
            name="Orc", health=15, attack=6,
            defense=5, attack_strategy=axe_attack, xp=300)


class Kobold(Monster):
    def __init__(self):
        super().__init__(
            name="Kobold", health=4, attack=6,
            defense=4, attack_strategy=spear_attack, xp=150)


class BossMonster(Monster):
    def __init__(self, name, health, attack, defense, attack_strategy, special_attack, xp):
        super().__init__(name, health, attack, defense, attack_strategy, xp)
        self.special_attack_strategy = special_attack
        self.special_cooldown = 0

    def attack_action(self, character) -> str:
        if self.special_cooldown <= 0 and self.health <= self.max_health // 2:
            text = f"{self.name} uses a special attack!\n"
            text += self.special_attack_strategy(
                character=character, attack_bonus=self.attack)
            self.special_cooldown = 3  # Can use special again after 3 turns
            return text
        else:
            text = super().attack_action(character)
            if self.special_cooldown > 0:
                self.special_cooldown -= 1
            return text


class Dragon(BossMonster):
    def __init__(self):
        super().__init__(
            name="Dragon", health=40, attack=8,
            defense=8, attack_strategy=claw_attack,
            special_attack=fire_breath, xp=1000)
        self.max_health = 40


class Necromancer(BossMonster):
    def __init__(self):
        super().__init__(
            name="Necromancer", health=25, attack=6,
            defense=5, attack_strategy=staff_strike,
            special_attack=summon_undead, xp=800)
        self.max_health = 25


# Additional attack strategies
def bone_strike(character, attack_bonus):
    text = f"It strikes with bony limbs at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"It hits!\n "
        dmg = die(6)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The strike misses!\n "
    return text


def web_attack(character, attack_bonus):
    text = f"It shoots sticky webs at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The web entangles!\n "
        dmg = die(4)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
        text += f"{character.name} is slowed down!\n "
        character.defense -= 1
    else:
        text += "The web misses!\n "
    return text


def acid_splash(character, attack_bonus):
    text = f"It splashes acid on {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The acid burns!\n "
        dmg = die(6)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The acid misses!\n "
    return text


def shamble_attack(character, attack_bonus):
    text = f"It shambles toward {character.name} and attacks\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"It hits!\n "
        dmg = die(8)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The attack misses!\n "
    return text


def axe_attack(character, attack_bonus):
    text = f"It swings its axe at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The axe connects!\n "
        dmg = die(10)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The axe misses!\n "
    return text


def spear_attack(character, attack_bonus):
    text = f"It jabs its spear at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The spear hits!\n "
        dmg = die(6)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The spear misses!\n "
    return text


def claw_attack(character, attack_bonus):
    text = f"It slashes with powerful claws at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The claws tear flesh!\n "
        dmg = die(8) + 2
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The claws miss!\n "
    return text


def fire_breath(character, attack_bonus):
    text = f"It breathes a cone of fire at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense() - 2):  # Easier to hit with breath
        text += f"The flames engulf!\n "
        dmg = die(6) + die(6) + die(6)
        if character.get_resistence('fire') > 0:
            dmg = dmg // 2
            text += f"{character.name} resists some of the fire!\n"
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
        character.status['fire'] = 2
    else:
        text += "The character dodges the flames!\n "
    return text


def staff_strike(character, attack_bonus):
    text = f"It strikes with a dark staff at {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense()):
        text += f"The staff connects!\n "
        dmg = die(6)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The staff misses!\n "
    return text


def summon_undead(character, attack_bonus):
    text = f"It raises undead to attack {character.name}\n "
    attack_roll = die(20) + attack_bonus
    if (attack_roll >= character.get_defense() - 3):  # Easier to hit with summoned undead
        text += f"The undead swarm attacks!\n "
        dmg = die(4) + die(4) + die(4)
        text += f"{character.name} health = {character.health} - {dmg} = {character.health - dmg}\n "
        character.health -= dmg
    else:
        text += "The character evades the undead!\n "
    return text


# Update MonsterFactory to include new monsters
def MonsterFactory() -> Monster:
    monsters = [Goblin, Rat, Bat, Skeleton, Spider, Slime, Zombie, Orc, Kobold]
    return random.choice(monsters)()


# Boss Monster Factory for special encounters
def BossMonsterFactory() -> Monster:
    bosses = [Dragon, Necromancer]
    return random.choice(bosses)()
