#!/bin/env/python
import pygame
from pygame.locals import *
import sys
from random import *       
import math

def random_pos():
  return (randint(0,639), randint(0,479))

def random_size():
  return (639-randint(random_pos[0],639), 479-randint (random_pos[1],479))

def get_pos(degree):
  if (degree < 0.0): degree = 360.0 + degree
  angle = math.radians(degree)
  radius = 300
  xCenter = 720
  yCenter = 450 
  x = xCenter + radius * math.cos(angle)
  y = yCenter + radius * math.sin(angle) 

  return ( int(x), int(y))


def main(resolution, fullscreen=False):
  # start everything
  pygame.init()
  if fullscreen:
    screen = pygame.display.set_mode(resolution, FULLSCREEN)
  else:
    screen = pygame.display.set_mode(resolution, DOUBLEBUF)
  pygame.mouse.set_visible(False)  
  pygame.display.set_caption("Chuck")

  # start everything else
  clock = pygame.time.Clock()
  pygame.display.flip()
  
  size = (100, 100)
  black  = (0, 0, 0)
  red    = (255, 0, 0)
  green  = (0, 255, 0)
  blue   = (0, 0, 255)
  yellow = (0, 120, 255)
  white  = (255, 255, 255)
  delta  = 0
  num_circles = 20;
  degrees = [0.0] * num_circles
  while True:
    clock.tick(30)

    for event in pygame.event.get():
      #print  "%d %d" %  (KEYDOWN, event.type)
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(black)
    pos = (100,100) # random_pos()

#   pygame.draw.circle(screen, white, (720, 450), 300, 1)
    
    for i in range(num_circles):
      r = (i+1) * 5;   
      pygame.draw.circle(screen, green,  get_pos(degrees[i]), r, 2) 
    
    #pygame.draw.circle(screen, red,     get_pos(degrees[1]), 30, 3) 
    #pygame.draw.circle(screen, green,   get_pos(degrees[2]), 40, 3) 
    #pygame.draw.circle(screen, blue,    get_pos(degrees[3]), 50, 3) 
    
    for i in range(num_circles):
      degrees[i]  += float(i+1) * .05
      if degrees[i] > 360.0: degrees[i] = 360.0 + degrees[i]
       
    pygame.display.flip()

if __name__ == '__main__':
  main(resolution=(1440,900), fullscreen=True)
