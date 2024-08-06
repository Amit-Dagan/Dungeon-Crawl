import curses
from curses import wrapper
import time
from dungeon import EncounterRoom
from dice import *


class Screen:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.HEIGHT, self.WIDTH = self.stdscr.getmaxyx()
        self._initialize_screen()

        # Window dimensions and positions
        self.MAIN_WINDOW_HEIGHT = max(1, self.HEIGHT // 3)
        self.MAIN_WINDOW_WIDTH = max(1, (self.WIDTH // 2) - 2)
        self.HERO_WINDOW_HEIGHT = max(1, self.HEIGHT - 2)
        self.HERO_WINDOW_WIDTH = max(1, (self.WIDTH // 2) - 2)

        # Initialize windows
        self.main_window = self._create_window(
            self.MAIN_WINDOW_HEIGHT, self.MAIN_WINDOW_WIDTH, 2, 1, "Main Window Initialized")
        self.second_window = self._create_window(
            self.MAIN_WINDOW_HEIGHT, self.MAIN_WINDOW_WIDTH, self.MAIN_WINDOW_HEIGHT + 2, 1, "Second Window Initialized")
        self.hero_window = self._create_window(
            self.HERO_WINDOW_HEIGHT, self.HERO_WINDOW_WIDTH, 2, self.MAIN_WINDOW_WIDTH + 2)

    def _initialize_screen(self):
        # Print dimensions to help with debugging
        self.stdscr.addnstr(0, 0, f"Screen dimensions: HEIGHT={
                            self.HEIGHT}, WIDTH={self.WIDTH}", 50)
        self.stdscr.refresh()

    def _create_window(self, height, width, starty, startx, init_text=None):
        win = curses.newwin(height, width, starty, startx)
        win.box()
        if init_text:
            win.addnstr(1, 1, init_text, width - 2)
        win.refresh()
        return win

    def _write_text(self, window, text, animated=False):
        window.clear()
        window.box()
        if animated:
            for i in range(len(text)):
                window.addstr(2, 1, text[:i+1])
                window.box()
                window.refresh()
                time.sleep(0.05)
        else:
            window.addstr(2, 1, text)
            window.box()
        window.refresh()

    def write_main(self, text):
        self._write_text(self.main_window, text)

    def animation_write_main(self, text):
        self._write_text(self.main_window, text, animated=True)

    def write_second(self, text):
        self._write_text(self.second_window, text)

    def animation_write_second(self, text):
        self._write_text(self.second_window, text, animated=True)

    def choose(self, text, options):
        self.animation_write_main(text)
        s = ''
        for i, option in enumerate(options, start=1):
            s += f"{i} - {option} \n "
        res = []
        for i, option in enumerate(options):
            res.append(options[option])
        self.animation_write_second(s)
        key = self.stdscr.getkey()
        while (int(key) > i):
            self.animation_write_main("please chose only from those options")
            key = self.stdscr.getkey()
        return res[i-1]


    def show_encounter(self, encounter: EncounterRoom):
        self.animation_write_main(encounter.info)
        s = ''

        for i, option in enumerate(encounter.options, start=1):
            s += f"{i} - to {option["text"]} ({option["type"]})\n "

        self.animation_write_second(s)
        key = self.stdscr.getkey()
        while (int(key) > i):
            self.animation_write_main("please chose only from those options")
            key = self.stdscr.getkey()
        return encounter.options[i]
        

def main(stdscr):
    screen = Screen(stdscr)
    screen.write_main("Hello, Main Window!")
    screen.write_second("Hello, Second Window!")
    screen.animation_write_main("Animating Main Window")
    screen.animation_write_second("Animating Second Window")
    choice = screen.choose("Choose an option:", [
                           "Option 1", "Option 2", "Option 3"])
    screen.write_main(f"You chose: {choice}")


if __name__ == "__main__":
    curses.wrapper(main)
    
# def main(stdscr):
#     screen = Screen(stdscr)
#     screen.write_main("asdasd")
#     time.sleep(1)
#     screen.animation_write_main("gfyjfgyjytj")
#     time.sleep(1)
#     arr = ["option1", "option2", "option3"]
#     text = "please choose a class"
#     screen.choose(text=text, options=arr)

#     stdscr.getkey()  # Wait for a key press to exit


#wrapper(main)















# import time
# import turtle
# from dungeon import *  # Ensure you are importing only what's necessary from dungeon


# class GameScreen:
#     WIDTH = 800
#     HEIGHT = 600
#     FONT_SIZE = 24

#     def __init__(self):
#         self.screen = turtle.Screen()
#         self.screen.title("Dungeon Crawl")
#         self.screen.bgcolor("black")
#         self.screen.setup(width=self.WIDTH, height=self.HEIGHT)

#         self.text_turtle = turtle.Turtle()
#         self.text_turtle.color("white")
#         self.text_turtle.hideturtle()
#         self.text_turtle.penup()

#     def text_animation(self, text):
#         self.text_turtle.clear()  # Clear previous text
#         # Starting position, adjust as needed
#         self.text_turtle.goto(-self.WIDTH/4, 0)

#         for i in range(len(text)):
#             self.text_turtle.clear()  # Clear previous text
#             self.text_turtle.write(
#                 text[:i+1], font=("Arial", self.FONT_SIZE, "normal"))
#             time.sleep(0.1)  # Adjust speed of animation if needed
#         time.sleep(1)

#     def run(self):
#         self.screen.mainloop()
