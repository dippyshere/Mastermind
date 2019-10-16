from graphics import*
import random
from turtle import*

win = GraphWin("My first window", 1600, 900)
win.setBackground('black')

order = random. randint(1,6)

display = order

setup()
t1 = Turtle()
t1.up()
colors = [ "red", "blue", "yellow", "green", "orange", "purple"]
t1.speed(0)

x1 = 25
y = 150
x2 = 75
x3 = 125
x4 = 175

circle_size = 15
circle_color = random.choice(colors)
      #first locatoion
t1.goto(x1, y)
t1.down()
t1.color(circle_color)
t1.begin_fill()
t1.circle(circle_size)
t1.end_fill()
t1. up

circle_color = random.choice(colors)
t1.goto(x2, y)
t1.down()
t1.color(circle_color)
t1.begin_fill()
t1.circle(circle_size)
t1.end_fill()
t1. up

circle_color = random.choice(colors)      
t1.goto(x3, y)
t1.down()
t1.color(circle_color)
t1.begin_fill()
t1.circle(circle_size)
t1.end_fill()
t1. up

circle_color = random.choice(colors) 
t1.goto(x4, y)
t1.down()
t1.color(circle_color)
t1.begin_fill()
t1.circle(circle_size)
t1.end_fill()
t1. up

