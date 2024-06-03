import pygame
from field import Field

class Player:
  # State consts
  IDLE_STATE = 0
  MOVING_STATE = 1
  USING_STATE = 2
  SWITCHING_STATE = 3
  
  WALK_SPEED = 3
  RUN_SPEED = 6
  
  DOWN = 0
  UP = 1
  LEFT = 2
  RIGHT = 3
  
  FRAME_SIZE = (100, 100)
  TOOL_FRAME_SIZE = (32, 32)
  TOOL_OFFSET = (-40, -50)
  TILE_SIZE = 32
  
  # Tool consts
  HOE = 0
  WATERING_CAN = 1
  # SICLE = 2
  # HAMMER = 3
  # AXE = 4
  TURNIP_SEED = 5
  
  # Tool vars
  cur_tool = 0
  tools = [HOE, WATERING_CAN, TURNIP_SEED]
  tool_frame_rect = pygame.Rect(0, 0, TOOL_FRAME_SIZE[0], TOOL_FRAME_SIZE[1])
  tool_screen_rect = pygame.Rect(0, 0, TOOL_FRAME_SIZE[0], TOOL_FRAME_SIZE[1])
  
  # Animations
  WALK_DURATION = 6
  RUN_DURATION = 4
  IDLE_ANIMATION = [(0, 60)]
  WALK_ANIMATION = [(0, WALK_DURATION), (1, WALK_DURATION), (0, WALK_DURATION), (2, WALK_DURATION)]
  RUN_ANIMATION = [(0, RUN_DURATION), (3, RUN_DURATION), (0, RUN_DURATION), (4, RUN_DURATION)]
  TILLING_ANIMATION = [(12, 15), (13, 4), (14, 8), (15, 30)]
  WATERING_ANIMATION = [(16, 15), (17, 30), (16, 7)]
  SOW_ANIMATION = [(18, 10), (19, 10), (20, 10), (21, 10), (22, 30)]
  TOOL_SWITCH_ANIMATION = [(11, 45)]
  
  TILLING_FRAME = 14
  
  # Variables
  field = None
  
  # starting position of the character
  pos_x = 400   # horizontal position 
  pos_y = 400   # vertikal position
  
  current_state = IDLE_STATE    # state of sprite
  current_direction = DOWN      # sprite view direction
  
  current_frame = 0
  current_animation = None
  
  frame_counter = 0
  current_duration = 0
  animation_index = 0
  
  tile_x = 0
  tile_y = 0
  reticle_x = 0
  reticle_y = 0
  
  running = False
  
  # rectangle to print the sprite to screen
  frame_rect = None     # rectangle position of the character from the png file
  screen_rect = None    # rectangle position of the character in the screen
  
  spritesheet = None    # the whole spritesheet
  tool_sheet = None
  
  def __init__(self, f):
    self.field = f
    # load the spritesheet
    self.spritesheet = pygame.image.load("farmer-big.png").convert_alpha()
    self.tool_sheet = pygame.image.load("tools-big.png").convert_alpha()
    # set what sprite to render based on the spritesheet
    self.frame_rect = pygame.Rect(0, 0, self.FRAME_SIZE[0], self.FRAME_SIZE[1])
    # set where the sprite is rendered on the screen
    self.screen_rect = pygame.Rect(self.pos_x, self.pos_y, self.FRAME_SIZE[0], self.FRAME_SIZE[1])
    # center the sprite
    self.screen_rect.center = (self.pos_x, self.pos_y)
    self.set_animation(self.IDLE_ANIMATION)
    
  # function to call to draw/render the sprite to the screen, need screen as input
  def draw(self, screen):
    screen.blit(self.spritesheet, self.screen_rect, self.frame_rect)
    
    if self.current_state == self.SWITCHING_STATE:
      screen.blit(self.tool_sheet, self.tool_screen_rect, self.tool_frame_rect)
    
  # function to call when changing the frame of the sprite
  def set_frame(self, frame):
    self.current_frame = frame
    cur_row = self.current_direction
    cur_col = self.current_frame
    
    self.frame_rect.topleft = (cur_col * self.FRAME_SIZE[0], cur_row * self.FRAME_SIZE[1])
  
  def next_frame(self):
    self.current_frame = self.current_animation[self.animation_index][0]
    self.current_duration = self.current_animation[self.animation_index][1]
    self.on_frame()
    
  def set_animation(self, animation):
    self.current_animation = animation
    self.animation_index = 0
    
    self.frame_counter = 0
    self.next_frame()
    self.set_frame(self.current_frame)
    
  def update_animation(self):
    self.frame_counter += 1
    
    if self.frame_counter >= self.current_duration:
      self.frame_counter = 0
      self.animation_index += 1
      if self.animation_index >= len(self.current_animation):
        self.animation_index = 0
        if self.current_state == self.USING_STATE:
          self.current_state = self.IDLE_STATE
          self.set_animation(self.IDLE_ANIMATION)
          return
      self.next_frame()
      self.set_frame(self.current_frame)
      
  def next_tool(self):
    if self.current_state != self.IDLE_STATE and self.current_state != self.MOVING_STATE:
      return
    self.current_state = self.SWITCHING_STATE
    self.cur_tool += 1
    if self.cur_tool >= len(self.tools):
      self.cur_tool = 0
    self.set_animation(self.TOOL_SWITCH_ANIMATION)
    
    self.tool_frame_rect.topleft = (self.tools[self.cur_tool] * self.TOOL_FRAME_SIZE[0], 0)
    self.tool_screen_rect.topleft = (self.pos_x + self.TOOL_OFFSET[0], self.pos_y + self.TOOL_OFFSET[1])
      
  def use_tool(self):
    self.current_state = self.USING_STATE
    if self.tools[self.cur_tool] == self.HOE:
      self.set_animation(self.TILLING_ANIMATION)
    elif self.tools[self.cur_tool] == self.WATERING_CAN:
      self.set_animation(self.WATERING_ANIMATION)
    elif self.tools[self.cur_tool] == self.TURNIP_SEED:
      self.set_animation(self.SOW_ANIMATION)
  
  # function to call when any arrow key is pressed, update the position of character and it's direction
  def move(self, direction):
    speed = 0
    if self.current_state == self.USING_STATE:
      return
    
    if self.running:
      speed = self.RUN_SPEED
    else:
      speed = self.WALK_SPEED
    
    if self.current_state != self.MOVING_STATE:
      self.current_state = self.MOVING_STATE
      if self.running:
        self.set_animation(self.RUN_ANIMATION)
      else:
        self.set_animation(self.WALK_ANIMATION)
    
    if direction == self.DOWN:
      self.current_direction = self.DOWN
      if self.pos_y <= 780:
        self.pos_y += speed
    elif direction == self.UP:
      self.current_direction = self.UP
      if self.pos_y >= 20:
        self.pos_y -= speed
    elif direction == self.RIGHT:
      self.current_direction = self.RIGHT
      if self.pos_x <= 780:
        self.pos_x += speed
    elif direction == self.LEFT:
      self.current_direction = self.LEFT
      if self.pos_x >= 20:
        self.pos_x -= speed
            
    self.screen_rect.center = (self.pos_x, self.pos_y) # update the location
    self.update_tile_position()
    self.field.set_reticle_pos(self.reticle_x, self.reticle_y)
      
  def stop_move(self):
    if self.current_state == self.MOVING_STATE:
      self.current_state = self.IDLE_STATE
      self.set_animation(self.IDLE_ANIMATION)
    
  def start_running(self):
    self.running = True
    self.set_animation(self.RUN_ANIMATION)
      
  def stop_running(self):
    self.running = False
    if self.current_state == self.MOVING_STATE:
      self.set_animation(self.WALK_ANIMATION)
    else:
      self.set_animation(self.IDLE_ANIMATION)
    
  def update(self):
    self.update_animation()
    
  def update_tile_position(self):
    self.tile_x = self.pos_x // self.TILE_SIZE
    self.reticle_x = self.tile_x
    if self.current_direction == self.LEFT:
      self.reticle_x -= 1
    elif self.current_direction == self.RIGHT:
      self.reticle_x += 1
      
    self.tile_y = self.pos_y // self.TILE_SIZE
    self.reticle_y = self.tile_y
    if self.current_direction == self.UP:
      self.reticle_y -= 1
    elif self.current_direction == self.DOWN:
      self.reticle_y += 1
    
  def on_frame(self):
    if self.current_frame == self.TILLING_FRAME:
      self.field.till_tile(self.reticle_x, self.reticle_y)