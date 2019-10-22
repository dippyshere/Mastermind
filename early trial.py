import random
from graphics import*
import time

win = GraphWin("My first window", 1280, 720)
win.setBackground('white')

colours = ['tomato', 'royalblue', 'gold', 'mediumseagreen', 'orange',
         'mediumpurple']
counter = 0
 #random colours
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

#what the user can select 
square = Rectangle(Point(50, 450), Point(100, 500))
square.setFill('tomato')
square.setOutline('tomato')
square.setWidth(5)
square.draw(win)


square = Rectangle(Point(150, 450), Point(200, 500))
square.setFill('royalblue')
square.setOutline('royalblue')
square.setWidth(5)
square.draw(win)


square = Rectangle(Point(250, 450), Point(300, 500))
square.setFill( 'gold')
square.setOutline( 'gold')
square.setWidth(5)
square.draw(win)


square = Rectangle(Point(350, 450), Point(400, 500))
square.setFill('mediumseagreen')
square.setOutline('mediumseagreen')
square.setWidth(5)
square.draw(win)

square = Rectangle(Point(450, 450), Point(500, 500))
square.setFill('orange')
square.setOutline('orange')
square.setWidth(5)
square.draw(win)


square = Rectangle(Point(550, 450), Point(600, 500))
square.setFill('mediumpurple')
square.setOutline('mediumpurple')
square.setWidth(5)
square.draw(win)

#what the user chose
square1 = Rectangle(Point(250, 550), Point(300, 600))
square1.setFill( 'white')
square1.setOutline( 'black')
square1.setWidth(5)
square1.draw(win)


square2 = Rectangle(Point(350, 550), Point(400, 600))
square2.setFill('white')
square2.setOutline('black')
square2.setWidth(5)
square2.draw(win)

square3 = Rectangle(Point(450, 550), Point(500, 600))
square3.setFill('white')
square3.setOutline('black')
square3.setWidth(5)
square3.draw(win)


square4 = Rectangle(Point(550, 550), Point(600, 600))
square4.setFill('white')
square4.setOutline('black')
square4.setWidth(5)
square4.draw(win)

square9 = Rectangle(Point(250, 650), Point(300, 700))
square9.setFill( 'white')
square9.setOutline( 'black')
square9.setWidth(5)
square9.draw(win)


square10 = Rectangle(Point(350, 650), Point(400, 700))
square10.setFill('white')
square10.setOutline('black')
square10.setWidth(5)
square10.draw(win)

square11 = Rectangle(Point(450, 650), Point(500, 700))
square11.setFill('white')
square11.setOutline('black')
square11.setWidth(5)
square11.draw(win)


square12 = Rectangle(Point(550, 650), Point(600, 700))
square12.setFill('white')
square12.setOutline('black')
square12.setWidth(5)
square12.draw(win)
#right or wrong box
square5 = Rectangle(Point(50, 250), Point(100, 200))
square5.setFill( 'gray')
square5.setOutline( 'black')
square5.setWidth(5)
square5.draw(win)

square6 = Rectangle(Point(150, 250), Point(200, 200))
square6.setFill('gray')
square6.setOutline('black')
square6.setWidth(5)
square6.draw(win)

square7 = Rectangle(Point(250, 250), Point(300, 200))
square7.setFill('gray')
square7.setOutline('black')
square7.setWidth(5)
square7.draw(win)

square8 = Rectangle(Point(350, 250), Point(400, 200))
square8.setFill('gray')
square8.setOutline('black')
square8.setWidth(5)
square8.draw(win)

