from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard

def draw_wall():
    wall = Turtle()
    wall.speed(0)
    wall.color("white")
    wall.penup()
    wall.goto(-292, 292)
    wall.pendown()
    wall.pensize(3)

    for _ in range(4):
        wall.forward(580)
        wall.right(90)

    wall.hideturtle()

def setup_scoreboard():
    scoreboard = Scoreboard()
    scoreboard.penup()
    scoreboard.color("white")
    scoreboard.goto(0, 296)
    scoreboard.hideturtle()
    return scoreboard

screen = Screen()
screen.setup(width=655, height=655)
screen.bgcolor("#000000")
screen.title("My Snake Game")
screen.tracer(0)

draw_wall()

snake = Snake()
food = Food()
score = setup_scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        score.reset()
        snake.reset()
        
     
        
# Detect collision with tail.
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        score.reset()
        snake.reset()
    


screen.exitonclick()
