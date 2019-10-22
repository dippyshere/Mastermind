from graphics import*
import random

width = 1280
height = 720

colours = ['tomato', 'royalblue', 'gold', 'mediumseagreen', 'orange',
         'mediumpurple']
counter = 0
#easter egg
special = random.randint(1,100)

#start screen

win = GraphWin("start screen", 1280,720)
win.setBackground(color_rgb(56,56,57))
def main():
        
        #background
        img1 = Image(Point(640,360), "background.PNG")
        img1.draw(win)
        #exit box instructions start screen
        img2 = Image(Point(910,570), "exit box image.PNG")
        img2.draw(win)
        #instructions button
        img3 = Image(Point(370,570), "instructions.PNG")
        img3.draw(win)
        #play button
        img4 = Image(Point(640,295), "play.PNG")
        img4.draw(win)
        #title
        title = Image(Point(640,150), "Title.PNG")
        title.draw(win)
        
        def check(x,y):
                if 230 < x < 510 and 535 < y < 605: 
                        _win2  = GraphWin("Instructions",600, 700)
                        _win2.setBackground(color_rgb(56,56,57))
                        return True
                else:
                        return False

        while True:

                #window close
                click = win.getMouse()  
                x = click.getX()
                y = click.getY()
                
                if 768< x < 1057 and 535 < y < 605: 
                          win.close()
                        
                elif 230 < x < 510 and 535 < y < 605: 
                        _win2  = GraphWin("Instructions",600, 700)
                        _win2.setBackground(color_rgb(56,56,57))
                          
        #instructions window
                elif 230 < x < 510 and 535 < y < 605:
                        
                        _win2  = GraphWin("Instructions",600, 700)
                        _win2.setBackground(color_rgb(56,56,57))
                elif 375 < x < 850 and 260 < y < 330:
                        for i in win.items[:]:
                                i.undraw()
                        neg()
                        break
                else:
                        continue

                        
                      
                img = Image(Point(300,600), "exit box image.PNG")
                img.draw(_win2)

                txt = Text(Point(300,275), "1. You have to play a modified version \n of mastermind nand to win you will have \n to guess the secret code. \n\n2. To play mastermind you have to guess a colour code \nthat has been randomly picked from 6 colour \nthe colours can repeat. \n\n3. The modifications to this version \nare that it is easier nto figure out the code as the \nblack or white indicators do not fill up in orden instead \nthey fill up according to which colour was right \nfor example if the third guess is right \nthen the third box will fill.. \n\n4.If the user guess a colour that has been generated \nmore than once than the indicators will show as \nwhite even if it is in the right spot \nthis  is a bug in the game.\n\n 5. Finally if the player wins or losses \nthen they will be greeted with either \na win screen or a game over screen\n\n5. finally exit this page using the \nexit button in the window as the game \nwill not work if you dont.")
                txt.draw(_win2)
                txt.setTextColor('white')
                txt.setFace('courier')
                txt.setSize(12)

         
                click = _win2.getMouse()
                x = click.getX()
                y = click.getY()
                v = False
                while v != True:
                        if 123 < x < 478and 557 < y < 643: 
                                _win2.close()
                                v = True
                        else:
                                click = _win2.getMouse()
                                x = click.getX()
                                y = click.getY()
                                continue
def neg():

        colours = ['tomato', 'royalblue', 'gold', 'mediumseagreen', 'orange',
                 'mediumpurple']
        counter = 0
        img1 = Image(Point(640,360), "game annotated sketch.PNG")
        img1.draw(win)
        #randomly generated colours
        #hidden of screen
        rand_item1 = colours[random.randrange(len(colours))]
        square = Rectangle(Point(50, 1550), Point(100, 1600))
        square.setFill(rand_item1)
        square.setOutline(rand_item1)
        square.setWidth(5)
        square.draw(win)

        rand_item2 = colours[random.randrange(len(colours))]
        square = Rectangle(Point(150, 1550), Point(200, 1600))
        square.setFill(rand_item2)
        square.setOutline(rand_item2)
        square.setWidth(5)
        square.draw(win)

        rand_item3 = colours[random.randrange(len(colours))]
        square = Rectangle(Point(250, 1550), Point(300, 1600))
        square.setFill(rand_item3)
        square.setOutline(rand_item3)
        square.setWidth(5)
        square.draw(win)

        rand_item4 = colours[random.randrange(len(colours))]
        square = Rectangle(Point(350, 1550), Point(400,1600))
        square.setFill(rand_item4)
        square.setOutline(rand_item4)
        square.setWidth(5)
        square.draw(win)

        #what the user can select 
        square = Rectangle(Point(708, 555), Point(752, 510))
        square.setFill('tomato')
        square.setOutline('tomato')
        square.setWidth(5)
        square.draw(win)


        square = Rectangle(Point(775, 555), Point(820, 510))
        square.setFill('royalblue')
        square.setOutline('royalblue')
        square.setWidth(5)
        square.draw(win)


        square = Rectangle(Point(840, 555), Point(884, 510))
        square.setFill( 'gold')
        square.setOutline( 'gold')
        square.setWidth(5)
        square.draw(win)


        square = Rectangle(Point(906, 555), Point(950, 510))
        square.setFill('mediumseagreen')
        square.setOutline('mediumseagreen')
        square.setWidth(5)
        square.draw(win)

        square = Rectangle(Point(971, 555), Point(1015, 510))
        square.setFill('orange')
        square.setOutline('orange')
        square.setWidth(5)
        square.draw(win)


        square = Rectangle(Point(1038, 555), Point(1082, 510))
        square.setFill('mediumpurple')
        square.setOutline('mediumpurple')
        square.setWidth(5)
        square.draw(win)

        #what the user chose
        #1st set
        square33 = Rectangle(Point(313, 71), Point(357, 115))
        square33.setFill( 'gray')
        square33.setOutline( 'black')
        square33.setWidth(1)
        square33.draw(win)


        square34 = Rectangle(Point(380, 71), Point(424, 115))
        square34.setFill('gray')
        square34.setOutline('black')
        square34.setWidth(1)
        square34.draw(win)

        square35 = Rectangle(Point(444, 71), Point(489, 115))
        square35.setFill('gray')
        square35.setOutline('black')
        square35.setWidth(1)
        square35.draw(win)


        square36 = Rectangle(Point(512, 71), Point(556, 115))
        square36.setFill('gray')
        square36.setOutline('black')
        square36.setWidth(1)
        square36.draw(win)

