from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # used to call the turtle classes' init method
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # length and width of turtle(food), default l and w is 20*20 ,
        self.color("blue")  # but we need it to be 10*10
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

