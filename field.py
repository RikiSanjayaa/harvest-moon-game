import pygame
import random

class Field:
  # Field constant
  FIELD_WIDTH = 25
  FIELD_HEIGHT = 25
  TILE_SIZE = 32
  SHEET_ROWS = 16
  SHEET_COLS = 2
  
  TILLED_SOIL_FRAME = 4
  
  # Field Variables
  ground_tiles = []
  spritesheet = None
  reticle_sprite = None
  screen_rect = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
  tile_rect = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
  reticle_rect = pygame.Rect(383, 417, TILE_SIZE, TILE_SIZE)
  
  def __init__(self):
    for x in range(0, self.FIELD_WIDTH):
      field_row = []
      for y in range(0, self.FIELD_HEIGHT):
        field_row.append(random.randint(0, 3))
      self.ground_tiles.append(field_row)
    self.spritesheet = pygame.image.load("field-big.png")
    self.reticle_sprite = pygame.image.load("reticle-big.png")
    
  def set_reticle_pos(self, tile_x, tile_y):
    if tile_x < 0:
      tile_x = 0
    elif tile_x > self.FIELD_WIDTH:
      tile_x = self.FIELD_WIDTH
    
    if tile_y < 0:
      tile_y = 0
    elif tile_y > self.FIELD_HEIGHT:
      tile_y = self.FIELD_HEIGHT
      
    self.reticle_rect.topleft = (self.TILE_SIZE * tile_x, self.TILE_SIZE * tile_y)
    
  def till_tile(self, tile_x, tile_y):
    if self.ground_tiles[tile_x][tile_y] <= 3:
      self.ground_tiles[tile_x][tile_y] = self.TILLED_SOIL_FRAME
    
  def draw(self, screen):
    for y in range(0, self.FIELD_HEIGHT):
      for x in range(0, self.FIELD_WIDTH):
        self.screen_rect.topleft = (x * self.TILE_SIZE, y * self.TILE_SIZE)
        cur_row = self.ground_tiles[x][y] // (self.SHEET_COLS)
        cur_col = self.ground_tiles[x][y] % self.SHEET_COLS
        
        self.tile_rect.topleft = (self.TILE_SIZE * cur_col, self.TILE_SIZE * cur_row)
        screen.blit(self.spritesheet, self.screen_rect, self.tile_rect)
        screen.blit(self.reticle_sprite, self.reticle_rect)