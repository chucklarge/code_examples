#!/usr/bin/python

import pygame,sys,time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

size = width,height = 640,480
screen = pygame.display.set_mode(size,pygame.OPENGL | pygame.DOUBLEBUF)

glLoadIdentity()
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0,100,0,100)
glMatrixMode(GL_MODELVIEW)

glClearColor(0,0,0,0)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pass
        elif event.type == MOUSEMOTION:
            pass

    glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
    glColor(255,0,0)
    glBegin(GL_LINES)
    glVertex(0,0)
    glVertex(100,100)
    glEnd()
    glFlush()
    pygame.display.flip()

pygame.quit()

