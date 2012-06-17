#!/bin/env/python
import pygame
from pygame.locals import *
import shapes_center
import sys
import math

def get_pos_sin(degree, radius, xCenter, yCenter, n, c):
#  assert degree <= 360.0  # not needed mathmatically.  
  theta = math.radians(degree)
  r = c + radius * math.cos(n * theta) 
  x = xCenter + r * math.cos(theta)
  y = yCenter + r * math.sin(theta) 
  return ( int(x), int(y))

def get_pos_tan(degree, radius, xCenter, yCenter, n, c):
#  assert degree <= 360.0  # not needed mathmatically.  
  theta = math.radians(degree)
  #r = radius * math.cos(n * theta) 
  r = c + radius * math.tan(n * theta) 
  x = xCenter + r * math.cos(theta)
  if x < 0: x=-5
  if x > xCenter*3: x = xCenter*2
  y = yCenter + r * math.sin(theta) 
  if y < 0: y=-5
  if y > yCenter*3: y = xCenter*3

  return ( int(x), int(y))

def get_pos_cos(degree, radius, xCenter, yCenter, n, c):
#  assert degree <= 360.0  # not needed mathmatically.  
  theta = math.radians(degree)
  r = c + radius * math.cos(n * theta) 
  #r = radius * math.sin(n * theta) 
  x = xCenter + r * math.cos(theta)
  y = yCenter + r * math.sin(theta) 

  return ( int(x), int(y))


def get_pos_square(degree, radius, xCenter, yCenter, n):
#  assert degree <= 360.0  # not needed mathmatically.  
  theta = math.radians(degree)
  rx = radius * math.cos(n * theta) 
  ry = radius * math.sin(n * theta) 
  x = xCenter + rx * math.cos(theta)
  y = yCenter + ry * math.sin(theta) 

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
  
  r_step = 0.2
  r = 50.0
  n_step = 0.002
  n = .0001   
  c = 0.0
  while True:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(pygame.color.Color("black"))
    degree = -360.0
    while degree <= 2*360:
      spos  = get_pos_sin(degree, r, res_x_half, res_y_half, n, c)
      cpos  = get_pos_cos(degree, r, res_x_half, res_y_half, n, c)
      tpos  = get_pos_tan(degree, r, res_x_half, res_y_half, n, c)
      #pygame.draw.circle(screen, pygame.color.Color("blue"), tpos, 4) 
      pygame.draw.circle(screen, pygame.color.Color("red"), spos, 3) 
      #pygame.draw.circle(screen, pygame.color.Color("green"), cpos, 4) 
      degree  += 2.0 #0.05
    pygame.display.flip()
    r += r_step
    n += n_step
    c = r 
    if (r > 500.0): r = 500.0; r_step = -0.2
    if (r < 50.0):  r = 50.0; r_step = 0.2

  
if __name__ == '__main__':
  main(resolution=(1024,768), fullscreen=True, num_objects=24, radius=240)
  #main(resolution=(1440,900), fullscreen=True, num_objects=128, radius=320)
  #main(resolution=(1280,1024), fullscreen=False, num_objects=24, radius=320)
