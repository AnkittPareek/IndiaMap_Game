from turtle import Turtle


class StateManager:
    def __init__(self):
        self.list_of_states = []

    def create_name(self):
        self.name = Turtle()
        self.list_of_states.append(self.name)

