from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("lightblue")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define colors, shuffle them, and set up initial positions
colors = ["red", "orange", "green", "blue", "purple", "yellow"]
random.shuffle(colors)
y_positions = [-70, -40, -10, 20, 50, 80]


turtles = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(tim)


def move_forward():
    for turtle in turtles:
        turtle.forward(random.randint(0, 15))

while True:
    move_forward()
    winner = None
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.color()[0]
            break
    if winner:
        break

if user_bet:
    if user_bet.lower() == winner.lower():
        print(f"Congratulations! Your turtle ({user_bet}) won!")
    else:
        print(f"Sorry, your turtle ({user_bet}) didn't win. You lose!")
else:
    print("No bet placed.")

screen.exitonclick()
