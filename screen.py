import time
import turtle

WIDTH = 800
HEIGHT = 600
FONT_SIZE = 24

screen = turtle.Screen()
screen.title("Dungeon Crawl")
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)

text_turtle = turtle.Turtle()
text_turtle.color("white")
text_turtle.hideturtle()
text_turtle.penup()


def text_animation(text):
    text_turtle.clear()  # Clear previous writings
    text_turtle.goto(-WIDTH/4, 0)  # Starting position, adjust as needed

    for i in range(len(text)):
        text_turtle.write(text[0:i], font=(
            "Arial", FONT_SIZE, "normal"))
        time.sleep(0.1)  # Adjust speed of animation if needed
    time.sleep(1)

text_turtle.goto(0, 0)
text_animation("Welcome to Dungeon Crawl!")
text_animation("Preper to Dieee")

screen.mainloop()


