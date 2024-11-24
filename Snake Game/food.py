from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self, shape="circle", color="red", size=0.5):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.shapesize(size)
        self.penup()
        self.appear()

    def appear(self):
        random_x = randint(-380, 380)
        random_y = randint(-360, 380)
        self.goto(random_x, random_y)