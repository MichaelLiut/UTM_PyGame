# Course: Course ID
# Name:  XXXXXXXX
# Student number: 0000000
# File: Train.py

# This program creates a train in the right end of a graphics window.
# After a click, the train moves left as far as it can and then stops.
# After a click, the train backs back to its original position.
# After a click, the graphics windows closes and the program terminates

# import all names from module graphics
from graphics import *

# import name sleep from module time
from time import sleep



# Wheels are common to BoxCar, PassengerCar, Caboose, and Locomotive
class Wheels:

    # constructor of class Wheels
    def __init__(self, win, b, length, height, r, colour):
        """ Creates wheels for a car whose box left-top
            corner is located at the point b, the box dimensions
            are length and height. r is the wheels radius. The
            wheels are drawn in the graphics window win in the
            colour given in the variable colour """ 

        x = length - 4*r    #  the length of the part not taken by the wheels                            
        if x <= 0 :  # the wheels are too big for the box
            message = Text(Point(300,100),"wrong wheel radius")
            message.draw(win)
            return
        # so the wheel size is OK
        # the wheels are placed evenly   |--O--O--|
        x = int(x) / 3    #                x  x  x
        c1 = Point(b.getX()+x+r,b.getY()+height) #center of the 1st wheel
        c2 = Point(b.getX()+length-x-r,b.getY()+height) #center of the 2nd wheel
        self.w1 = Circle(c1,r)      # create the first wheel
        self.w1.setFill(colour)     # give it required colour
        self.w1.draw(win)           # draw it
        self.w2 = Circle(c2,r)      # create the second wheel
        self.w2.setFill(colour)     # give it required colour
        self.w2.draw(win)           # draw it
    #end of constructor

    # method move -- move the wheels dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.w1.move(dx, dy)    # move the first wheel (it is a Circle)
        self.w2.move(dx, dy)    # move the second wheel (it is a Circle)
#end of class Wheels




# Box is common to BoxCar, PassengerCar, Caboose, and Locomotive 
class Box:

    # the constructor
    def __init__ (self, win, b, length, height, colour):
        """ Creates box for a car whose left-top corner is located
            at the point b, the box dimensions are length and height.
            The box is drawn in the graphics window win in the
            colour given in the variable colour """ 

        #compute the right bottom point of the box
        b1 = Point(b.getX()+length,b.getY()+height)  
        self.box = Rectangle(b,b1)   # create the box
        self.box.setFill(colour)     # give it required colour
        self.box.draw(win)           # draw the box
    #end of constructor

    # method move -- moves the box dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.box.move(dx, dy)    # move the box (it is a Rectangle)
    #end of move
#end of class Box


# BoxCar uses Wheels and Box
class BoxCar:


    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a box car with a box given by b, length, height
            and wheels given by b, length, height, and radius.
            The box is to have colour box_colour, the wheels are
            to have colour wheel_colour. The box car is drawn in
            the graphics window win """ 
        
        # create and draw wheels (must do wheels first so they are
        # half-covered by the box)
        self.wheels = Wheels(win, b, length, height, radius, wheel_colour)
        # create and draw box
        self.box = Box(win, b, length, height, box_colour)
        # we need to add doors
        p1 = Point(b.getX()+length/3,b.getY()+height/3)  #compute left-top point
        p2 = Point(b.getX()+(2*length)/3,b.getY()+height)#compute right-bottom point
        self.door = Rectangle(p1,p2)   # creates the door
        self.door.draw(win)            # and draw it
    #end of constructor

    # method move -- moves box car dx along the x axis and dy along the y axis
    def move(self, dx, dy):
        self.wheels.move(dx, dy)   # move the wheels (must do before box!!)
        self.box.move(dx, dy)      # move the box
        self.door.move(dx, dy)     # move the door
    #end of move
#end of class BoxCar


# PassengerCar uses Wheels and Box
class PassengerCar:

    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a passenger car with a box given by b, length, height
            and wheels given by b, length, height, and radius.
            The box is to have colour box_colour, the wheels are
            to have colour wheel_colour. The box car is drawn in
            the graphics window win """

        # create and draw wheels (must do wheels first so they are
        # half-covered by the box)       
        self.wheels = Wheels(win, b, length, height, radius, wheel_colour)

        # create and draw box
        self.box = Box(win, b, length, height, box_colour)

        # now we need to add black left door, three blue windows, and
        # black right door
        d = length/11
        # compute x1,y1 and x2,y2 points for the left door
        x1 = b.getX()+d 
        y1 = b.getY()+height/4
        x2 = x1+d
        y2 = y1+(2*height)/4
        self.door1 = Rectangle(Point(x1,y1),Point(x2,y2)) # create left door
        self.door1.setFill('black')                       # make it black colour
        self.door1.draw(win)                              # draw it
        # compute x1,y1 and x2,y2 points for the 1st window
        x1 = x1+2*d
        x2 = x1+d
        y2 = y1+height/4
        self.window1 = Rectangle(Point(x1,y1),Point(x2,y2)) # create 1st window
        self.window1.setFill('blue')                        # make it blue
        self.window1.draw(win)                              # draw it
        # compute x1,y1 and x2,y2 points for the 2nd window
        x1 = x1+2*d
        x2 = x1+d
        y2 = y1+height/4
        self.window2 = Rectangle(Point(x1,y1),Point(x2,y2)) # create 1st window
        self.window2.setFill('blue')                        # make it blue
        self.window2.draw(win)                              # draw it
        # compute x1,y1 and x2,y2 points for the 3rd window
        x1 = x1+2*d
        x2 = x1+d
        y2 = y1+height/4
        self.window3 = Rectangle(Point(x1,y1),Point(x2,y2)) # create 1st window
        self.window3.setFill('blue')                        # make it blue
        self.window3.draw(win)                              # draw it
        # compute x1,y1 and x2,y2 points for the right door
        x1 = x1+2*d
        y1 = b.getY()+height/4
        x2 = x1+d
        y2 = y1+(2*height)/4
        self.door2 = Rectangle(Point(x1,y1),Point(x2,y2)) # create right door
        self.door2.setFill('black')                       # make it black colour
        self.door2.draw(win)                              # draw it
    #end of constructor
        
    # method move -- moves the passenger car dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.wheels.move(dx, dy)  # move the wheels (before box!!)
        self.box.move(dx, dy)     # move the box
        self.door1.move(dx, dy)   # move the left door (it is Rectangle)
        self.window1.move(dx, dy) # move the 1st window (it is Rectangle)
        self.window2.move(dx, dy) # move the 2nd window (it is Rectangle)
        self.window3.move(dx, dy) # move the 3rd window (it is Rectangle)
        self.door2.move(dx, dy)   # move the right door (it is Rectangle)
    #end of move
