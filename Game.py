from Equipment import *
from Character import *
from dungeon import *
from Player import *
from screen import *
from town import *


class Game:
    def __init__(self, stdscr):
        self.screen = Screen(stdscr)
        player_class = self.screen.choose("choose a hero", CLASSES)
        name = self.screen.get_text("Give your hero a name")
        self.player = player_class(name)
        self.dungeon = Dungeon("First level")
        self.current_room = None
        self.town = Town()

    def explore(self):
        self.screen.show_player(self.player)
        # Create a room using the dungeon's room factory
        self.current_room = self.dungeon.create_room()

        match self.current_room:
            case MonsterRoom():
                self.screen.animation_write_main(self.current_room.describe())
                self.fight()
                # After fight, check for treasure
                if self.player.health > 0:
                    self.get_treasure()
            case EncounterRoom():
                self.encounter()

    def encounter(self):
        chosen_option = self.screen.show_encounter(self.current_room)
        roll = die(20)
        match chosen_option["type"]:
            case "charisma":
                roll = roll + self.player.charisma
            case "dexterity":
                roll = roll + self.player.dexterity
            case "wisdom":
                roll = roll + self.player.wisdom

        if (roll >= chosen_option["DC"]):
            self.screen.animation_write_main(chosen_option["succeed"])
            # Maybe get treasure on success
            if "treature" in chosen_option and chosen_option["treature"]:
                self.get_treasure()
        else:
            self.screen.animation_write_main(chosen_option["fail"])

    def get_treasure(self):
        if self.current_room.treature:
            self.screen.animation_write_main(
                f"You found treasure: {self.current_room.treature.get_name()}")
            # Add treasure to inventory or equip it
            equip = self.screen.choose(
                "Equip treasure?", {"Yes": True, "No": False})
            if equip:
                if isinstance(self.current_room.treature, Sword):
                    self.player.update_sword(self.current_room.treature)
                elif isinstance(self.current_room.treature, Armor):
                    self.player.update_armor(self.current_room.treature)
                self.screen.animation_write_main(
                    f"You equipped {self.current_room.treature.get_name()}")
            else:
                self.player.inventory.append(self.current_room.treature)
                self.screen.animation_write_main(
                    f"Added {self.current_room.treature.get_name()} to inventory")
            self.screen.show_player(self.player)
            self.screen.wait()

    def fight(self):
        monsters = self.current_room.monsters
        character_initiative = [die(20), self.player]
        monster_initiative = [[die(20), monster] for monster in monsters]
        initiative = monster_initiative + [character_initiative]
        initiative.sort(reverse=True, key=lambda x: x[0])

        # Continue fighting until all monsters are defeated or player is dead
        while self.current_room.monsters and self.player.health > 0:
            # Create a dictionary of monsters for selection
            monster_dict = {
                f"{monster.name} (HP:{monster.health})": monster
                for monster in self.current_room.monsters
            }

            # Process each entity's turn in initiative order
            for roll, entity in initiative:
                # Skip entities that are dead
                if isinstance(entity, Monster) and entity.health <= 0:
                    continue
                if isinstance(entity, Player) and entity.health <= 0:
                    break

                self.screen.animation_write_main(
                    f'Initiative: {roll}, {entity.name}')
                self.screen.wait()

                # Monster's turn
                if isinstance(entity, Monster) and entity.health > 0:
                    text = entity.attack_action(self.player)
                    self.screen.animation_write_main(text=text)
                    self.screen.show_player(self.player)
                    self.screen.wait()

                    # Check if player is dead
                    if self.player.health <= 0:
                        self.screen.animation_write_main(
                            "You have been defeated!")
                        self.screen.wait()
                        return False

                # Player's turn
                if isinstance(entity, Player) and self.current_room.monsters:
                    if len(monster_dict) > 0:
                        target = self.screen.choose(
                            "Choose a monster to attack:", monster_dict)
                        text = self.player.attack_action(target)
                        self.screen.animation_write_main(text=text)
                        self.screen.show_player(self.player)
                        self.screen.wait()

                        # Update monsters list after player's attack
                        self.current_room.update_monsters()
                        # Recalculate monster_dict for next round
                        monster_dict = {
                            f"{monster.name} (HP:{monster.health})": monster
                            for monster in self.current_room.monsters
                        }

                        # Check if all monsters are defeated
                        if not self.current_room.monsters:
                            xp_gained = self.current_room.get_xp()
                            self.player.xp += xp_gained
                            self.screen.animation_write_main(
                                f"All monsters defeated! You gained {xp_gained} XP.")
                            self.screen.show_player(self.player)
                            self.screen.wait()
                            return True

            # Update monster list after each round
            self.current_room.update_monsters()

        return self.player.health > 0  # Return True if player survived

    def visit_town(self):
        self.screen.animation_write_main("You enter the town...")
        # Implement town visit logic
        options = {"Shop": self.shop, "Rest": self.rest, "Leave": lambda: None}
        choice = self.screen.choose("What would you like to do?", options)
        if choice:
            choice()

    def shop(self):
        self.screen.animation_write_main("Welcome to the shop!")
        items = {
            f"{item.get_name()} - {item.get_stats()}": item for item in self.town.items}
        items["Leave"] = None

        while True:
            item = self.screen.choose("What would you like to buy?", items)
            if item is None:
                break

            if self.player.gold >= 10:  # Simple price system
                self.player.gold -= 10
                self.player.inventory.append(item)
                self.screen.animation_write_main(
                    f"You purchased {item.get_name()}")
                self.town.items.remove(item)
                items.pop(next(k for k, v in items.items() if v == item))
            else:
                self.screen.animation_write_main("Not enough gold!")

            if not self.town.items:
                self.screen.animation_write_main("Shop is out of items!")
                break

    def rest(self):
        self.screen.animation_write_main("You rest and recover your health.")
        self.player.health = 25  # Reset to max health
        self.screen.show_player(self.player)


def main(stdscr):
    game = Game(stdscr)
    game_over = False

    while not game_over:
        # Main game loop
        options = {"Explore Dungeon": 1, "Visit Town": 2, "Quit": 3}
        choice = game.screen.choose("What would you like to do?", options)
        game.screen.animation_write_hero(choice)
        game.screen.wait()
        if choice == 1:
            game.explore()
            # Check if player died
            if game.player.health <= 0:
                game.screen.animation_write_main("Game Over!")
                game_over = True
        elif choice == 2:
            game.visit_town()
        elif choice == 3:
            game.screen.animation_write_main("Thank you for playing!")
            game_over = True


if __name__ == "__main__":
    wrapper(main)
