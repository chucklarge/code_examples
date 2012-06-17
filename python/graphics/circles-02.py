#!/bin/env/python
import pygame
from pygame.locals import *
import sys
import math

def get_pos(degree, radius, xCenter, yCenter):
  assert degree <= 360.0  # not needed mathmatically.
  angle = math.radians(degree)
  x = xCenter + radius * math.cos(angle)
  y = yCenter + radius * math.sin(angle)

  return ( int(x), int(y))

def main(resolution, fullscreen=False, num_circles=24, radius=300):
  #radius = int (9.0 * float(resolution[1] / num_circles))
  res_x_half = int(resolution[0]/2)
  res_y_half = int(resolution[1]/2)
  # start everything
  pygame.init()
  if fullscreen:
    screen = pygame.display.set_mode(resolution, FULLSCREEN)
  else:
    screen = pygame.display.set_mode(resolution, DOUBLEBUF)
  pygame.mouse.set_visible(False)
  pygame.display.set_caption("circles")

  # start everything else
  clock = pygame.time.Clock()
  pygame.display.flip()

  black  = (0, 0, 0)
  red    = (255, 0, 0)
  green  = (0, 255, 0)
  blue   = (0, 0, 255)
  yellow = (0, 120, 255)
  white  = (255, 255, 255)
  degrees = [0.0] * num_circles  # array_fill
  while True:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(black)

    pygame.draw.circle(screen, white, (res_x_half, res_y_half), radius, 1)

    for i in range(num_circles):
      r = (i+1) * 5
      pos  = get_pos(degrees[i], radius, res_x_half, res_y_half)
      pos2 = (pos[0]+2, pos[1]+2)
      pygame.draw.circle(screen, blue,  pos, r, 2)
      pygame.draw.circle(screen, green, pos2, r, 2)

    for i in range(num_circles):
      degrees[i]  += float(i+1) * .05
      if degrees[i] > 360.0: degrees[i] -= 360.0

    pygame.display.flip()

if __name__ == '__main__':
  main(resolution=(1440,900), fullscreen=True, num_circles=32, radius=300)
