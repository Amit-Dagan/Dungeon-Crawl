import curses
from curses import wrapper
import time
from dungeon import EncounterRoom
from dice import *

class Screen:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.HEIGHT, self.WIDTH = self.stdscr.getmaxyx()

        # Print dimensions to help with debugging
        self.stdscr.addnstr(0, 0, f"Screen dimensions: HEIGHT={
                            self.HEIGHT}, WIDTH={self.WIDTH}", 50)
        self.stdscr.refresh()

        # Ensure the windows have valid dimensions
        main_window_height = max(1, self.HEIGHT // 3)
        main_window_width = max(1, self.WIDTH - 2)

        self.main_window = curses.newwin(
            main_window_height, main_window_width, 2, 1)
        self.main_window.box()  # Draw a border around the window
        self.main_window.addnstr(
            1, 1, "Main Window Initialized", main_window_width - 2)
        self.main_window.refresh()

        self.second_window = curses.newwin(
            main_window_height, main_window_width, main_window_height + 2, 1)
        self.second_window.box()  # Draw a border around the window
        self.second_window.addnstr(
            1, 1, "Main Window Initialized", main_window_width - 2)
        self.second_window.refresh()




    def write_main(self, text):
        self.main_window.clear()
        self.main_window.box()
        self.main_window.addstr(2, 1, text)
        self.main_window.refresh()

    def animation_write_main(self, text):
        self.main_window.clear()
        self.main_window.box()
        for i in range(len(text)):
            self.main_window.addstr(2, 1, text[:i+1])
            self.main_window.box()
            self.main_window.refresh()
            time.sleep(0.05)

    def write_second(self, text):
        self.second_window.clear()
        self.second_window.box()
        self.second_window.addstr(2, 1, text)
        self.second_window.refresh()

    def animation_write_second(self, text):
        self.second_window.clear()
        self.second_window.box()
        for i in range(len(text)):
            self.second_window.addstr(2, 1, text[:i+1])
            self.second_window.box()
            self.second_window.refresh()
            time.sleep(0.05)

    def choose(self, text, options):
        self.animation_write_main(text)
        s = ''
        for i, option in enumerate(options):
            s += f"{i} - {option} \n "
        res = []
        for i, option in enumerate(options):
            res.append(options[option])
        self.animation_write_second(s) 
        key = self.stdscr.getkey()
        while(int(key)>i):
            self.animation_write_main("please chose only from those options")
            key = self.stdscr.getkey()
        return res[i]

    def show_encounter(self, encounter: EncounterRoom):
        self.animation_write_main(encounter.info)
        s = ''

        for i, option in enumerate(encounter.options):
            s += f"{i} - to {option["text"]} ({option["type"]})\n "

        self.animation_write_second(s)
        key = self.stdscr.getkey()
        while (int(key) > i):
            self.animation_write_main("please chose only from those options")
            key = self.stdscr.getkey()
        return encounter.options[i]
        






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
