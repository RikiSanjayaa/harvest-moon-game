import pygame
from player import Player
from field import Field

pygame.init()

class Game:
  # Game consts
  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 800

  DOWN = 0
  UP = 1
  LEFT = 2
  RIGHT = 3

  def __init__(self):
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.field = Field()
    self.player = Player(self)
    
  def set_reticle_pos(self, tile_x, tile_y):
    self.field.set_reticle_pos(tile_x, tile_y)
    
  def till_tile(self, tile_x, tile_y):
    self.field.till_tile(tile_x, tile_y)
  
  def sow_tile(self, tile_x, tile_y):
    self.field.sow_tile(tile_x, tile_y)
  
  def water_tile(self, tile_x, tile_y):
    self.field.water_tile(tile_x, tile_y)
    
  def use_tile(self, tile_x, tile_y):
    return self.field.use_tile(tile_x, tile_y)
  
  def drop_item(self, tile_x, tile_y, item_type):
    return self.field.drop_item(tile_x, tile_y, item_type)
    
  def update(self):
      # Run game at 60 FPS
      self.clock.tick(60)
      
      # detect any key pressed while game is running
      key = pygame.key.get_pressed()
      if key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
        self.player.move(self.DOWN)
      if key[pygame.K_UP] == True  or key[pygame.K_w] == True:
        self.player.move(self.UP)
      if key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
        self.player.move(self.LEFT)
      if key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
        self.player.move(self.RIGHT)
        
      # stop move if no key is pressed
      if (key[pygame.K_DOWN] == False and key[pygame.K_UP] == False and
          key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and
          key[pygame.K_w] == False and key[pygame.K_s] == False and
          key[pygame.K_a] == False and key[pygame.K_d] == False):
        self.player.stop_move()
      
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
          self.player.use_tool()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
          self.player.next_tool()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
          self.player.use_hand()
        
        # listen to hold l shift key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
          self.player.start_running()
        elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
          self.player.stop_running()
        
        # quit the game
        if event.type == pygame.QUIT:
          return False
          
      # update code
      self.player.update()
      self.screen.fill((255,255,255))
          
      self.field.draw(self.screen)
      self.player.draw(self.screen)
      
      pygame.display.flip()
      return True