#end of class PassengerCar





# Caboose uses Wheels and Box
class Caboose:

    def __init__(self, win, b, length, height, radius, box_colour,
                 wheel_colour, bubble_colour):
        """ Creates a caboose with a box given by b, length, height of
            the colour box_colour, and wheels given by b, length, height,
            and radius of colour wheel_colour. The bubble's dimensions
            are determined from the dimensions of the box, its colour is
            given by bubble_colour. The caboose is drawn in the graphics
            window win """

        # create and draw wheels (before box)
        self.wheels = Wheels(win, b, length, height, radius, wheel_colour)
        # create bubble before box!!
        # compute bounding rectangle for the bubble
        p1 = Point(b.getX()+length/4,b.getY()-height/4)
        p2 = Point(b.getX()+(3*length)/4,b.getY()+height/4)
        self.bubble = Oval(p1,p2)   # create bubble
        self.bubble.setFill(bubble_colour)   # make it required colour
        self.bubble.draw(win)       # draw it
        # create and draw box
        self.box = Box(win, b, length, height, box_colour)
    #end of constructor

    #method move -- moves caboose dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.wheels.move(dx, dy)   # move wheels (before box)
        self.bubble.move(dx, dy)   # move bubble (it is an Oval) - before box
        self.box.move(dx, dy)      # move box
    #end of move
#end of class Caboose



        
# uses Box and Wheels
class Locomotive:

    # the constructor
    def __init__(self, win, b, length, height, radius, box_colour,
                 cowcatcher_colour, wheel_colour, smokestack_colour,
                 cabin_colour):
        """ Creates a locomotive with a box given by b, length, height of
            the colour box_colour, and wheels given by b, length, height,
            and radius of colour wheel_colour. The cowcatcher colour is given
            by cowcatcher_colour. The smokestack's colour is given by
            smokestack_colour. The cabin colour is given by cabin_colour.
            The dimensions of the cowcatcher are determined from the dimension
            of the box. The dimensions of the smokestack are determined from
            the dimensions of the box. The dimensions of the cabin are determined
            from the dimensions of the box. The locomotive is drawn in the
            graphics window win """

        # create and draw wheels (before box)
        self.wheels = Wheels(win, b, length, height, radius, wheel_colour)
        self.box = Box(win, b, length, height, box_colour) # create and draw box
        # compute the dimensions of the smokestack
        p1 = Point(b.getX()+length/8,b.getY()-height/3)
        p2 = Point(b.getX()+length/4,b.getY())
        self.smokestack = Rectangle(p1,p2)  # create the smokestack
        self.smokestack.setFill(smokestack_colour)  # make it required colour
        self.smokestack.draw(win)                   # and draw it
        # compute the dimensions of the cabin
        p1 = Point(b.getX()+(2*length)/3,b.getY()-height/2)
        p2 = Point(b.getX()+length,b.getY())
        self.cabin = Rectangle(p1,p2)      # create cabin
        self.cabin.setFill(cabin_colour)  # give it required colour
        self.cabin.draw(win)               # and draw it
        # compute cowcatcher
        p1 = Point(b.getX(),b.getY()+height)
        p2 = Point(b.getX()-length/6,b.getY()+height)
        self.cowcatcher = Polygon(b,p1,p2)   # create cowcatcher
        self.cowcatcher.setFill(cowcatcher_colour)  # give it required colour
        self.cowcatcher.draw(win)            # and draw it
    #end of constructor

    # method move -- moves locomotive dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.wheels.move(dx, dy)      # move wheels (before box)
        self.box.move(dx, dy)         # move box
        self.smokestack.move(dx, dy)  # move smokestack (it is Rectangle)
        self.cabin.move(dx, dy)      # move cabin (it is Rectangle)
        self.cowcatcher.move(dx, dy)  # move cowcatcher (it is Polygon)
    #end of move
