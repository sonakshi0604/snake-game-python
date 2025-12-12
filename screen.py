from turtle import Screen

def create_screen():
    screen = Screen()
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)  
    return screen