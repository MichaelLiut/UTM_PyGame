# Course: Course ID
# Name:  XXXXXXXX
# Student number: 0000000
# File: SmallTrain.py

# This program creates a graphical window, displays a message.  After a click,  
# a tractor-trailer emerges from behind the right edge of the window and moves 
# from right to left.  As it moves, it slowly gets smaller.  It will disappear 
# behind the left edge of the window. After a click, the terminates.

from graphics import *
from time import sleep


# class Road -----------------------------------------------------------
class Road:

    # constructor
    def __init__(self, win, height):
        '''create round in black colour as a thin long black rectangle 
           displayd at the bottom of the window `win'. `length' and `height' 
           are the window's dimensions.'''
 
        self.road = Rectangle(Point(4,196-height),Point(1196,196))
        self.road.setFill('black')   # make it black
        self.road.draw(win)          # display it in `win'
    # end of constructor

#end of class Road -----------------------------------------------------


# class TrailerWheels --------------------------------------------------
class TrailerWheels:

    # constructor 
    def __init__(self, win, p, d):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the trailer is, `d' is the scaling factor. '''

        # the wheels consist of 4 black filled circles of radies 3d
        c1 = Point(p.getX()+7*d,p.getY()-3*d)  # centre of the 1st wheel
        c2 = Point(p.getX()+14*d,p.getY()-3*d) # centre of the 2nd wheel
        c3 = Point(p.getX()+26*d,p.getY()-3*d) # centre of the 3rd wheel
        c4 = Point(p.getX()+33*d,p.getY()-3*d) # centre of the 3rd wheel
        self.w1 = Circle(c1,3*d)    # create the first wheel
        self.w1.setFill('black')    # give it required colour
        self.w1.draw(win)           # display it in `win'
        self.w2 = Circle(c2,3*d)    # create the second wheel
        self.w2.setFill('black')    # give it required colour
        self.w2.draw(win)           # display it in `win'
        self.w3 = Circle(c3,3*d)    # create the third wheel
        self.w3.setFill('black')    # give it required colour
        self.w3.draw(win)           # display it in `win'
        self.w4 = Circle(c4,3*d)    # create the third wheel
        self.w4.setFill('black')    # give it required colour
        self.w4.draw(win)           # display it in `win'
    #end of constructor

    def undraw(self):
        self.w1.undraw()           # remove from display w1
        self.w2.undraw()           # remove from display w2
        self.w3.undraw()           # remove from display w3
        self.w4.undraw()           # remove from display w4
    # end of undraw

#end of class TrailerWheels --------------------------------------------


#class TrailerBox ------------------------------------------------------
class TrailerBox:

    # constructor
    def __init__(self,win,p,d,colour):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the trailer is, `d' is the scaling factor,
             `colour; is the fill colour of the box.'''

        q1 = Point(p.getX(),p.getY()-23*d)   # top left point of the box
        q2 = Point(p.getX()+40*d,p.getY()-3*d)    # bottom right point of the box
        self.box = Rectangle(q1,q2)          # create the box
        self.box.setFill(colour)             # give it the right colour
        self.box.setOutline(colour)
        self.box.draw(win)                   # display it in `win'
    # end of constructor

    def undraw(self):
        self.box.undraw()                    # remove from display it
    # end of undraw 

#end class TrailerBox --------------------------------------------------


#class Trailer ---------------------------------------------------------
class Trailer:

    # constructor
    def __init__(self,win,p,d,colour):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the trailer is, `d' is the scaling factor,
             `colour; is the fill colour of the box of the trailer.'''

        # trailer consists of trailer box and thrailer wheels
        # we have to create them in this order, so the wheels are not
        # covered by the tbox
        self.tbox = TrailerBox(win,p,d,colour)    # create and display tbox
        self.wheels = TrailerWheels(win,p,d)      # create and display wheels
    # end of constructor

    def undraw(self):
        self.tbox.undraw()               # remove from display the tbox
        self.wheels.undraw()             # remove from display the wheels
    # end of andraw

# end of class Trailer -------------------------------------------------



#class TractorWheels ---------------------------------------------------
class TractorWheels:

    # constructor
    def __init__(self,win,p,d):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the tractor is, `d' is the scaling factor.'''

        # the wheels consist of 3 black filled circles of radius 4d
        c1 = Point(p.getX()+6*d,p.getY()-4*d)    # centre of 1st wheel
        self.w1 = Circle(c1,4*d)                 # create the wheel
        self.w1.setFill('black')                 # make it black
        self.w1.draw(win)                        # display it in `win'
        c2 = Point(p.getX()+25*d,p.getY()-4*d)   # centre of 2nd wheel
        self.w2 = Circle(c2,4*d)                 # create the wheel
        self.w2.setFill('black')                 # make it black
        self.w2.draw(win)                        # display it in `win'
        c3 = Point(p.getX()+34*d,p.getY()-4*d)   # centre of 3rd wheel
        self.w3 = Circle(c3,4*d)                 # create the wheel
        self.w3.setFill('black')                 # make it black
        self.w3.draw(win)                        # display it in `win'
    # end of constructor

    def undraw(self):
        self.w1.undraw()                         # remove it form display
        self.w2.undraw()                         # remove it form display
        self.w3.undraw()                         # remove it form display
    # end of undraw