square1colour = ''
square2colour = ''
square3colour = ''
square4colour = ''
square9colour = ''
square10colour = ''
square11colour = ''
square12colour = ''
while True:
          while True:
                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square1.setFill('tomato')
                              square1colour = 'tomato'

                    if 150 < x < 200 and 450 < y < 500: 
                              square1.setFill('royalblue')
                              square1colour = 'royalblue'

                    if 250 < x < 300 and 450 < y < 500: 
                              square1.setFill('gold')
                              square1colour = 'gold'

                    if 350 < x < 400 and 450 < y < 500: 
                              square1.setFill('mediumseagreen')
                              square1colour = 'mediumseagreen'

                    if 450 < x < 500 and 450 < y < 500: 
                              square1.setFill('orange')
                              square1colour = 'orange'

                    if 550 < x < 600 and 450 < y < 500: 
                              square1.setFill('mediumpurple')
                              square1colour = 'mediumpurple'

                    if 50 < x < 600 and 450 < y < 500: 
                              break
          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square2.setFill('tomato')
                              square3colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500:  
                              square2.setFill('royalblue')
                              square2colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square2.setFill('gold')
                              square2colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square2.setFill('mediumseagreen')
                              square2colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square2.setFill('orange')
                              square2colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500: 
                              square2.setFill('mediumpurple')
                              square2colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break

          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square3.setFill('tomato')
                              square3colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500: 
                              square3.setFill('royalblue')
                              square3colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square3.setFill('gold')
                              square3colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square3.setFill('mediumseagreen')
                              square3colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square3.setFill('orange')
                              square3colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500: 
                              square3.setFill('mediumpurple')
                              square3colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break
          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square4.setFill('tomato')
                              square4colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500: 
                              square4.setFill('royalblue')
                              square4colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square4.setFill('gold')
                              square4colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square4.setFill('mediumseagreen')
                              square4colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square4.setFill('orange')
                              square4colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500:  
                              square4.setFill('mediumpurple')
                              square4colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break
                        #right wrong for first thing
          if rand_item1 == square1colour    :
                    counter += 1
                    square5.setFill('black')

          if rand_item2 == square2colour:
                    counter += 1
                    square6.setFill('black')

          if rand_item3 == square3colour:
                    counter += 1
                    square7.setFill('black')

          if rand_item4 == square4colour:
                    counter += 1
                    square8.setFill('black')

          if counter == 4:
                    txt = Text(Point(325,200),'You guessed the code')
                    txt.draw(win)
                    txt.setTextColor('black')
                    txt.setFace('courier')
                    txt.setSize(50)

          else:
                  time.sleep(1)
                  counter = counter - counter
                  square5.setFill('gray')
                  square6.setFill('gray')
                  square7.setFill('gray')
                  square8.setFill('gray')                  
          while True:
                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square9.setFill('tomato')
                              square9colour = 'tomato'

                    if 150 < x < 200 and 450 < y < 500: 
                              square9.setFill('royalblue')
                              square9colour = 'royalblue'

                    if 250 < x < 300 and 450 < y < 500: 
                              square9.setFill('gold')
                              square9colour = 'gold'

                    if 350 < x < 400 and 450 < y < 500: 
                              square9.setFill('mediumseagreen')
                              square9colour = 'mediumseagreen'

                    if 450 < x < 500 and 450 < y < 500: 
                              square9.setFill('orange')
                              square9colour = 'orange'

                    if 550 < x < 600 and 450 < y < 500: 
                              square9.setFill('mediumpurple')
                              square9colour = 'mediumpurple'

                    if 50 < x < 600 and 450 < y < 500: 
                              break
          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square10.setFill('tomato')
                              square10colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500:  
                              square10.setFill('royalblue')
                              square10colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square10.setFill('gold')
                              square10colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square10.setFill('mediumseagreen')
                              square10colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square10.setFill('orange')
                              square10colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500: 
                              square10.setFill('mediumpurple')
                              square10colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break

          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square11.setFill('tomato')
                              square11colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500: 
                              square11.setFill('royalblue')
                              square11colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square11.setFill('gold')
                              square11colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square11.setFill('mediumseagreen')
                              square11colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square11.setFill('orange')
                              square11colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500: 
                              square11.setFill('mediumpurple')
                              square11colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break
          while True:

                    click = win.getMouse()  
                    x = click.getX()
                    y = click.getY()
                  
                    if 50 < x < 100 and 450 < y < 500: 
                              square12.setFill('tomato')
                              square12colour = 'tomato'
                    if 150 < x < 200 and 450 < y < 500: 
                              square12.setFill('royalblue')
                              square12colour = 'royalblue'
                    if 250 < x < 300 and 450 < y < 500: 
                              square12.setFill('gold')
                              square12colour = 'gold'
                    if 350 < x < 400 and 450 < y < 500: 
                              square12.setFill('mediumseagreen')
                              square12colour = 'mediumseagreen'
                    if 450 < x < 500 and 450 < y < 500: 
                              square12.setFill('orange')
                              square12colour = 'orange'
                    if 550 < x < 600 and 450 < y < 500:  
                              square12.setFill('mediumpurple')
                              square12colour = 'mediumpurple'
                    if 50 < x < 600 and 450 < y < 500: 
                              break

          if rand_item1 == square9colour    :
                    counter += 1
                    square5.setFill('black')

          if rand_item2 == square10colour:
                    counter += 1
                    square6.setFill('black')

          if rand_item3 == square11colour:
                    counter += 1
                    square7.setFill('black')

          if rand_item4 == square12colour:
                    counter += 1
                    square8.setFill('black')

          if counter == 4:
                    txt = Text(Point(325,200),'You guessed the code')
                    txt.draw(win)
                    txt.setTextColor('black')
                    txt.setFace('courier')
                    txt.setSize(50)

          else:
                  pass

          break
          #reset incorrect squares

#Win screen / message

