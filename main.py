import turtle

import pandas
from turtle import Turtle
from turtle import Screen

screen = Screen()
image = "map.gif"
screen.title("Name The States.")
screen.addshape(image)
turtle.shape(image)
score = []
data = pandas.read_csv("data.csv")

print(data["name"])
statemanager = Turtle()
statemanager.hideturtle()
statemanager.penup()

while not len(score) == 31:
    new_name = True
    guess = screen.textinput(f"{len(score)}/31 States Correct.", "Whats another state name?").lower()
    for item in score:
        if guess == item:
            new_name = False
    if new_name:
        for item in data.name:
            if item.lower() == guess:
                score.append(guess)
                state_row = data[data.name == item]
                newx= float(state_row.xcor)
                newy = float(state_row.ycor)
                statemanager.goto(newx, newy)
                statemanager.write(guess,font=("Courier", 8, "normal"), align="center")

statemanager.color("blue")
statemanager.home()
statemanager.write("Cogratulations!! You Won..",font=("Arial", 35, "normal"), align="center")

screen.exitonclick()
