from turtle import Turtle
ALIGN = "center"
FONT = ('Courier',15,'normal') 

class Scoreboard(Turtle):
    """Creates scoreboard for keeping record of user progress"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,275)
        self.write(f'Score: {self.score}', False, align=ALIGN, font=FONT)
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', False, align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.color('red')
        self.write('GAME OVER', False, align=ALIGN, font=FONT)