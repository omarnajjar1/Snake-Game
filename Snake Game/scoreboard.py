from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 350)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.home()
        self.write(f"Game Over \nFinal Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))