from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.speed("fastest")

    def update_scoreboard(self):
        """Docstring"""
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score {self.l_score}", align=ALIGMENT, font=(FONT, 24, "normal"))
        self.goto(100, 200)
        self.write(f"Score {self.r_score}", align=ALIGMENT, font=(FONT, 24, "normal"))

    def l_point(self):
        """Docstring"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Docstring"""
        self.r_score += 1
        self.update_scoreboard()