import pygame 
from pygame.locals import * 
from sys import exit
from random import *

def main():
  pygame.init() 
  screen = pygame.display.set_mode((640, 480), DOUBLEBUF )
  pygame.display.set_caption("Chuck")

  clock = pygame.time.Clock()
  pygame.display.flip()
  
  color = (255,200,034)
  while True:
    #clock.tick(30)
    for event in pygame.event.get(): 
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    
    random_pos = (randint(0,639), randint(0,479)) 
    random_size = (639-randint(random_pos[0],639), 479-randint (random_pos[1],479))
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, Rect(random_pos, random_size))
    pygame.display.update()
    pygame.time.delay(200)

if __name__ == '__main__':
  main()
