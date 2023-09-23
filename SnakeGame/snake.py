from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "" 

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)
            
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("#00FF00")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake() 
        self.head=self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        if self.direction == "up":
            self.head.setheading(90)
            self.head.forward(move_distance)
        elif self.direction == "down":
            self.head.setheading(270)
            self.head.forward(move_distance)
        elif self.direction == "left":
            self.head.setheading(180)
            self.head.forward(move_distance)
        elif self.direction == "right":
            self.head.setheading(0)
            self.head.forward(move_distance)

    def up(self):
        if self.direction != "down": 
            self.direction = "up"

    def down(self):
        if self.direction != "up": 
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    def right(self):
        if self.direction != "left": 
            self.direction = "right"
