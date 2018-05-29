# Course: Course Code
# Name: FirstName LastName
# Student Number: ##########
# File: Train_YourName.py
# Description: What does this file do? 


# import all names from module graphics
from graphics import *
   
# import name sleep from module time
import time



# Wheels are common to BoxCar, PassengerCar, Caboose, and Locomotive
class Wheels:

    # constructor of class Wheels
    def __init__(self, win, b, length, height, r, colour):
        """ Creates wheels for a car whose box left-top
            corner is located at the point 'b', the box dimensions
            are 'length' and 'height'. r is the wheels radius. The
            wheels are drawn in the graphics window 'win' in the
            colour given in the variable 'colour' """ 

        """ Your code goes here """
    	
    	
    
    #end of constructor

    # method move -- moves the wheels dx along x axis and dy along y axis
    def move(self, dx, dy):
        """ Your code goes here """
#end of class Wheels




# Box is common to BoxCar, PassengerCar, Caboose, and Locomotive 
class Box:

    # the constructor
    def __init__ (self, win, b, length, height, colour):
        """ Creates box for a car whose left-top corner is located
            at the point 'b', the box dimensions are 'length' and 'height'.
            The box is drawn in the graphics window 'win' in the
            colour given in the variable 'colour' """ 

        """ Your code goes here """
    #end of constructor

    # method move -- moves the box dx along x axis and dy along y axis
    def move(self, dx, dy):
        """ Your code goes here """
    #end of move
#end of class Box


# BoxCar uses Wheels and Box
class BoxCar:


    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a boxcar with a box given by 'b', 'length', 'height'
            and wheels given by 'b', 'length', 'height', and 'radius'.
            The box is to have colour 'box_colour', the wheels are
            to have colour 'wheel_colour'. The box car is drawn in
            the graphics window 'win' """ 
        
        """ Your code goes here """
    #end of constructor

    # method move -- moves box car dx along the x axis and dy along the y axis
    def move(self, dx, dy):
        """ Your code goes here """
    #end of move
#end of class BoxCar


# PassengerCar uses Wheels and Box
class PassengerCar:

    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a passenger car with a box given by 'b', 'length',
            'height' and wheels given by 'b', 'length', 'height', and
            'radius'. The box is to have colour 'box_colour', the wheels
            are to have colour 'wheel_colour'. The box car is drawn in
            the graphics window 'win' """

        """ Your code goes here """
    #end of constructor
        
    # method move -- moves the passenger car dx along x axis and dy along y axis
    def move(self, dx, dy):
        """ Your code goes here """
    #end of move
#end of class PassengerCar





# Caboose uses Wheels and Box
class Caboose:

    def __init__(self, win, b, length, height, radius, box_colour,
                 wheel_colour, bubble_colour):
        """ Creates a caboose with a box given by 'b', 'length', 'height' and
            of colour 'box_colour'. The wheels are given by 'b', 'length',
            'height', 'radius' and are of colour 'wheel_colour'. The bubble's
            dimensions are determined from the dimensions of the box, its
            colour is given by 'bubble_colour'. The caboose is drawn in the
            graphics window 'win' """

        """ Your code goes here """
    #end of constructor

    #method move -- moves caboose dx along x axis and dy along y axis
    def move(self, dx, dy):
        """ Your code goes here """
    #end of move
#end of class Caboose



        
# uses Box and Wheels
class Locomotive:

    # the constructor
    def __init__(self, win, b, length, height, radius, box_colour,
                 cowcatcher_colour, wheel_colour, smokestack_colour,
                 cabin_colour):
        """ Creates a locomotive with a box given by 'b', 'length', 'height'
            and of colour 'box_colour'. The wheels are given by 'b', 'length',
            'height', 'radius' and are of colour 'wheel_colour'. The cowcatcher
            colour is given by 'cowcatcher_colour'. The smokestack's colour
            is given by 'smokestack_colour'. The cabin colour is given by
            'cabin_colour'. The dimensions of the cowcatcher are determined
            from the dimension of the box. The dimensions of the smokestack
            are determined from the dimensions of the box. The dimensions of
            the cabin are determined from the dimensions of the box. The
            locomotive is drawn in the graphics window 'win' """

        """ Your code goes here """
    #end of constructor

    # method move -- moves locomotive dx along x axis and dy along y axis
    def move(self, dx, dy):
        """ Your code goes here """
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
    
        """ Your code goes here """
    #end of constructor

    # method move -- moves train dx along x axis and dy along y-axis
    def move(self, dx, dy):
        """ Your code goes here """
    #end of move

    #method getStart -- returns the position of the front of the train
    def getStart(self):
        """ Your code goes here """
    #end of getStart()
#end of class Train



# function main()
def main():
    win = GraphWin("Train",1200,200)   # create the required graphics window
    tracks = Tracks(win,2)             # create and display the tracks
    train = Train(win)                 # create and display train in the starting position
    original = train.getStart()        # remember starting position

    """ Your code goes here """
#end of main()


# the executable part of the program
main()  # execute main()
# program terminates