#2nd set
        square37 = Rectangle(Point(313, 148), Point(357, 193))
        square37.setFill( 'gray')
        square37.setOutline( 'black')
        square37.setWidth(1)
        square37.draw(win)


        square38 = Rectangle(Point(380, 148), Point(424, 193))
        square38.setFill('gray')
        square38.setOutline('black')
        square38.setWidth(1)
        square38.draw(win)

        square39 = Rectangle(Point(444, 148), Point(489, 193))
        square39.setFill('gray')
        square39.setOutline('black')
        square39.setWidth(1)
        square39.draw(win)


        square40 = Rectangle(Point(512, 148), Point(556, 193))
        square40.setFill('gray')
        square40.setOutline('black')
        square40.setWidth(1)
        square40.draw(win)

#3rd set
        square41 = Rectangle(Point(313, 225), Point(357, 270))
        square41.setFill( 'gray')
        square41.setOutline( 'black')
        square41.setWidth(1)
        square41.draw(win)

        square42 = Rectangle(Point(380, 225), Point(424, 270))
        square42.setFill('gray')
        square42.setOutline('black')
        square42.setWidth(1)
        square42.draw(win)

        square43 = Rectangle(Point(446, 225), Point(490, 270))
        square43.setFill('gray')
        square43.setOutline('black')
        square43.setWidth(1)
        square43.draw(win)


        square44 = Rectangle(Point(513, 225), Point(556, 270))
        square44.setFill('gray')
        square44.setOutline('black')
        square44.setWidth(1)
        square44.draw(win)

#4th set
        square45 = Rectangle(Point(313, 303), Point(357, 348))
        square45.setFill( 'gray')
        square45.setOutline( 'black')
        square45.setWidth(1)
        square45.draw(win)

        square46 = Rectangle(Point(380, 303), Point(424, 348))
        square46.setFill('gray')
        square46.setOutline('black')
        square46.setWidth(1)
        square46.draw(win)

        square47 = Rectangle(Point(446, 303), Point(490, 348))
        square47.setFill('gray')
        square47.setOutline('black')
        square47.setWidth(1)
        square47.draw(win)


        square48 = Rectangle(Point(513, 303), Point(556, 348))
        square48.setFill('gray')
        square48.setOutline('black')
        square48.setWidth(1)
        square48.draw(win)

#5th set
        square49 = Rectangle(Point(313, 381), Point(357, 425))
        square49.setFill( 'gray')
        square49.setOutline( 'black')
        square49.setWidth(1)
        square49.draw(win)

        square50 = Rectangle(Point(380, 381), Point(424, 425))
        square50.setFill('gray')
        square50.setOutline('black')
        square50.setWidth(1)
        square50.draw(win)

        square51 = Rectangle(Point(446, 381), Point(490, 425))
        square51.setFill('gray')
        square51.setOutline('black')
        square51.setWidth(1)
        square51.draw(win)


        square52 = Rectangle(Point(513, 381), Point(556, 425))
        square52.setFill('gray')
        square52.setOutline('black')
        square52.setWidth(1)
        square52.draw(win)

#6th set
        square53 = Rectangle(Point(313, 458), Point(357, 502))
        square53.setFill( 'gray')
        square53.setOutline( 'black')
        square53.setWidth(1)
        square53.draw(win)

        square54 = Rectangle(Point(380, 458), Point(424, 502))
        square54.setFill('gray')
        square54.setOutline('black')
        square54.setWidth(1)
        square54.draw(win)

        square55 = Rectangle(Point(446, 458), Point(490, 502))
        square55.setFill('gray')
        square55.setOutline('black')
        square55.setWidth(1)
        square55.draw(win)

        square56 = Rectangle(Point(513, 458), Point(556, 502))
        square56.setFill('gray')
        square56.setOutline('black')
        square56.setWidth(1)
        square56.draw(win)

