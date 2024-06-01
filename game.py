import pygame
from player import Player
from field import Field

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
field = Field()
player = Player(field)

run = True
while run:
  # Run game at 60 FPS
  clock.tick(60)
  
  screen.fill((255,255,255))
  
  # detect any key pressed while game is running
  key = pygame.key.get_pressed()
  if key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
    player.move(DOWN)
  if key[pygame.K_UP] == True  or key[pygame.K_w] == True:
    player.move(UP)
  if key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
    player.move(LEFT)
  if key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
    player.move(RIGHT)
    
  # stop move if no key is pressed
  if (key[pygame.K_DOWN] == False and key[pygame.K_UP] == False and
      key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and
      key[pygame.K_w] == False and key[pygame.K_s] == False and
      key[pygame.K_a] == False and key[pygame.K_d] == False):
    player.stop_move()
  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
      player.use_tool()
    
    # listen to hold l shift key
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
      player.start_running()
    elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
      player.stop_running()
    
    # quit the game
    if event.type == pygame.QUIT:
      run = False
      
  # update code
  player.update()
      
  field.draw(screen)
  player.draw(screen)

  pygame.display.flip()
    

pygame.quit()