import random
from graphics import*

win = GraphWin("My first window", 1280, 720)
win.setBackground('white')

colours = ['red', 'blue', 'yellow', 'green', 'orange',
         'purple']
 
rand_item1 = colours[random.randrange(len(colours))]

square = Rectangle(Point(50, 350), Point(100, 400))
square.setFill(rand_item1)
square.setOutline(rand_item1)
square.setWidth(5)
square.draw(win)

rand_item2 = colours[random.randrange(len(colours))]
square = Rectangle(Point(150, 350), Point(200, 400))
square.setFill(rand_item2)
square.setOutline(rand_item2)
square.setWidth(5)
square.draw(win)

rand_item3 = colours[random.randrange(len(colours))]
square = Rectangle(Point(250, 350), Point(300, 400))
square.setFill(rand_item3)
square.setOutline(rand_item3)
square.setWidth(5)
square.draw(win)

rand_item4 = colours[random.randrange(len(colours))]
square = Rectangle(Point(350, 350), Point(400, 400))
square.setFill(rand_item4)
square.setOutline(rand_item4)
square.setWidth(5)
square.draw(win)

