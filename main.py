from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    #Detect collisions with food 
    if snake.ssv[0].distance(food) < 16:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    #Detect collision with wall
    if snake.ssv[0].xcor() > 290 or snake.ssv[0].xcor() < -300 or snake.ssv[0].ycor() > 300 or snake.ssv[0].ycor() < -290:
        game_on = False
        
    #Detect collision with tail
    for x in snake.ssv[1:]:
        if snake.ssv[0].distance(x) < 16:
            game_on = False
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
scoreboard.gameover()

screen.exitonclick()