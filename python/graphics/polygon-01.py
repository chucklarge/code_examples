#!/bin/env/python
import pygame
from pygame.locals import *
import sys
import math

def feq(a,b):
  if abs(a-b)<0.00000001: return 1
  return 0

def get_pos(degree, radius, xCenter, yCenter):
  assert degree <= 360.0  # not needed mathmatically.
  angle = math.radians(degree)
  x = xCenter + radius * math.cos(angle)
  y = yCenter + radius * math.sin(angle)

  return ( int(x), int(y))

def get_octogon_points( position, radius):
  x = position[0]
  y = position[1]

  p0 = (x - radius/2, y - radius)
  p1 = (x + radius/2, y - radius)
  p2 = (x + radius,   y - radius/2)
  p3 = (x + radius,   y + radius/2)
  p4 = (x + radius/2, y + radius)
  p5 = (x - radius/2, y + radius)
  p6 = (x - radius,   y + radius/2)
  p7 = (x - radius,   y - radius/2)

  return (p0, p1, p2, p3, p4, p5, p6, p7)

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
  d = 0
  count = 0
  degrees = [0.0] * num_circles  # array_fill
  while True:
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == QUIT or event.type == KEYDOWN:
        pygame.quit(); sys.exit();

    screen.fill(black)

#    pygame.draw.circle(screen, white, (res_x_half, res_y_half), radius, 1)

    for i in range(num_circles):
      r = (i+1) * 5
      pos  = get_pos(degrees[i], radius, res_x_half, res_y_half)
      pos2 = (pos[0]+2, pos[1]+2)
      #pygame.draw.circle(screen, blue,  pos, r, 2)
      #pygame.draw.circle(screen, green, pos2, r, 2)
      points = get_octogon_points(pos, r)
      pygame.draw.polygon(screen, green, points, 2)

    pygame.display.flip()

    # want to pause when circle 0 is at a multiple of 30deg
    # count x 20 = 1 degree ; 20 * 30 = 600
    if count % 600 ==  0:
      pygame.time.delay(1000)
    count += 1
    for i in range(num_circles):
      degrees[i]  += float(i+1) * .05
      if degrees[i] > 360.0: degrees[i] -= 360.0


if __name__ == '__main__':
  main(resolution=(1024,768), fullscreen=True, num_circles=24, radius=240)
  #main(resolution=(1440,900), fullscreen=True, num_circles=24, radius=320)
