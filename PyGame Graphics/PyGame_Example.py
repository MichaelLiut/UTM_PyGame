import sys
import pygame
from pygame.locals import *

pygame.init() 	# initializes the PyGame modules

# Set a PyGame Window to a size of 640 x 480
screenSizeX = 640
screenSizeY = 480
screen = pygame.display.set_mode((screenSizeX,screenSizeY))

# Circle Creation 
centre = (100, 100)
radius = 20
colourBlue = (0, 0, 255)
pygame.draw.circle (screen, colourBlue, centre, radius)
pygame.display.update()

# Text Output
font = pygame.font.SysFont("times", 46) 
mytext = font.render ("Thanks for playing!", False, (255, 255, 255))
screen.blit (mytext, (250, 250))
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
