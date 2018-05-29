################################################################################
############################ UTM PyGame Workshop ###############################
##############################  June 5, 2018  ##################################
################################################################################
##############################  Michael Liut  ##################################
########################## michael.liut@utoronto.ca ############################
################################################################################
###############################   main.py   ####################################
################################################################################

"""
To install PyGame: "python3 -m pip install -U pygame --user"
PyGame Documentation: https://www.pygame.org/docs/
"""

# Package Imports
import pygame
from pygame.locals import *
import sys 			# not required for PyGame, but useful for exiting windows
import particle 	        # this is a class that student's must build
import random		        # for acquiring a random integer N


"""
GLOBAL VARIABLES
"""
# Total number of particles to be created
global totalParticles
totalParticles = 500

# Particle List -- referring to Class Particle
global particleList
particleList = []

# PyGame Window
global screen

# Create Particle Function
def createParticle(screenSizeX, screenSizeY):
	
	# Initialize particle 
	newParticle = particle.Particle(screenSizeX,screenSizeY)
	
	# Creating a circle shape with the arguments: (screen, color, position, radius, thickness)
	pygame.draw.circle(screen, newParticle.getColour(), newParticle.getPosition(), newParticle.getSize(), newParticle.getSize())

	return(newParticle)

# Update Particle Function
def updateParticle(newParticle):
	
	# Creating a circle shape with the arguments: (screen, color, position, radius, thickness)
	pygame.draw.circle(screen, newParticle.getColour(), newParticle.getPosition(), newParticle.getSize(), newParticle.getSize())


# Action occurs on mouse event on Left Click
def leftClick(coordinate):
	print("LEFT CLICK WAS PRESSED")

	screen.fill(pygame.Color("black"))				# need to clear the screen

	# Generate random range to "flock" from
	particleRangeFromClick = (random.randint(0, 99) % (screenSizeX/3) + 50)

	for i in range (0, len(particleList)):
		position = particleList[i].getPosition()	# Particle's Tuple Position
		particleX = position[0]  					# Particle's X-coordinate
		particleY = position[1]  					# Particle's Y-coordinate

		particleX -= coordinate[0]	# remove the distance between click
		particleY -= coordinate[1]	# remove the distance between click

		# in the event the distance between the click and the particle is 
		# within the random range, we will alter the particle's location
		if ((particleX <= particleRangeFromClick) and (particleY <= particleRangeFromClick)):
			particleX -= 10
			particleY -= 10
			particleList[i].setPosition((particleX,particleY))
		
		updateParticle(particleList[i])		# update all particles
		pygame.display.update()				# refresh the PyGame Window

# Action occurs on mouse event on Right Click
def rightClick(coordinate):
	print("RIGHT CLICK WAS PRESSED")

"""
Let's call these 'global values'
"""

pygame.init() 	# initializes the PyGame modules

# Set a PyGame Window to a size of 640 x 480
screenSizeX = 640
screenSizeY = 480
screen = pygame.display.set_mode((screenSizeX,screenSizeY))

# Give the PyGame Window a name
pygame.display.set_caption('Particle Flocking System')

# Particle Group -- a PyGame Sprite Group
# particleGroup = pygame.sprite.Group()

"""
Some Notes:
	- The point (0,0) is on the top left corner of the plane/screen.
	- X-axis increases from left-to-right, Y-axis increases from top-to-bottom
	- All changes to the screen must be updated: pygame.display.update()
"""

colour = (0,0,0)				# operates with RGB, max value of 255.
screen.fill(colour)				# sets the screen colour to black
pygame.display.update()			# refresh the PyGame Window

for i in range (0, totalParticles):
	particleList.append(createParticle(screenSizeX,screenSizeY))
	# newParticle = createParticle(screen,screenSizeX,screenSizeY)
	# particleList.append(newParticle[0])
	# particleGroup.add(newParticle[1])

while (True):

	pygame.display.update()		# refresh the PyGame Window
	# pygame.event.wait() 		# waits on an action event before looping again

	# get all user 'events'
	for event in pygame.event.get():

        # for a button click event (i.e. key is pressed down)
		if event.type == pygame.KEYDOWN:
			
			if event.key == K_q:				# on 'q' quit application
				pygame.quit(); sys.exit();
			if event.key == K_ESCAPE:			# on 'escape; quit application
				pygame.quit(); sys.exit();

        # for a mouse click event
		if event.type == pygame.MOUSEBUTTONDOWN:
			occurance = pygame.mouse.get_pressed()		# returns a triple type
        								# (left, centre, right)
        	
			coordinate = pygame.mouse.get_pos()			# get (X,Y) coordinate
			print(coordinate)
        	
        	# Left Click
			if (occurance[0] == True):
				leftClick(coordinate)
        	# Right Click
			elif (occurance[2] == True):
				rightClick(coordinate)

		# to quit the application
		if event.type == pygame.QUIT:
        	# and the game close the window
			pygame.quit(); sys.exit();

################################################################################
##################################   END   #####################################
################################################################################