#7th set
        square57 = Rectangle(Point(313, 536), Point(357, 580))
        square57.setFill( 'gray')
        square57.setOutline( 'black')
        square57.setWidth(1)
        square57.draw(win)

        square58 = Rectangle(Point(380, 536), Point(424, 580))
        square58.setFill('gray')
        square58.setOutline('black')
        square58.setWidth(1)
        square58.draw(win)

        square59 = Rectangle(Point(446, 536), Point(490, 580))
        square59.setFill('gray')
        square59.setOutline('black')
        square59.setWidth(1)
        square59.draw(win)

        square60 = Rectangle(Point(513, 536), Point(556, 580))
        square60.setFill('gray')
        square60.setOutline('black')
        square60.setWidth(1)
        square60.draw(win)

#8th set
        square61 = Rectangle(Point(313, 613), Point(357, 657))
        square61.setFill( 'gray')
        square61.setOutline( 'black')
        square61.setWidth(1)
        square61.draw(win)

        square62 = Rectangle(Point(380, 613), Point(424, 657))
        square62.setFill('gray')
        square62.setOutline('black')
        square62.setWidth(1)
        square62.draw(win)

        square63 = Rectangle(Point(446, 613), Point(490, 657))
        square63.setFill('gray')
        square63.setOutline('black')
        square63.setWidth(1)
        square63.draw(win)

        square64 = Rectangle(Point(513, 613), Point(556, 657))
        square64.setFill('gray')
        square64.setOutline('black')
        square64.setWidth(1)
        square64.draw(win)
        #right or wrong box( black and white indicators)
        #1st set
        square1 = Rectangle(Point(239, 71), Point(260, 92))
        square1.setFill( 'gray')
        square1.setOutline( 'black')
        square1.setWidth(1)
        square1.draw(win)

        square2 = Rectangle(Point(263, 71), Point(283, 92))
        square2.setFill('gray')
        square2.setOutline('black')
        square2.setWidth(1)
        square2.draw(win)

        square3 = Rectangle(Point(239, 95), Point(260, 115))
        square3.setFill('gray')
        square3.setOutline('black')
        square3.setWidth(1)
        square3.draw(win)

        square4 = Rectangle(Point(263, 95), Point(283, 115))
        square4.setFill('gray')
        square4.setOutline('black')
        square4.setWidth(1)
        square4.draw(win)

#2nd set
        square5 = Rectangle(Point(239, 148), Point(260, 169))
        square5.setFill( 'gray')
        square5.setOutline( 'black')
        square5.setWidth(1)
        square5.draw(win)

        square6 = Rectangle(Point(263, 148), Point(283, 169))
        square6.setFill('gray')
        square6.setOutline('black')
        square6.setWidth(1)
        square6.draw(win)

        square7 = Rectangle(Point(239, 172), Point(260, 193))
        square7.setFill('gray')
        square7.setOutline('black')
        square7.setWidth(1)
        square7.draw(win)

        square8 = Rectangle(Point(263, 172), Point(283, 193))
        square8.setFill('gray')
        square8.setOutline('black')
        square8.setWidth(1)
        square8.draw(win)

#3rd set
        square9 = Rectangle(Point(239, 225), Point(260, 247))
        square9.setFill( 'gray')
        square9.setOutline( 'black')
        square9.setWidth(1)
        square9.draw(win)

        square10 = Rectangle(Point(263, 225), Point(283, 247))
        square10.setFill('gray')
        square10.setOutline('black')
        square10.setWidth(1)
        square10.draw(win)

        square11 = Rectangle(Point(239, 250), Point(260, 270))
        square11.setFill('gray')
        square11.setOutline('black')
        square11.setWidth(1)
        square11.draw(win)

        square12 = Rectangle(Point(263, 250), Point(283, 270))
        square12.setFill('gray')
        square12.setOutline('black')
        square12.setWidth(1)
        square12.draw(win)

#4th set
        square13 = Rectangle(Point(239, 303), Point(260, 324))
        square13.setFill( 'gray')
        square13.setOutline( 'black')
        square13.setWidth(1)
        square13.draw(win)

        square14 = Rectangle(Point(263, 303), Point(283, 324))
        square14.setFill('gray')
        square14.setOutline('black')
        square14.setWidth(1)
        square14.draw(win)

        square15 = Rectangle(Point(239, 327), Point(260, 348))
        square15.setFill('gray')
        square15.setOutline('black')
        square15.setWidth(1)
        square15.draw(win)

        square16 = Rectangle(Point(263, 327), Point(283, 348))
        square16.setFill('gray')
        square16.setOutline('black')
        square16.setWidth(1)
        square16.draw(win)

#5th set
        square17 = Rectangle(Point(239, 381), Point(260, 401))
        square17.setFill( 'gray')
        square17.setOutline( 'black')
        square17.setWidth(1)
        square17.draw(win)

        square18 = Rectangle(Point(263, 381), Point(283, 401))
        square18.setFill('gray')
        square18.setOutline('black')
        square18.setWidth(1)
        square18.draw(win)

        square19 = Rectangle(Point(239, 404), Point(260, 424))
        square19.setFill('gray')
        square19.setOutline('black')
        square19.setWidth(1)
        square19.draw(win)

        square20 = Rectangle(Point(263, 404), Point(283, 424))
        square20.setFill('gray')
        square20.setOutline('black')
        square20.setWidth(1)
        square20.draw(win)

