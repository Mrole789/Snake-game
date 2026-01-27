from turtle import Turtle
SD = 20 #Snake move distance
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Creates square turtles for snake body defines its movement."""
    def __init__(self):
        self.ssv = [] #ss_variants
        self.create_snake()
        
    def create_snake(self):
        s = 0 #steps -to be multiplied by -20 n moved behind previous ss
        for x in range(3):
            ss = Turtle() #ss = snake_square
            ss.shape("square")
            ss.color("white")
            ss.penup()
            ss.goto(-(20*s),0)
            self.ssv.append(ss)
            s = x + 1
            
    def extend(self):
        """add a new segment to the snake"""
        lsp = self.ssv[-1].position()
        ss2 = Turtle() #ss2 = other snake_squares created after snake eats food
        ss2.shape("square")
        ss2.color("white")
        ss2.penup()
        ss2.goto(lsp)
        self.ssv.append(ss2)
            
    def move(self):
        for x in range(len(self.ssv)-1,0,-1): #x - ss variant
            sscor = self.ssv[x-1].pos() #sscor - sscordinates x n y
            self.ssv[x].goto(sscor[0],sscor[1])
        self.ssv[0].forward(SD)
        
    def up(self):
        if self.ssv[0].heading() != DOWN:
            self.ssv[0].seth(UP)
        
    def down(self):
        if self.ssv[0].heading() != UP:
            self.ssv[0].seth(DOWN)
        
    def left(self):
        if self.ssv[0].heading() != RIGHT:
            self.ssv[0].seth(LEFT)
        
    def right(self):
        if self.ssv[0].heading() != LEFT:
            self.ssv[0].seth(RIGHT)
        