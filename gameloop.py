import pygame
from game import Game

game = Game()

running = True
while running:
  running = game.update()
  
pygame.quit()


# TODO: 1. make more crops available
# TODO: 2. make a collision between the character and the house and bin sprite
# TODO: 3. implement the UI showing how much gold/currency the player has with the uibar.png and hmoon font
# TODO: 4. add a blank page animation to next_day function
# TODO: 5. properly documented this whole project