#6th set
        square21 = Rectangle(Point(239, 458), Point(260, 478))
        square21.setFill( 'gray')
        square21.setOutline( 'black')
        square21.setWidth(1)
        square21.draw(win)

        square22 = Rectangle(Point(263, 458), Point(283, 478))
        square22.setFill('gray')
        square22.setOutline('black')
        square22.setWidth(1)
        square22.draw(win)

        square23 = Rectangle(Point(239, 481), Point(260, 502))
        square23.setFill('gray')
        square23.setOutline('black')
        square23.setWidth(1)
        square23.draw(win)

        square24 = Rectangle(Point(263, 481), Point(283, 502))
        square24.setFill('gray')
        square24.setOutline('black')
        square24.setWidth(1)
        square24.draw(win)

#7th set
        square25 = Rectangle(Point(239, 536), Point(260, 556))
        square25.setFill( 'gray')
        square25.setOutline( 'black')
        square25.setWidth(1)
        square25.draw(win)

        square26 = Rectangle(Point(263, 536), Point(283, 556))
        square26.setFill('gray')
        square26.setOutline('black')
        square26.setWidth(1)
        square26.draw(win)

        square27 = Rectangle(Point(239, 559), Point(260, 580))
        square27.setFill('gray')
        square27.setOutline('black')
        square27.setWidth(1)
        square27.draw(win)

        square28 = Rectangle(Point(263, 559), Point(283, 580))
        square28.setFill('gray')
        square28.setOutline('black')
        square28.setWidth(1)
        square28.draw(win)

#8th set
        square29 = Rectangle(Point(239, 613), Point(260, 633))
        square29.setFill( 'gray')
        square29.setOutline( 'black')
        square29.setWidth(1)
        square29.draw(win)

        square30 = Rectangle(Point(263, 613), Point(283, 633))
        square30.setFill('gray')
        square30.setOutline('black')
        square30.setWidth(1)
        square30.draw(win)

        square31 = Rectangle(Point(239, 636), Point(260, 657))
        square31.setFill('gray')
        square31.setOutline('black')
        square31.setWidth(1)
        square31.draw(win)

        square32 = Rectangle(Point(263, 636), Point(283, 657))
        square32.setFill('gray')
        square32.setOutline('black')
        square32.setWidth(1)
        square32.draw(win)
        
        square33colour = ''
        square34colour = ''
        square35colour = ''
        square36colour = ''
        square37colour = ''
        square38colour = ''
        square39colour = ''
        square40colour = ''
        square41colour = ''
        square42colour = ''
        square43colour = ''
        square44colour = ''
        square45colour = ''
        square46colour = ''
        square47colour = ''
        square48colour = ''
        square49colour = ''
        square50colour = ''
        square51colour = ''
        square52colour = ''
        square53colour = ''
        square54colour = ''
        square55colour = ''
        square56colour = ''
        square57colour = ''
        square58colour = ''
        square59colour = ''
        square60colour = ''
        square61colour = ''
        square62colour = ''
        square63colour = ''
        square64colour = ''
