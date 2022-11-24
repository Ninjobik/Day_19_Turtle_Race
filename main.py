import turtle
from turtle import Turtle, Screen

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen_height = 300
screen_width = 500

contes = 6
places = []


def setup_screen(width, height):
    turtle.setup(width, height)
    for i in range(contes):
        y_distance = (height / 2) / contes
        initial_y = contes / 2 * y_distance
        place = (0 - (width / 2) + 20, initial_y - (y_distance * i))
        places.append(place)


setup_screen(screen_width, screen_height)
turtle_list = []

for n in range(contes):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[n % 6])
    new_turtle.goto(places[n])

user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win? Enter color: ")
print(user_bet)



















screen.exitonclick()