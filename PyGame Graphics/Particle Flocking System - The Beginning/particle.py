################################################################################
############################ UTM PyGame Workshop ###############################
##############################  June 5, 2018  ##################################
################################################################################
##############################  Michael Liut  ##################################
########################## michael.liut@utoronto.ca ############################
################################################################################
#############################   particle.py   ##################################
################################################################################

# Imports
import random       # random.randint(a, b) returns a random integer N,
                    # such that a <= N <= b.
# import twoDMath     # import our custom 2D Math Library

class Particle:
    
    """
        You may set global variables for Particle in this space
    """
    # Set your global variables here


    """
        This initializes a Particle.
            For an instance of a Particle to be created, it must be given the 
            size of the Window -- i.e. maximal (X,Y) coordinates of the plane
    """
    def __init__(self, screenSizeX, screenSizeY):

        # Randomize Particle Position
        randomX = random.randint(0, screenSizeX)
        randomY = random.randint(0, screenSizeY)
        self.position = (randomX, randomY);

        # Randomize Particle Colour
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.colour = (r,g,b);

        # Randomize the Particle Size (from 1-5)
        self.size = random.randint(1, 8)

        # Particle's Range
        self.particleRange = (random.randint(0, 99) % (screenSizeX/3) + 50);

        # Particle's Speed
        self.speed = 3;
        
    """
        These are methods belonging to the Class Particle.
        Usually they are either "getters" or "setters"
    """
    # Returns the colour of the particle
    def getColour(self):
        return(self.colour)

    # Set the colour of the particle
    def setColour(self, colour):
        self.colour = colour

    # Returns the position of the particle
    def getPosition(self):
        return(self.position)

    # Set the new position of the particle
    def setPosition(self, position):
        self.position = position

    # Returns the size of the particle
    def getSize(self):
        return(self.size)

    # Set the new size of the particle
    def setSize(self, size):
        self.size = size
    
    # Returns the range of the particle
    def getRange(self):
        return(self.particleRange)


################################################################################
##################################   END   #####################################
################################################################################