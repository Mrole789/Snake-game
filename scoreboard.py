from turtle import Turtle
ALIGN = "center"
FONT = ('Courier',15,'normal') 

class Scoreboard(Turtle):
    """Creates scoreboard for keeping record of user progress"""
    def __init__(self):
        super().__init__()
        
        self.score = 0
        #Reads the previous highscore from the text file
        with open("highscore.txt",mode="r") as file:
            self.highscore = int(file.read())
        
        self.color('white')
        self.penup()
        self.goto(0,275)
        self.hideturtle()
        self.write_score()
     
    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.highscore}', False, align=ALIGN, font=FONT)
     
    def increase_score(self):
        self.score += 1
        self.write_score()

    def s_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        
        with open("highscore.txt",mode="w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.write_score()
    
#     def gameover(self):
#         self.goto(0,0)
#         self.color('red')
#         self.write('GAME OVER', False, align=ALIGN, font=FONT)
