from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race? Enter a color: ")
# print(user_bet)


red = Turtle()
red.penup()
red.shape("turtle")
red.color("red")
red.goto(-230, -100)

orange = Turtle()
orange.penup()
orange.shape("turtle")
orange.color("orange")
orange.goto(-230, -70)

yellow = Turtle()
yellow.penup()
yellow.shape("turtle")
yellow.color("yellow")
yellow.goto(-230, -40)

green = Turtle()
green.penup()
green.shape("turtle")
green.color("green")
green.goto(-230, -10)

blue = Turtle()
blue.penup()
blue.shape("turtle")
blue.color("blue")
blue.goto(-230, 20)

purple = Turtle()
purple.penup()
purple.shape("turtle")
purple.color("purple")
purple.goto(-230, 50)

all_turtle = [red, orange, yellow, green, blue, purple]

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False

    # random_distance = random.randint(0, 10)
    # turtle.forward(random_distance)

screen.exitonclick()