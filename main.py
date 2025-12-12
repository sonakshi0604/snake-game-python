import time
from screen_setup import create_screen
from snake import Snake
from food import Food
from score import Scoreboard

def main():
    screen=create_screen()
    snake=Snake()
    food=Food()
    score=Scoreboard()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"right")

    game_is_on=True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food)<15:
            food.refresh()
            snake.extend()
            score.increase_score()

        x,y=snake.head.xcor(),snake.head.ycor()
        if x>290 or x<-290 or y>290 or y<-290:
            score.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                score.reset()
                snake.reset()

    screen.mainloop()

if __name__=="__main__":
    main()



