import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen_height = 400
screen_width = 700

contes = 10
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
    turtle_list.append(new_turtle)

user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win? Enter color: ")


def random_speed():
    return random.randint(1, 10)


def race():
    while True:
        for turtle_ in turtle_list:
            if turtle_.xcor() >= screen_width / 2 - 20:
                return turtle_.pencolor()
            else:
                turtle_.forward(random_speed())


win_color = race()
if win_color == user_bet.lower():
    print("You won")
else:
    print(f"You lost, winning color is {win_color}")

screen.exitonclick()
