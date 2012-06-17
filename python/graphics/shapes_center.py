import pygame
from math import sqrt

def octagon(screen, color, center_position, radius, width):
  x,y = center_position
  side_a = int (float(radius) * 0.923879533)  # sin 22.5 deg = 0.923879533
  side_b = int (float(radius) * 0.382683432)  # cos 22.5 deg = 0.382683432
 
  p0 = (x - side_b,   y - side_a)
  p1 = (x + side_b,   y - side_a)
  p2 = (x + radius,   y - side_b)
  p3 = (x + radius,   y + side_b)
  p4 = (x + side_b,   y + side_a)
  p5 = (x - side_b,   y + side_a)
  p6 = (x - radius,   y + side_b)
  p7 = (x - radius,   y - side_b)

  points = (p0, p1, p2, p3, p4, p5, p6, p7)
  pygame.draw.polygon(screen, color, points, width)    


def hexagon(screen, color, center_position, radius, width):
  x,y = center_position
  side_a = int( sqrt( float( radius*radius) - float(radius*radius) / 4.0 ) )  

  p0 = (x - radius/2,  y - side_a)
  p1 = (x + radius/2,  y - side_a)
  p2 = (x + radius,    y)
  p3 = (x + radius/2,  y + side_a)
  p4 = (x - radius/2,  y + side_a)
  p5 = (x - radius,    y)
  
  points = (p0, p1, p2, p3, p4, p5)
  pygame.draw.polygon(screen, color, points, width)    


def square(screen, color, center_position, radius, width):
  x,y = center_position
  rect = ((x-radius, y-radius), (2*radius, 2*radius))
  pygame.draw.rect(screen, color, rect, width)

def square2(screen, color, center_position, radius, width):
  x,y = center_position
  rect = ((x-radius/2, y-radius/2), (radius, radius))
  pygame.draw.rect(screen, color, rect, width)


def triangle_down(screen, color, center_position, radius, width):
  x,y = center_position
  y -= int(float(radius) / 4.0)
  side_a = int(float(radius) * 0.5)         # sin 30 deg = 0.5
  side_b = int(float(radius) * 0.866025404) # cos 30 deg = 0.866025404 
 
  p0 = (x - side_b,   y - side_a)
  p1 = (x + side_b,   y - side_a)
  p2 = (x, y + radius)

  points = (p0, p1, p2)
  pygame.draw.polygon(screen, color, points, width)

