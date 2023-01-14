from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def count_points(self):
        if self.r_score > self.l_score:
            self.goto(0, 0)
            self.write("Right Player Win the Game", align="center", font=("Courier", 30, "normal"))
        else:
            self.goto(0, 0)
            self.write("Left Player Win the Game", align="center", font=("Courier", 30, "normal"))