#end of class TractorWheels --------------------------------------------

#class Tractor ---------------------------------------------------------
class Tractor:

    # constructor
    def __init__(self,win,p,d,colour):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the tractor is, `d' is the scaling factor, and
             `colour' is the colour of the tractor. '''

        # the tractor consists of two boxes box1 and box2 making the body,
        # and a box w1 and a triangle w2 making the window, and the wheels
        p1 = Point(p.getX(),p.getY()-11*d)       # top left of box box1
        p2 = Point(p.getX()+40*d,p.getY()-3*d)   # bottom right of box box1
        self.box1 = Rectangle(p1,p2)             # create it
        self.box1.setFill(colour)                # give it colour
        self.box1.setOutline(colour)           
        self.box1.draw(win)                      # displayit in `win'
        
        p1 = Point(p.getX()+7*d,p.getY()-20*d)   # top left of box box2
        p2 = Point(p.getX()+16*d,p.getY()-11*d)  # bottom right of box box2
        self.box2 = Rectangle(p1,p2)             # create it
        self.box2.setFill(colour)                # give it colour
        self.box2.setOutline(colour)
        self.box2.draw(win)                      # display it in `win'
        
        p1 = Point(p.getX()+7*d,p.getY()-19*d)   # top left of box w1
        p2 = Point(p.getX()+15*d,p.getY()-11*d)  # bottom right of box w1
        self.w1 = Rectangle(p1,p2)               # create it
        self.w1.setFill('blue')                  # make it blue
        self.w1.setOutline('blue')
        self.w1.draw(win)                        # display it in `win'
        
        p2 = Point(p.getX()+7*d,p.getY()-11*d)   # point 2 of the trinagle
        p3 = Point(p.getX()+3*d,p.getY()-11*d)   # point 3 of the triangle
        self.w2 = Polygon(p1,p2,p3,p1)           # create the triangle
        self.w2.setFill('blue')                  # make it blue
        self.w2.setOutline('blue')
        self.w2.draw(win)                        # display it in `win'

        # we have to do the wheels last so they are not covered by the body
        self.wheels = TractorWheels(win,p,d)     # create and display the wheels
    # end of constructor

    def undraw(self):
        self.box1.undraw()                         # remove it form display
        self.box2.undraw()                         # remove it form display
        self.w1.undraw()                           # remove it form display
        self.w2.undraw()                           # remove it form display
        self.wheels.undraw()                       # remove it form display
    # end of undraw

#end class Tractor -----------------------------------------------------

#class TractorTrailer --------------------------------------------------
class TractorTrailer:
    # constructor
    def __init__(self,win,p,d,colour1,colour2,colour3):
        ''' `win' is the window, `p' is the point on the ground where the
             beginning of the tractor is, `d' is the scaling factor, 
             `colour1' is the colour of the tractor, `colour2' is the colour
            of the first trailer, and `colour3' is the colour of the
            second trailer. '''

        # tractor-trailer consists of a tractor and two trailers
        self.tractor = Tractor(win,p,d,colour1)  # create and display tractor at
                                                 # position p
        p = Point(p.getX()+42*d,p.getY())        # compute position of trailer1
        self.trailer1 = Trailer(win,p,d,colour2) # crate and display trailor1 at
                                                 # position p
        p = Point(p.getX()+42*d,p.getY())        # compute the potition of trailer2
        self.trailer2 = Trailer(win,p,d,colour3) # create and display tarilor2 at
                                                 # positon p
    # end of constructor

    def undraw(self):
        self.tractor.undraw()                    # remove from display
        self.trailer1.undraw()                   # remove from display
        self.trailer2.undraw()                   # remove from display
    # end of undraw

#end class TractorTrailer ----------------------------------------------
        
        

# function main --------------------------------------------------------
def main():
    win = GraphWin("Tractor trailer",1200,200)    # create the window
    road = Road(win,2)                            # create and display the road
    # create initial message in blue
    message = Text(Point(580,70),"A mouse click will start the tractor-trailer")
    message.setTextColor('blue')        
    message.draw(win)                     # display initial message
    win.getMouse()                        # wait for click
    message.undraw()                      # remove initial message from display
    p = Point(1200,193)                   # compute initial starting point
    d = 4                                 # set initial scaling factort
    # create and display the initial tractor-trailer
    t = TractorTrailer(win,p,d,'orange','green','grey')

    # animation loop
    #     loop as long as at least a part of tractor-traileris visible    
    while p.getX()+ 124*d > 0:
        sleep(0.1)                         # sleep
        t.undraw()                         # remove tractor-trailer from display
        d -= 0.02                          # shrink the scale
        p = Point(p.getX()-10,p.getY())    # compute new starting point
        # create and display smaller tractor-trailer
        t = TractorTrailer(win,p,d,'orange','green','grey')
    # end of animation loop
    # create final message in blue
    message = Text(Point(600,70),"A mouse click will terminate the program")
    message.setTextColor('blue')
    message.draw(win)                      # display final message
    win.getMouse()                         # wait for click
    win.close()                            # close the window
# end of function main -------------------------------------------------


# executable program
main()
# program terminates
