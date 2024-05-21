import pygame
from player import Player

pygame.init()

# Game consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()

run = True
while run:
  # Run game at 60 FPS
  clock.tick(60)
  
  screen.fill((255,255,255))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
  player.draw(screen)

  pygame.display.flip()
    

pygame.quit()