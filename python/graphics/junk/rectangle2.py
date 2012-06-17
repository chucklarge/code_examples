import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

color = (255,255,255)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

  random_pos = (randint(0,639), randint(0,479))
  random_size = (639-randint(random_pos[0],639), 479-randint (random_pos[1],479))

  screen.fill((0, 0, 0))
  pygame.draw.rect(screen, color, Rect(random_pos, random_size))
  pygame.display.update()
  #pygame.time.wait(500)
  pygame.time.delay(200)
