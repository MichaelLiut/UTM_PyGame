import sys
import pygame
from pygame.locals import *
import random

SCREEN_SIZE = (640, 480)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# The world class keeps a list of all active entities

class World(object):
  def __init__(self):
    self.entities = []
    
  def add_player(self, entity):
    self.entities.append (entity)
    self.player = entity
  
  def add_entity(self, entity):
    self.entities.append (entity)
    
  def remove_entity (self, entity):
    self.entities.remove (entity)
    
  def process(self, time_passed):
    seconds = time_passed / 1000.0
    for entity in self.entities: # process all entities
      entity.process (seconds)
      
  def render(self, surface):
    surface.fill (BLACK) # blank the screen
    for entity in self.entities: # and render all entities
      entity.render(surface)


# Base class for game entities
# good objects, bad objects, and the player descend from this class

class GameEntity(object):
  def __init__(self, world, image, location, speed):
    self.world = world
    self.image = image
    self.location = location
    self.destination = [0, location[1]]
    self.speed = speed
    self.loop_sound()
      
  def loop_sound(self):
    pass
  
  def render(self, surface):    
    # render the entity (i.e. copy it to the screen buffer)
    x, y = self.location
    surface.blit(self.image, (x, y))
    if self != self.world.player:
      # position the entity's sound to match its position on-screen
      rvol = float(x) / SCREEN_SIZE[0]
      lvol = 1 - rvol
      if self.step_chan: self.step_chan.set_volume (lvol, rvol)

  def process(self, time_passed): 
    # movement and collision detection
    x, y = self.location
    w, h = self.image.get_width(), self.image.get_height()
    player = self.world.player
    p_x, p_y = player.location
    p_w, p_h = player.image.get_width(), player.image.get_height()
    rect1 = pygame.Rect (x, y, w, h)
    rect2 = pygame.Rect (p_x, p_y, p_w, p_h)
    if rect1.colliderect (rect2):
      self.hit_player()
      self.step.stop()
      self.world.remove_entity (self)
      return
    if self.speed > 0 and self.location != self.destination: 
      distance = abs(self.destination[0] - self.location[0])
      moved = min(distance, time_passed * self.speed)      
      self.location[0] -= moved 
    if self.location == self.destination:
      self.step.stop()
      self.world.remove_entity (self)
      

class Good(GameEntity):
  def __init__(self, world, image, location):
    speed = random.randint (50, 500)
    GameEntity.__init__ (self, world, image, location, speed)

  def hit_player (self):
    player = self.world.player
    player.hit_good()
    
  def loop_sound(self):
    self.step = pygame.mixer.Sound ('g_move.wav')
    self.step_chan = self.step.play(-1)
    if self.step_chan: self.step_chan.set_volume (0, 1)


class Bad(GameEntity):
  def __init__(self, world, image, location):
    speed = random.randint (50, 500)
    GameEntity.__init__ (self, world, image, location, speed)

  def hit_player (self):
    player = self.world.player
    player.hit_bad()
    
  def loop_sound(self):
    self.step = pygame.mixer.Sound ('b_move.wav')
    self.step_chan = self.step.play(-1)
    if self.step_chan: self.step_chan.set_volume (0, 1)


class Player(GameEntity):
  def __init__(self, world, image, location):
    self.speed = 300
    self.step = pygame.mixer.Sound ('step.wav')
    self.step_playing = False
    self.dir = 0
    self.points = 0
    self.good_hits = 0 # counter for collecting good objects
    self.bad_hits = 0 # counter for collecting bad objects
    GameEntity.__init__ (self, world, image, location, self.speed)

  def hit_good(self):
    self.points += 10
    self.good_hits += 1
    
  def hit_bad (self):
    self.points = max(self.points - 5, 0)
    self.bad_hits += 1

  def process(self, time_passed):    
    x, y = self.location
    moved = time_passed * self.speed
    moved = self.dir * moved  
    start_location = self.location[1]
    self.location[1] += moved 
    if self.location[1] < 0:
      self.location[1] = 0
    if self.location[1] > SCREEN_SIZE[1] - self.image.get_height():
      self.location[1] = SCREEN_SIZE[1] - self.image.get_height()
    if self.location[1] != start_location:
      if not self.step_playing:
        self.step_playing = True
        self.step.play (-1)
    elif self.step_playing:
      self.step_playing = False
      self.step.stop()
        
  def loop_sound(self):
    # unlike good/bad objects, the player has no constant looping sound
    pass
    
    
##### Mainline #####
      
def rand_height(h):
  return random.randint(0, h-1)


# top-level function to run/play the game

def run():
  pygame.init()
  pygame.mixer.pre_init (44100, 16, 2, 2048)
  pygame.mixer.init()
  
  screen = pygame.display.set_mode(SCREEN_SIZE)
  pygame.display.set_caption ("Scrolling Game")
    
  world = World()
  w, h = SCREEN_SIZE
  clock = pygame.time.Clock()
  u_image = pygame.image.load ('player.png')
  g_image = pygame.image.load ('good.png')
  b_image = pygame.image.load ('bad.png')
  player = Player(world, u_image, [0, 0])
  world.add_player (player)

  while True: 
    for event in pygame.event.get(): 
      if event.type == QUIT: 
        return 
      if event.type == KEYDOWN:
        if event.key == K_UP:
          player.dir = -1
        if event.key == K_DOWN:
          player.dir = 1
          
      if event.type == KEYUP:
        if event.key == K_UP or event.key == K_DOWN:
          player.dir = 0

    time_passed = clock.tick(30)
    if random.randint(1, 125) == 1:
      bad = Bad(world, b_image, [w - 1, rand_height(h)])
      world.add_entity (bad)
    if random.randint(1, 200) == 1:
      good = Good(world, g_image, [w - 1, rand_height(h)])
      world.add_entity (good)
    world.process (time_passed)
    world.render (screen)

    if pygame.font: # assuming font object is available...
        gamefont = pygame.font.Font(None, 28)
        # status bar text
        ps = "Score: " + str(player.points)
        go = "   Good Objects: " + str(player.good_hits)
        bo = "   Bad Objects: " + str(player.bad_hits)
        totals = [ps, go, bo]
        
        text = gamefont.render(' '.join(totals), True, WHITE)
        textpos = text.get_rect(centerx = SCREEN_SIZE[0] / 2, centery =
                                SCREEN_SIZE[1] - gamefont.get_height())
        screen.blit(text, textpos)
        
    pygame.display.update()

run()
