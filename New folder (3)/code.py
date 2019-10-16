from graphics import*
import random

width = 1280
eight = 720

#start screen
win = GraphWin("start screen", 1280,720)
win.setBackground(color_rgb(56,56,57))

img = Image(Point(640,360), "background.PNG")
img.draw(win)
#exit box instructions start screen
img = Image(Point(910,570), "exit box image.PNG")
img.draw(win)
#instructions button
img = Image(Point(370,570), "instructions.PNG")
img.draw(win)
#play button
img = Image(Point(640,295), "play.PNG")
img.draw(win)

colours = ['red', 'blue', 'yellow', 'green', 'orange',
         'purple']
 
rand_item1 = colours[random.randrange(len(colours))]

square = Rectangle(Point(200, 150), Point(600, 450))
square.setFill(rand_item1)
square.setOutline(rand_item1)
square.setWidth(5)
square.draw(win)

rand_item2 = colours[random.randrange(len(colours))]
square = Rectangle(Point(500, 150), Point(800, 450))
square.setFill(rand_item2)
square.setOutline(rand_item2)
square.setWidth(5)
square.draw(win)

while True:

        #window close
        click = win.getMouse()  
        x = click.getX()
        y = click.getY()

        if 768< x < 1057 and 535 < y < 605: 
                  win.close()
                  
#instructions window ( dont break)
        if 230 < x < 510 and 535 < y < 605:
                
              win2  = GraphWin("Instructions",600, 700)
              win2.setBackground(color_rgb(56,56,57))
              
        img = Image(Point(300,600), "exit box image.PNG")
        img.draw(win2)

        txt = Text(Point(300,200), "1. Beat mastermind you will have a different ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)

        txt = Text(Point(300,220), "number of lives depending on the difficulty ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)

        txt = Text(Point(300,240), "if you lose you lose a live ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)

        txt = Text(Point(300,280), "2. after you beat mastermind you will have to beat Hi-Lo ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)
        
        txt = Text(Point(300,320), "3. Once you beat Hi-Lo ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)
        
        txt = Text(Point(300,340), "click the open button to open the vault door ")
        txt.draw(win2)
        txt.setTextColor('white')
        txt.setFace('courier')
        txt.setSize(12)

 
        click = win2.getMouse()
        x = click.getX()
        y = click.getY()

        if 123 < x < 478and 557 < y < 643: 
                  win2.close()
                  
        click = win.getMouse()  
        x = click.getX()
        y = click.getY()
        
        if 0< x < 1280 and 0 < y < 400:
                break

