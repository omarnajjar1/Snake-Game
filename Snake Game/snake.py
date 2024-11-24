from turtle import Turtle 

class Snake:
    def __init__(self):
        self.turtles = []
        self.position = ((-20,0), (0,0), (20,0))
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        for i in range(len(self.position)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.turtles.append(new_turtle)
        
    def extend(self):
        new_turtles = Turtle("square")
        new_turtles.color("white")
        new_turtles.penup()
        new_turtles.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_turtles)

    def move(self):
        for i in range(len(self.turtles) -1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)