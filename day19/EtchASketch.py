from turtle import Turtle, Screen

tim=Turtle()

tim.color("red")

screen=Screen()

def move_forwards():
    tim.forward(15)
def move_backwords():
    tim.backward(15)
def turn_right():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def turn_left():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwords)
screen.onkeypress(key="d", fun=turn_left)
screen.onkeypress(key="a", fun=turn_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()