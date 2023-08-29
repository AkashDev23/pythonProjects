import turtle as t
import random

tim = t.Turtle()

tim.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]

random.shuffle(colors)

def drawShape(sides):
    tim.color(colors.pop())  
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for side in range(3, 11):
    drawShape(side)

t.exitonclick()
