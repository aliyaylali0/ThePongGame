from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player_1.up, 'w')
screen.onkey(player_1.down, 's')
screen.onkey(player_2.up, 'Up')
screen.onkey(player_2.down, 'Down')

ball = Ball()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() > 330 or ball.distance(player_1) < 50 and ball.xcor() > -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

screen.exitonclick()