#end of class Locomotive

    

class Tracks:

    # the constructor
    def __init__(self, win, height):
        """ create tracks in black colour """
        # create tracks as a thin long rectangle
        self.tracks = Rectangle(Point(4,196-height),Point(1196,196))
        self.tracks.setFill('black')   # make it black
        self.tracks.draw(win)          # draw it
#end of class Tracks



class Train:

    # the constructor
    def __init__(self, win):
        """ assemble a train and draw it in the graphics window win """
        length = 60
        height = 30
        radius = 8
    
        p = Point(1136,155)  # set position of the last car
        # create last caboose and draw it
        self.trail_caboose = Caboose(win, p, length, height, radius, 'red', 'black', 'blue')
        
        p = Point(p.getX()-64,p.getY()) # compute position of the second last car
        # create a box car and draw it
        self.BoxCar1 = BoxCar(win,p,length,height,8,'blue','black')

        p = Point(p.getX()-64,p.getY()) # compute position of the third car from the end
        # create a box car and draw it
        self.BoxCar2 = BoxCar(win,p,length,height,8,'yellow','black')
        
        p = Point(p.getX()-64,p.getY()) # compute position of the 4th car from the end
        # create a passenger car and draw it
        self.PassengerCar1 = PassengerCar(win, p, length, height, radius, 'green', 'black')
        
        p = Point(p.getX()-64,p.getY()) # compute position of the 5th car from the end
        # create a passenger car and draw it
        self.PassengerCar2 = PassengerCar(win, p, length, height, radius, 'red','black')
        
        p = Point(p.getX()-64,p.getY()) # compute position of the 6th car from the end
        # create a caboose and draw it
        self.lead_caboose = Caboose(win, p, length, height, radius, 'blue', 'black', 'red')
        
        p = Point(p.getX()-64,p.getY()) # compute position of the 7th car from the end
        # create a locomotive and draw it
        self.locomotive = Locomotive(win, p, length, height, radius, 'black', 'brown', 'black', 'gray', 'gray')

        self.start = p.getX()-length/6  # compute the position of the front of the train
    #end of constructor

    # method move -- moves train dx along x axis and dy along y-axis
    def move(self, dx, dy):
        self.trail_caboose.move(dx, dy)  # move the last car
        self.BoxCar1.move(dx, dy)        # move the 2nd last car
        self.BoxCar2.move(dx, dy)        # move the 3rd car from the end
        self.PassengerCar1.move(dx, dy)  # move the 4th car from the end
        self.PassengerCar2.move(dx, dy)  # move the 5th car from the end
        self.lead_caboose.move(dx, dy)   # move the 6th car from the end
        self.locomotive.move(dx, dy)     # move the locomotive
        self.start = self.start + dx     # update the position of the front of the train
    #end of move

    #method getStart -- returns the position of the front of the train
    def getStart(self):
        return self.start
    #end of getStart()
#end of class Train



# function main()
def main():
    win = GraphWin("Train",1200,200)   # create the required graphics window
    tracks = Tracks(win,2)             # create and display the tracks
    train = Train(win)                 # create and display train in the starting position
    original = train.getStart()        # remember starting position
    message = Text(Point(600,30),"click to start")   # display the message
    message.draw(win)                                
    win.getMouse()                                   # wait for click
    message.undraw()                   # undisplay the message
    # the animation loop -- move train from right to left
    while train.getStart() >= 4:
        train.move(-1,0)
        sleep(0.000001)
    # the train moved to the left
    message.setText("click to reverse") # change the message
    message.draw(win)                  # and draw it
    win.getMouse()                     # wait for click
    message.undraw()                   # undraw the message
    # the animation loop -- move train from left to right backward
    while train.getStart() < original:
        train.move(2,0)
        sleep(0.000001)
    # the train is back to the right
    message.setText("click to terminate")  # change the message
    message.draw(win)                      # draw it
    win.getMouse()                         # wait for click
    win.close()                            # close the graphics window
#end of main()


# the executable part of the program
main()  # execute main()
# program terminates
