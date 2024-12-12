import turtle as t
import time

t.bgcolor("black")
t.color("white")
t.penup()
t.hideturtle()

t.teleport(0,0)
t.write("🤡", align= "center",font=("Arial",100,"bold") )
t.teleport(0,-200)
t.write("Do you wanna play a game?", align= "center",font=("Arial",25,"bold") )
time.sleep(2)
t.clear()

for i in range(3,0,-1): 
    t.teleport(0,-200)
    t.write(i,align="center",font=("Arial",250,"bold"))
    time.sleep(1)
    t.clear()

font_colors = [
    "Red",
    "Orange",
    "Dark Red",
    "Grey",
    "Orange",
    "Red",
    "Orange",
    "Grey",
    "Red",
    "Orange",
    "Grey",
    "White"
]

for color in font_colors:
    t.pencolor(color)
    t.teleport(0,0)
    t.write("👻🔪🎃",align="center",font=("Arial",100,"normal"))
    t.teleport(0,-50)
    t.write("Happy Birthday Peter!!!",align="center",font=("Arial",40,"bold"))
    t.teleport(300, -300)
    t.write("-From your favourites (Group 45/46)", align= "center",font=("Arial",15,"bold"))
    time.sleep(0.1)

t.done()