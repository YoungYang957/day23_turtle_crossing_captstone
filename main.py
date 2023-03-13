import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True

screen.listen()
screen.onkey(player.move, "Up")
carmaneger = CarManager()
scoreboard = Scoreboard()
update = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    update +=1
    if update % 6 ==0:
        carmaneger.create_car()




    for car in carmaneger.all_cars:
        if car.distance(player) < 20 :
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()

    if player.is_finish():
        player.reset_pos()
        carmaneger.move_increase()
        scoreboard.increase_score()

    carmaneger.move_car()