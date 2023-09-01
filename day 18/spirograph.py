import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0, 256)
    g=random.randint(0, 256)
    b=random.randint(0, 256)
    colour=(r, g, b)
    return colour


tim.speed("fastest")
def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)


draw_spirograph(8)
t.exitonclick()