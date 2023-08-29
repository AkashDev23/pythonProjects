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

def randomWalk():
    walk = ["left", "right", "forward", "backward"]
    while True:
        choice = random.choice(walk)
        if choice == "left":
            tim.left(90)
        elif choice == "right":
            tim.right(90)
        elif choice == "forward":
            tim.forward(50)
        else:
            tim.backward(50)
        
        if t.onkey(lambda: exit(), "Escape"):
            break
        
# Listen for keyboard events
t.listen()

# Call the randomWalk() function
randomWalk()

t.exitonclick()
