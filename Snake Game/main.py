from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from scoreboard import Scoreboard


window = Screen()
window.setup(width=800, height=800)
window.title("Snake Game")
window.bgcolor("black")
window.tracer(0)


snake = Snake()
natural_food = Food(color="red")
magic_food = Food(color="orange")
magic_food.hideturtle()
score = Scoreboard()


red_food_count = 0
helper = 0
game_on = True

while game_on:
    snake.move()
    window.update()
    sleep(0.1 - min(0.09, (score.score - helper) * 0.005))
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")

    if snake.head.distance(natural_food) < 15:
        natural_food.appear()
        snake.extend()
        score.increase_score()
        red_food_count += 1
        if not magic_food.isvisible() and red_food_count % 3 == 0:
            magic_food.appear()
            magic_food.showturtle()
    
    if magic_food.isvisible() and snake.head.distance(magic_food) < 15:
        magic_food.hideturtle()
        snake.extend()
        score.increase_score()
        helper += 2

    if abs(snake.head.xcor()) > 370 or abs(snake.head.ycor()) > 370:
        game_on = False
        score.game_over()

    for segment in snake.turtles[:-1]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
            
window.exitonclick()
