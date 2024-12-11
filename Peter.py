import turtle as t
import time

t.bgcolor("black")
t.color("white")

for i in range(3,0,-1):   
    t.teleport(0,-200)
    t.write(i,align="center",font=("Arial",250,"bold"))
    time.sleep(1)
    t.clear()

bright_colors = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Magenta",
    "Cyan",
    "Orange",
    "Purple",
    "Pink",
    "Lime Green"
]

for color in bright_colors:
    t.teleport(0,-50)
    t.pencolor(color)
    t.write("Happy Birthday!!!",align="center",font=("Arial",50,"bold"))
    time.sleep(0.1)

t.hideturtle()
t.done()