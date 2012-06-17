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
  pygame.display.flip()
  count = 0
  clock_tick = 30 
  degrees1 = [0.0] * num_objects  # array_fill 
  degrees2 = [180.0] * num_objects  # array_fill 
  while True:
    clock.tick(clock_tick)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    #screen.fill(pygame.color.Color("midnightblue"))
    screen.fill( (0,0,40) )

#    pygame.draw.circle(screen, (0,255,0), (res_x_half, res_y_half), radius, 1)
   
    for i in range(num_objects):
      r = (i+1) * 5   
      pos  = get_pos(degrees1[i], radius, res_x_half, res_y_half)
      shapes_center.triangle_down(screen, pygame.color.Color("white"),   pos, r, 2)
  
      pos  = get_pos(degrees2[i], radius, res_x_half, res_y_half)
      shapes_center.triangle_down(screen, (255,0,155),   pos, r, 2)
    
    pygame.display.flip()

    # want to pause when circle 0 is at a multiple of 30deg
    # count x 20 = 1 degree ; 20 * 30 = 600
#    if count % (20 * clock_tick) ==  0:
#      pygame.time.delay(1000)    
#    count += 1


    for i in range(num_objects):
      degrees1[i]  += float(i+1) * .05
      if degrees1[i] > 360.0: degrees1[i] -= 360.0
    
      degrees2[i]  -= float(i+1) * .05
      if degrees2[i] < 0.0: degrees2[i] += 360.0
   

if __name__ == '__main__':
  #main(resolution=(1024,768), fullscreen=True, num_objects=24, radius=240)
  main(resolution=(1440,900), fullscreen=True, num_objects=32, radius=300)
  #main(resolution=(1280,1024), fullscreen=False, num_objects=24, radius=320)
