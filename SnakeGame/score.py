from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260) 

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 18, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
