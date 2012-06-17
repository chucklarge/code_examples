import pygame 
from pygame.locals import * 
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

red_scale_surface = pygame.surface.Surface((640, 480)) 

c = int((40/639.)*255.) 
red = (c, 0, 0) 
line_rect = Rect( 10, 0, 1, 480) 
pygame.draw.rect(red_scale_surface, red, line_rect) 
    
color = [127, 127, 127] 

while True:
  for event in pygame.event.get(): 
    if event.type == QUIT:
      exit() 
    
  screen.fill((0, 0, 0))
  # Draw the scales to the screen 
  screen.blit(red_scale_surface, (0, 00)) 
    
  pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240)) 
  pygame.display.update()
