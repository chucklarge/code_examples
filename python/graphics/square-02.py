#!/bin/env/python
import pygame
from pygame.locals import *
import shapes_center
import sys
import math

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
  count = 0
  clock_tick = 30 
  degrees = [0.0] * num_objects  # array_fill 
  while True:
    clock.tick(clock_tick)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(pygame.color.Color("black"))
    
#    pygame.draw.circle(screen, white, (res_x_half, res_y_half), radius, 1)
    
    for i in range(num_objects):
      r = (i+1) * 5   
      pos  = get_pos(degrees[i], radius, res_x_half, res_y_half)
      pos2 = (pos[0]+2, pos[1]+2)
      pygame.draw.circle(screen, pygame.color.Color("blue"),    pos, r, 2) 
      #pygame.draw.circle(screen, pygame.color.Color("green"),   pos2, r, 2) 
      #shapes_center.square(screen, pygame.color.Color("green"), pos, r, 2)
      #shapes_center.square(screen, pygame.color.Color("green"), pos, r/2, 2)
      #shapes_center.octagon(screen, pygame.color.Color("yellow"),   pos, r, 2)
      #shapes_center.hexagon(screen, pygame.color.Color("green"),   pos, r, 2)
    
    pygame.display.flip()

    # want to pause when circle 0 is at a multiple of 30deg
    # count x 20 = 1 degree ; 20 * 30 = 600
    
#    if count % (20 * clock_tick) ==  0:
#      pygame.time.delay(1000)    
#    count += 1

    for i in range(num_objects):
      degrees[i]  += float(i+1) * .05
      if degrees[i] > 360.0: degrees[i] -= 360.0
       

if __name__ == '__main__':
  main(resolution=(1920,1080), fullscreen=True, num_objects=90, radius=240)
  #main(resolution=(1440,900), fullscreen=True, num_objects=180, radius=320)
  #main(resolution=(1280,1024), fullscreen=False, num_objects=24, radius=320)
