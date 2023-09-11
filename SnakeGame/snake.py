# snake.py

from turtle import Turtle

def create_segments():
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.color("pink")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)

    return segments
