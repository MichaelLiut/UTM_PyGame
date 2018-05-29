# Course: Course ID
# Name:  XXXXXXXX
# Student number: 0000000
# File: MovingBox.py

# This program creates a graphical window, displays a message and a square.
# After a click, the square starts rolling to the right. When it rolls all 
# the way to the right, a message is displayed, and after a click, the 
# program terminates.

from graphics import *
from time import sleep
from math import *

# class Ground -----------------------------------------------------------
class Ground:
    # the constructor
    def __init__(self, win, length, height):
        '''create ground in black colour as a thin long black rectangle 
           drawn at the bottom of the window `win'. `length' and `height' 
           are the window's dimensions.'''

        self.ground = Rectangle(Point(6,height-6),Point(length-6,height-10))
        self.ground.setFill('black')   # make it black
        self.ground.draw(win)          # ddisplay it in window win
#end of class Ground -----------------------------------------------------


# function rotate --------------------------------------------------------
def rotate(p1,p2,angle):
    ''' this function returns a new position of point p1 after rotating the
        segment <p1,p2> by angle `angle'. The angle is in radians.
        The x-coordinate of p1 must be <= x-coordinate of p2 and
        the y-coordinate of p2 must be <= y-coordinate of p2
        The angle must be so that the angle <= pi/2. '''

    t1 = abs(p1.getY()-p2.getY())
    t2 = abs(p1.getX()-p2.getX())
    beta = atan(t1/t2)                      # in radians
    alpha = angle*(pi/180)                  # in radians
    gamma = alpha+beta                      # in radians
    r = sqrt(t1*t1+t2*t2)
    a = r*sin(gamma)
    b = r*cos(gamma)
    dx = t2-b
    dy = a-t1
    p3 = Point(p1.getX()+dx,p1.getY()-dy)
    return p3
# end of function rotate -------------------------------------------------


# function complete ------------------------------------------------------
def complete(p1,p2,r,angle):
   ''' this function computes points p3 and p4 so that
        p1,p3,p4,p2 forms a square of size r. `angle' is
        the angle of the segment <p1,p2> and a horizontal line.'''
   
   dx = r*sin(angle)                    # compute dx
   dy = r*cos(angle)                    # compute dy
   p3 = Point(p1.getX()+dx,p1.getY()-dy)  # create p3
   p4 = Point(p2.getX()+dx,p2.getY()-dy)  # create p4
   return (p3,p4)                       # return p3 and p4
# end of function complete ----------------------------------------------


# function one_rotation -------------------------------------------------
def one_rotation(p1,p2,p3,p4,win):
    ''' thus function rotates the square p1,p3,p4,p1 one full rotation
        to the right. The speed should be 5 degrees every 0.1 second. '''

    s = Polygon(p1,p3,p4,p2,p1)      # create the square
    s.setFill('red')                 # make it red
    s.setOutline('red')
    s.draw(win)                      # display it in `win'
    totangle = angle = 5             # angle will be moving 5 degrees
    # the animation loop until the vertical line is reached
    while totangle <= 90:            # untill we reach vertical
        p1 = rotate(p1,p2,angle)     # rotate <p1,p2> around p2
        # after rotating <p1,p2>, complete the whole square
        p3,p4 = complete(p1,p2,100,totangle*(pi/180))
        s.undraw()                   # remove from display the old square
        s = Polygon(p1,p3,p4,p2,p1)  # create the new (rotated) square
        s.setFill('red')             # make it red
        s.setOutline('red')
        s.draw(win)                  # display it
        sleep(0.01)                  # sleep
        totangle += 5                # cummulate the angles
    # end of animation loop
    # after one full rotation, rmove the square from display
    s.undraw()
# end of function one_rotation ------------------------------------------


# function main ---------------------------------------------------------
def main():
    height = 400                      # required dimensions of the window
    length = 1000
    win = GraphWin("Rolling square",length,height)   # create the window
    ground = Ground(win,length,height)       # create and display the ground
    p1 = Point(20, height-10)                # create initial p1 and p2
    p2 = Point(p1.getX()+100,p1.getY())
    p3,p4 = complete(p1,p2,100,0)            # complete p1, p2 to square
    s = Polygon(p1,p3,p4,p2,p1)              # create the square
    s.setFill('red')                         # make it red  
    s.setOutline('red')
    s.draw(win)                              # display it in `win'

    # create initial message in blue
    message = Text(Point(450,70), "A mouse click will start the square rolling")
    message.setTextColor('blue')
    message.draw(win)                         # display initial message
    win.getMouse()                            # wait for click
    s.undraw()                                # remove the square from display
    message.undraw()                          # remove the message from display

    # the animation loop until the square is in the ight position
    while p2.getX() < 900:
        one_rotation(p1,p2,p3,p3,win)         # rotate the squre 1 rotation
        p1 = Point(p1.getX()+100,p1.getY())   # create p1 shifted 100 to the right
        p2 = Point(p2.getX()+100,p2.getY())   # create p2 shifted 100 to the right
        p3 = Point(p3.getX()+100,p3.getY())   # create p3 shifted 100 to the right
        p4 = Point(p4.getX()+100,p4.getY())   # create p4 shifted 100 to the right
    # end of animation loop

    s = Polygon(p1,p3,p4,p2,p1)               # create the final square
    s.setFill('red')                          # make it red
    s.setOutline('red')
    s.draw(win)                               # display it in 'win'

    # create final message in blue
    message = Text(Point(450,70), "A mouse click will terminate the program")
    message.setTextColor('blue')
    message.draw(win)                        # display tfinal message
    win.getMouse()                           # wait from click
    win.close()                              # close the window
# end of function main --------------------------------------------------

# executable program
main()
