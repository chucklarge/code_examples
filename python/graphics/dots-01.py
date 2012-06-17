#!/bin/env/python
import pygame
from pygame.locals import *
import shapes_center
import sys
import math
import random

def get_pos(degree, radius, xCenter, yCenter):
  assert degree <= 360.0  # not needed mathmatically.  
  angle = math.radians(degree)
  x = xCenter + radius * math.cos(angle)
  y = yCenter + radius * math.sin(angle) 

  return ( int(x), int(y))

def main(resolution, fullscreen=False, num_objects=24, radius=300):
  #radius = int (9.0 * float(resolution[1] / num_circles))
  res_x_half = resolution[0] / 2
  res_y_half = resolution[1] / 2 
  # start everything
  pygame.init()
  if fullscreen:
    screen = pygame.display.set_mode(resolution, FULLSCREEN)
  else:
    screen = pygame.display.set_mode(resolution, DOUBLEBUF)
  pygame.mouse.set_visible(False)  
  pygame.display.set_caption("squares")

  # start everything else
  clock = pygame.time.Clock()
  pygame.display.flip() 
  while True:
    clock.tick(3)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(pygame.color.Color("black"))
    
    #randnum = random.randint(1, 100) 
    for i in range(1, 100):
      
      pos = ( random.randint(0, resolution[0]), random.randint(0, resolution[1]))  
      pygame.draw.circle(screen, pygame.color.Color("blue"), pos, 3) 
      #shapes_center.square(screen, pygame.color.Color("green"), pos, r, 4)
      #shapes_center.square(screen, pygame.color.Color("green"), pos, r/2, 4)
      #shapes_center.octagon(screen, pygame.color.Color("yellow"),   pos, r, 4)
      #shapes_center.hexagon(screen, pygame.color.Color("green"),   pos, r, 4)
    
      pygame.display.flip()

       

if __name__ == '__main__':
  #main(resolution=(1024,768), fullscreen=True, num_objects=24, radius=240)
  main(resolution=(1440,900), fullscreen=True, num_objects=128, radius=320)
  #main(resolution=(1280,1024), fullscreen=False, num_objects=24, radius=320)
