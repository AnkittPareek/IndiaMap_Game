"""Rename this file to main.py if you want to collect data in data csv again.
If you don't intend to change data , don't touch this file."""

import turtle
import pandas
from turtle import Turtle
from turtle import Screen

screen = Screen()
states = ["Ladakh", "Jammu & Kashmir", "himachal pradesh", "Uttarakhand", "Punjab"
    , "Haryana", "Delhi", "Sikkim", "Arunachal Pradesh", "Assam"
    , "Meghalaya", "Nagaland", "Manipur", "Mizoram", "Tripura", "Rajasthan"
    , "Uttar Pradesh", "Bihar", "Gujarat", "Madhya Pradesh", "Jharkhand"
    , "West Bengal", "Goa", "Maharashtra", "Chattisgarh", "odisha", "Telangana"
    , "Karnataka", "Andhra Pradesh", "Tamil Nadu", "Kerala"]

data = {"name": [],
        "xcor": [],
        "ycor": [],
        }

image = "map.gif"
screen.addshape(image)
turtle.shape(image)

val = 0

print(states[0])


def getcoor(x, y):
    global val
    if val == 31:
        data_csv = pandas.DataFrame(data)
        print(data_csv)
        data_csv.to_csv("data.csv")
        exit()
    if val < len(states) - 1:
        print(states[val + 1])
    data["name"].append(states[val])
    data["xcor"].append(x)
    data["ycor"].append(y)
    val += 1


def inc_val():
    global val
    val += 1


screen.onscreenclick(getcoor)

# data_csv = pandas.DataFrame(data)
# print(data_csv)

# print(data)
screen.mainloop()
