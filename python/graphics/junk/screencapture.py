import pygame
from pygame.locals import *
import sys
import math
 
  
pygame.init() 
screen = pygame.display.set_mode((100, 100)) 
all_colors = pygame.Surface((4096,4096), depth=24)

#
#for r in xrange(256): 
#  print r+1, "out of 256" 
#  x = (r&15)*256
#  y = (r>>4)*256 
#  for g in xrange(256):
#    for b in xrange(256): 
#      all_colors.set_at((x+g, y+b), (r, g, b))

#pygame.image.save(all_colors, "allcolors.bmp"
i = 0
while i < 5:

  for event in pygame.event.get():
    if event.type == QUIT or event.type == KEYDOWN:
      pygame.quit(); sys.exit();

  screen.fill(pygame.color.Color("black"))

  pygame.draw.circle(screen, (0,255,0), (50,50), 50, i+1) 
  pygame.display.flip()
  pa = pygame.PixelArray(screen)


  pygame.image.save(pa.make_surface(), "screen-%05d.bmp" %(i))
  i += 1