#check user guess and generated code
        while True:
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square33.setFill('tomato')
                                      square33colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555: 
                                      square33.setFill('royalblue')
                                      square33colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square33.setFill('gold')
                                      square33colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square33.setFill('mediumseagreen')
                                      square33colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square33.setFill('orange')
                                      square33colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square33.setFill('mediumpurple')
                                      square33colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square34.setFill('tomato')
                                      square34colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square34.setFill('royalblue')
                                      square34colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square34.setFill('gold')
                                      square34colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square34.setFill('mediumseagreen')
                                      square34colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square34.setFill('orange')
                                      square34colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square34.setFill('mediumpurple')
                                      square34colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square35.setFill('tomato')
                                      square35colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square35.setFill('royalblue')
                                      square35colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square35.setFill('gold')
                                      square35colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square35.setFill('mediumseagreen')
                                      square35colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square35.setFill('orange')
                                      square35colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square35.setFill('mediumpurple')
                                      square35colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square36.setFill('tomato')
                                      square36colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square36.setFill('royalblue')
                                      square36colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square36.setFill('gold')
                                      square36colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square36.setFill('mediumseagreen')
                                      square36colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square36.setFill('orange')
                                      square36colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square36.setFill('mediumpurple')
                                      square36colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break


                  if rand_item1 == square33colour    :
                        counter += 1
                        square1.setFill('black')
                                
                  elif rand_item1 == square34colour    :
                        square1.setFill('white')

                  elif rand_item1 == square35colour    :
                        square1.setFill('white')

                  elif rand_item1 == square36colour    :
                        square1.setFill('white')

                            
                  if rand_item2 == square34colour:
                        counter += 1
                        square2.setFill('black')

                  elif rand_item2 == square33colour    :
                        square2.setFill('white')

                  elif rand_item2 == square35colour    :
                        square2.setFill('white')
                            
                  elif rand_item2 == square36colour    :
                        square2.setFill('white')


                  if rand_item3 == square35colour:
                        counter += 1
                        square3.setFill('black')

                  elif rand_item3 == square33colour    :
                                square3.setFill('white')

                  elif rand_item3 == square34colour    :
                                square3.setFill('white')
                            
                  elif rand_item3 == square36colour    :
                                square3.setFill('white')

                  if rand_item4 == square36colour:
                        counter += 1
                        square4.setFill('black')

                  elif rand_item4 == square33colour    :
                                square4.setFill('white')
                            
                  elif rand_item4 == square34colour    :
                                square4.setFill('white')
                                
                  elif rand_item4 == square35colour    :
                                square4.setFill('white')
                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)
                  else:
                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square37.setFill('tomato')
                                      square37colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square37.setFill('royalblue')
                                      square37colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square37.setFill('gold')
                                      square37colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square37.setFill('mediumseagreen')
                                      square37colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square37.setFill('orange')
                                      square37colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square37.setFill('mediumpurple')
                                      square37colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square38.setFill('tomato')
                                      square38colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square38.setFill('royalblue')
                                      square38colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square38.setFill('gold')
                                      square38colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square38.setFill('mediumseagreen')
                                      square38colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square38.setFill('orange')
                                      square38colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square38.setFill('mediumpurple')
                                      square38colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square39.setFill('tomato')
                                      square39colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square39.setFill('royalblue')
                                      square39colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square39.setFill('gold')
                                      square39colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square39.setFill('mediumseagreen')
                                      square39colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square39.setFill('orange')
                                      square39colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square39.setFill('mediumpurple')
                                      square39colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square40.setFill('tomato')
                                      square40colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square40.setFill('royalblue')
                                      square40colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square40.setFill('gold')
                                      square40colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square40.setFill('mediumseagreen')
                                      square40colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square40.setFill('orange')
                                      square40colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square40.setFill('mediumpurple')
                                      square40colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square37colour    :
                        counter += 1
                        square5.setFill('black')
                                
                  elif rand_item1 == square38colour    :
                            square5.setFill('white')
                            
                  elif rand_item1 == square39colour    :
                            square5.setFill('white')
                            
                  elif rand_item1 == square40colour    :
                            square5.setFill('white')

                            
                  if rand_item2 == square38colour:
                        counter += 1
                        square6.setFill('black')

                  elif rand_item2 == square37colour    :
                            square6.setFill('white')
                            
                  elif rand_item2 == square39colour    :
                            square6.setFill('white')
                            
                  elif rand_item2 == square40colour    :
                            square6.setFill('white')

                  if rand_item3 == square39colour:
                        counter += 1
                        square7.setFill('black')
                                
                  elif rand_item3 == square37colour    :
                            square7.setFill('white')
                            
                  elif rand_item3 == square38colour    :
                            square7.setFill('white')
                            
                  elif rand_item3 == square40colour    :
                            square7.setFill('white')

                  if rand_item4 == square40colour:
                        counter += 1
                        square8.setFill('black')

                  elif rand_item4 == square37colour    :
                            square8.setFill('white')
                            
                  elif rand_item4 == square38colour    :
                            square8.setFill('white')
                            
                  elif rand_item4 == square39colour    :
                            square8.setFill('white')

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:
                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square41.setFill('tomato')
                                      square41colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square41.setFill('royalblue')
                                      square41colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square41.setFill('gold')
                                      square41colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square41.setFill('mediumseagreen')
                                      square41colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square41.setFill('orange')
                                      square41colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square41.setFill('mediumpurple')
                                      square41colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square42.setFill('tomato')
                                      square42colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square42.setFill('royalblue')
                                      square42colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square42.setFill('gold')
                                      square42colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square42.setFill('mediumseagreen')
                                      square42colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square42.setFill('orange')
                                      square42colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square42.setFill('mediumpurple')
                                      square42colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square43.setFill('tomato')
                                      square43colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square43.setFill('royalblue')
                                      square43colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square43.setFill('gold')
                                      square43colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square43.setFill('mediumseagreen')
                                      square43colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square43.setFill('orange')
                                      square43colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square43.setFill('mediumpurple')
                                      square43colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square44.setFill('tomato')
                                      square44colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square44.setFill('royalblue')
                                      square44colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square44.setFill('gold')
                                      square44colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square44.setFill('mediumseagreen')
                                      square44colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square44.setFill('orange')
                                      square44colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square44.setFill('mediumpurple')
                                      square44colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square41colour    :
                        counter += 1
                        square9.setFill('black')

                  elif rand_item1 == square42colour    :
                            square9.setFill('white')
                            
                  elif rand_item1 == square43colour    :
                            square9.setFill('white')
                            
                  elif rand_item1 == square44colour    :
                            square9.setFill('white')

                            
                  if rand_item2 == square42colour:
                        counter += 1
                        square10.setFill('black')

                  elif rand_item2 == square41colour    :
                            square10.setFill('white')
                            
                  elif rand_item2 == square43colour    :
                            square10.setFill('white')
                            
                  elif rand_item2 == square44colour    :
                            square10.setFill('white')

                  if rand_item3 == square43colour:
                        counter += 1
                        square11.setFill('black')

                  elif rand_item3 == square41colour    :
                            square11.setFill('white')
                            
                  elif rand_item3 == square42colour    :
                            square11.setFill('white')
                            
                  elif rand_item3 == square44colour    :
                            square11.setFill('white')

                  if rand_item4 == square44colour:
                        counter += 1
                        square12.setFill('black')

                  elif rand_item4 == square41colour    :
                            square12.setFill('white')
                            
                  elif rand_item4 == square42colour    :
                            square12.setFill('white')
                            
                  elif rand_item4 == square43colour    :
                            square12.setFill('white')


                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:

                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square45.setFill('tomato')
                                      square45colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square45.setFill('royalblue')
                                      square45colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square45.setFill('gold')
                                      square45colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square45.setFill('mediumseagreen')
                                      square45colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square45.setFill('orange')
                                      square45colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square45.setFill('mediumpurple')
                                      square45colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square46.setFill('tomato')
                                      square46colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square46.setFill('royalblue')
                                      square46colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square46.setFill('gold')
                                      square46colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square46.setFill('mediumseagreen')
                                      square46colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square46.setFill('orange')
                                      square46colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square46.setFill('mediumpurple')
                                      square46colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square47.setFill('tomato')
                                      square47colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square47.setFill('royalblue')
                                      square47colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square47.setFill('gold')
                                      square47colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square47.setFill('mediumseagreen')
                                      square47colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square47.setFill('orange')
                                      square47colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square47.setFill('mediumpurple')
                                      square47colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square48.setFill('tomato')
                                      square48colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square48.setFill('royalblue')
                                      square48colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square48.setFill('gold')
                                      square48colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square48.setFill('mediumseagreen')
                                      square48colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square48.setFill('orange')
                                      square48colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square48.setFill('mediumpurple')
                                      square48colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square45colour    :
                        counter += 1
                        square13.setFill('black')

                  elif rand_item1 == square46colour    :
                            square13.setFill('white')
                            
                  elif rand_item1 == square47colour    :
                            square13.setFill('white')
                            
                  elif rand_item1 == square48colour    :
                            square13.setFill('white')

                  if rand_item2 == square46colour:
                        counter += 1
                        square14.setFill('black')

                  elif rand_item2 == square45colour    :
                            square14.setFill('white')
                            
                  elif rand_item2 == square47colour    :
                            square14.setFill('white')
                            
                  elif rand_item2 == square48colour    :
                            square14.setFill('white')

                  if rand_item3 == square47colour    :
                        counter += 1
                        square15.setFill('black')

                  elif rand_item3 == square45colour    :
                            square15.setFill('white')
                            
                  elif rand_item3 == square46colour    :
                            square15.setFill('white')
                            
                  elif rand_item3 == square48colour    :
                            square15.setFill('white')

                  if rand_item4 == square48colour:
                        counter += 1
                        square16.setFill('black')

                  elif rand_item4 == square45colour    :
                            square16.setFill('white')
                            
                  elif rand_item4 == square46colour    :
                            square16.setFill('white')
                            
                  elif rand_item4 == square47colour    :
                            square16.setFill('white')

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:

                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square49.setFill('tomato')
                                      square49colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square49.setFill('royalblue')
                                      square49colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square49.setFill('gold')
                                      square49colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square49.setFill('mediumseagreen')
                                      square49colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square49.setFill('orange')
                                      square49colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square49.setFill('mediumpurple')
                                      square49colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square50.setFill('tomato')
                                      square50colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square50.setFill('royalblue')
                                      square50colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square50.setFill('gold')
                                      square50colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square50.setFill('mediumseagreen')
                                      square50colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square50.setFill('orange')
                                      square50colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square50.setFill('mediumpurple')
                                      square50colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square51.setFill('tomato')
                                      square51colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square51.setFill('royalblue')
                                      square51colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square51.setFill('gold')
                                      square51colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square51.setFill('mediumseagreen')
                                      square51colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square51.setFill('orange')
                                      square51colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square51.setFill('mediumpurple')
                                      square51colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square52.setFill('tomato')
                                      square52colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square52.setFill('royalblue')
                                      square52colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square52.setFill('gold')
                                      square52colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square52.setFill('mediumseagreen')
                                      square52colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square52.setFill('orange')
                                      square52colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square52.setFill('mediumpurple')
                                      square52colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square49colour    :
                            counter += 1
                            square17.setFill('black')

                  elif rand_item1 == square50colour    :
                            square17.setFill('white')
                            
                  elif rand_item1 == square51colour    :
                            square17.setFill('white')
                            
                  elif rand_item1 == square52colour    :
                            square17.setFill('white')

                  if rand_item2 == square50colour:
                            counter += 1
                            square18.setFill('black')

                  elif rand_item2 == square49colour    :
                            square18.setFill('white')
                            
                  elif rand_item2 == square51colour    :
                            square18.setFill('white')
                            
                  elif rand_item2 == square52colour    :
                            square18.setFill('white')

                  if rand_item3 == square51colour:
                            counter += 1
                            square19.setFill('black')

                  elif rand_item3 == square49colour    :
                            square19.setFill('white')
                            
                  elif rand_item3 == square50colour    :
                            square19.setFill('white')
                            
                  elif rand_item3 == square52colour    :
                            square19.setFill('white')

                  if rand_item4 == square52colour:
                            counter += 1
                            square20.setFill('black')

                  elif rand_item4 == square49colour    :
                            square20.setFill('white')
                            
                  elif rand_item4 == square50colour    :
                            square20.setFill('white')
                            
                  elif rand_item4 == square51colour    :
                            square20.setFill('white')
 

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:
                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square53.setFill('tomato')
                                      square53colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square53.setFill('royalblue')
                                      square53colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square53.setFill('gold')
                                      square53colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square53.setFill('mediumseagreen')
                                      square53colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square53.setFill('orange')
                                      square53colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square53.setFill('mediumpurple')
                                      square53colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square54.setFill('tomato')
                                      square54colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square54.setFill('royalblue')
                                      square54colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square54.setFill('gold')
                                      square54colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square54.setFill('mediumseagreen')
                                      square54colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square54.setFill('orange')
                                      square54colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square54.setFill('mediumpurple')
                                      square54colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square55.setFill('tomato')
                                      square55colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square55.setFill('royalblue')
                                      square55colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square55.setFill('gold')
                                      square55colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square55.setFill('mediumseagreen')
                                      square55colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square55.setFill('orange')
                                      square55colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square55.setFill('mediumpurple')
                                      square55colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square56.setFill('tomato')
                                      square56colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square56.setFill('royalblue')
                                      square56colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square56.setFill('gold')
                                      square56colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square56.setFill('mediumseagreen')
                                      square56colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square56.setFill('orange')
                                      square56colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square56.setFill('mediumpurple')
                                      square56colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square53colour    :
                            counter += 1
                            square21.setFill('black')

                  elif rand_item1 == square54colour    :
                            square21.setFill('white')
                            
                  elif rand_item1 == square55colour    :
                            square21.setFill('white')
                            
                  elif rand_item1 == square56colour    :
                            square21.setFill('white')

                  if rand_item2 == square54colour:
                            counter += 1
                            square22.setFill('black')

                  elif rand_item2 == square53colour    :
                            square22.setFill('white')
                            
                  elif rand_item2 == square55colour    :
                            square22.setFill('white')
                            
                  elif rand_item2 == square56colour    :
                            square22.setFill('white')

                  if rand_item3 == square55colour:
                            counter += 1
                            square23.setFill('black')

                  elif rand_item3 == square53colour    :
                            square23.setFill('white')
                            
                  elif rand_item3 == square54colour    :
                            square23.setFill('white')
                            
                  elif rand_item3 == square56colour    :
                            square23.setFill('white')

                  if rand_item4 == square56colour:
                            counter += 1
                            square24.setFill('black')

                  elif rand_item4 == square53colour    :
                            square24.setFill('white')
                            
                  elif rand_item4 == square54colour    :
                            square24.setFill('white')
                            
                  elif rand_item4 == square55colour    :
                            square24.setFill('white')

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:
                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square57.setFill('tomato')
                                      square57colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square57.setFill('royalblue')
                                      square57colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square57.setFill('gold')
                                      square57colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square57.setFill('mediumseagreen')
                                      square57colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square57.setFill('orange')
                                      square57colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square57.setFill('mediumpurple')
                                      square57colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square58.setFill('tomato')
                                      square58colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square58.setFill('royalblue')
                                      square58colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square58.setFill('gold')
                                      square58colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square58.setFill('mediumseagreen')
                                      square58colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square58.setFill('orange')
                                      square58colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square58.setFill('mediumpurple')
                                      square58colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square59.setFill('tomato')
                                      square59colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square59.setFill('royalblue')
                                      square59colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square59.setFill('gold')
                                      square59colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square59.setFill('mediumseagreen')
                                      square59colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square59.setFill('orange')
                                      square59colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square59.setFill('mediumpurple')
                                      square59colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square60.setFill('tomato')
                                      square60colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square60.setFill('royalblue')
                                      square60colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square60.setFill('gold')
                                      square60colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square60.setFill('mediumseagreen')
                                      square60colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square60.setFill('orange')
                                      square60colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square60.setFill('mediumpurple')
                                      square60colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square57colour    :
                            counter += 1
                            square25.setFill('black')

                  elif rand_item1 == square58colour    :
                            square25.setFill('white')
                            
                  elif rand_item1 == square59colour    :
                            square25.setFill('white')
                            
                  elif rand_item1 == square60colour    :
                            square25.setFill('white')

                  if rand_item2 == square58colour:
                            counter += 1
                            square26.setFill('black')

                  elif rand_item2 == square57colour    :
                            square26.setFill('white')
                            
                  elif rand_item2 == square59colour    :
                            square26.setFill('white')
                            
                  elif rand_item2 == square60colour    :
                            square26.setFill('white')

                  if rand_item3 == square59colour:
                            counter += 1
                            square27.setFill('black')

                  elif rand_item3 == square57colour    :
                            square27.setFill('white')
                            
                  elif rand_item3 == square58colour    :
                            square27.setFill('white')
                            
                  elif rand_item3 == square60colour    :
                            square27.setFill('white')

                  if rand_item4 == square60colour:
                            counter += 1
                            square28.setFill('black')

                  elif rand_item4 == square57colour    :
                            square28.setFill('white')

                  elif rand_item4 == square58colour    :
                            square28.setFill('white')

                  elif rand_item4 == square59colour    :
                            square28.setFill('white')

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)

                  else:
                          counter = counter - counter
             
                  while True:
                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square61.setFill('tomato')
                                      square61colour = 'tomato'

                            if 775 < x < 820 and 510 < y < 555:  
                                      square61.setFill('royalblue')
                                      square61colour = 'royalblue'

                            if 840 < x < 884 and 510 < y < 555: 
                                      square61.setFill('gold')
                                      square61colour = 'gold'

                            if 906 < x < 950 and 510 < y < 555: 
                                      square61.setFill('mediumseagreen')
                                      square61colour = 'mediumseagreen'

                            if 971 < x < 1015 and 510 < y < 555: 
                                      square61.setFill('orange')
                                      square61colour = 'orange'

                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square61.setFill('mediumpurple')
                                      square61colour = 'mediumpurple'

                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square62.setFill('tomato')
                                      square62colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square62.setFill('royalblue')
                                      square62colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square62.setFill('gold')
                                      square62colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square58.setFill('mediumseagreen')
                                      square58colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square62.setFill('orange')
                                      square62colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square62.setFill('mediumpurple')
                                      square62colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square63.setFill('tomato')
                                      square63colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square63.setFill('royalblue')
                                      square63colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square63.setFill('gold')
                                      square63colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square63.setFill('mediumseagreen')
                                      square63colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square63.setFill('orange')
                                      square63colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square63.setFill('mediumpurple')
                                      square63colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break
                  while True:

                            click = win.getMouse()  
                            x = click.getX()
                            y = click.getY()
                          
                            if 708 < x < 752 and 510 < y < 555: 
                                      square64.setFill('tomato')
                                      square64colour = 'tomato'
                                      
                            if 775 < x < 820 and 510 < y < 555:  
                                      square64.setFill('royalblue')
                                      square64colour = 'royalblue'
                                      
                            if 840 < x < 884 and 510 < y < 555: 
                                      square64.setFill('gold')
                                      square64colour = 'gold'
                                      
                            if 906 < x < 950 and 510 < y < 555: 
                                      square64.setFill('mediumseagreen')
                                      square64colour = 'mediumseagreen'
                                      
                            if 971 < x < 1015 and 510 < y < 555: 
                                      square64.setFill('orange')
                                      square64colour = 'orange'
                                      
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      square64.setFill('mediumpurple')
                                      square64colour = 'mediumpurple'
                                      
                            if 708 < x < 752 and 510 < y < 555:
                                      break
                            if 775 < x < 820 and 510 < y < 555:
                                      break
                            if 840 < x < 884 and 510 < y < 555:
                                      break
                            if 906 < x < 950 and 510 < y < 555:
                                      break
                            if 971 < x < 1015 and 510 < y < 555:
                                      break
                            if 1038 < x < 1082 and 510 < y < 555: 
                                      break

                  if rand_item1 == square61colour    :
                            counter += 1
                            square29.setFill('black')

                  elif rand_item1 == square54colour    :
                            square30.setFill('white') 
                            
                  elif rand_item1 == square55colour    :
                            square31.setFill('white')
                            
                  elif rand_item1 == square56colour    :
                            square32.setFill('white')

                  if rand_item2 == square62colour:
                            counter += 1
                            square30.setFill('black')

                  elif rand_item2 == square53colour    :
                            square29.setFill('white')
                            
                  elif rand_item2 == square55colour    :
                            square31.setFill('white')
                            
                  elif rand_item2 == square56colour    :
                            square32.setFill('white')

                  if rand_item3 == square63colour:
                            counter += 1
                            square31.setFill('black')

                  elif rand_item3 == square53colour    :
                            square29.setFill('white')
                            
                  elif rand_item3 == square54colour    :
                            square30.setFill('white')
                            
                  elif rand_item3 == square56colour    :
                            square32.setFill('white')

                  if rand_item4 == square64colour:
                            counter += 1
                            square32.setFill('black')

                  elif rand_item4 == square53colour    :
                            square29.setFill('white')
                            
                  elif rand_item4 == square54colour    :
                            square30.setFill('white')
                            
                  elif rand_item4 == square55colour    :
                            square31.setFill('white')

                  if counter == 4:
                        if special == 1:
                                img1 = Image(Point(640,360), "winscreen special.PNG")
                                img1.draw(win)
                        else:
                                normal = Image(Point(640,360), "winscreen.PNG")
                                normal.draw(win)
                        
                  if counter != 4:
                        img5 = Image(Point(640,360), "gameover screen.PNG")
                        img5.draw(win)
                  else:
                          
                          pass  

                  break
                  #reset incorrect squares

        #Win screen / message

if __name__ == "__main__":
        main()


        
        

        
