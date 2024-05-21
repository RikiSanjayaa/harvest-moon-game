import pygame

class Player:
  # State consts
  IDLE_STATE = 0
  MOVING_STATE = 1
  
  WALK_SPEED = 3
  
  DOWN = 0
  UP = 1
  LEFT = 2
  RIGHT = 3
  
  FRAME_SIZE = (100, 100)
  
  # Variables
  # starting position of the character
  pos_x = 400   # horizontal position 
  pos_y = 400   # vertikal position
  
  current_state = IDLE_STATE    # state of sprite
  current_direction = DOWN      # sprite view direction
  
  # rectangle to print the sprite to screen
  frame_rect = None     # rectangle position of the character from the png file
  screen_rect = None    # rectangle position of the character in the screen
  
  spritesheet = None    # the whole spritesheet
  
  def __init__(self):
    # load the spritesheet
    self.spritesheet = pygame.image.load("farmer-big.png").convert_alpha()
    # set what sprite to render based on the spritesheet
    self.frame_rect = pygame.Rect(0, 0, self.FRAME_SIZE[0], self.FRAME_SIZE[1])
    # set where the sprite is rendered on the screen
    self.screen_rect = pygame.Rect(self.pos_x, self.pos_y, self.FRAME_SIZE[0], self.FRAME_SIZE[1])
    # center the sprite
    self.screen_rect.center = (self.pos_x, self.pos_y)
    
  # function to call to draw/render the sprite to the screen, need screen as input
  def draw(self, screen):
    screen.blit(self.spritesheet, self.screen_rect, self.frame_rect)
    
  # function to call when any arrow key is pressed, update the position of character and it's direction
  def move(self, direction):
    self.current_state = self.MOVING_STATE
    if direction == self.DOWN:
      self.pos_y += self.WALK_SPEED
      self.current_direction = self.DOWN
    if direction == self.UP:
      self.pos_y -= self.WALK_SPEED
      self.current_direction = self.UP
    if direction == self.RIGHT:
      self.pos_x += self.WALK_SPEED
      self.current_direction = self.RIGHT
    if direction == self.LEFT:
      self.pos_x -= self.WALK_SPEED
      self.current_direction = self.LEFT
      
    self.screen_rect.center = (self.pos_x, self.pos_y) # update the location
    self.frame_rect.topleft = (0, 100*self.current_direction) # update the direction
      
  def stop_move(self):
    self.current_state = self.IDLE_STATE