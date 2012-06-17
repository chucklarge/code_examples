#!/bin/env/python
#
#    This file is part of Lines Simulation.
#
#    Lines is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Lines.  If not, see <http://www.gnu.org/licenses/>.
from pygame.locals import *
import pygame, random, sys

class Point(pygame.sprite.Sprite):
    """ A movable point """
    def __init__(self, x, y, dx, dy, screensize, maxspeed=10, minspeed=2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1)); self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x; self.y = y
        self.dx = dx; self.dy = dy
        self.maxspeed = 5; self.lock = screensize
        self.minspeed = minspeed
    def move(self, x, y):
        self.x = x
        self.y = y
    def update(self):
        # calculate next position
        if self.x >= self.lock[0]:
            self.x = self.lock[0]
            if self.dx > 0: self.dx = -random.randint(self.minspeed, self.maxspeed)
            elif self.dx < 0: self.dx = random.randint(self.minspeed, self.maxspeed)
        elif self.x <= 0:
            self.x = 0
            if self.dx > 0: self.dx = -random.randint(self.minspeed, self.maxspeed)
            elif self.dx < 0: self.dx = random.randint(self.minspeed, self.maxspeed)
        if self.y >= self.lock[1]:
            self.y = self.lock[1]
            if self.dy > 0: self.dy = -random.randint(self.minspeed, self.maxspeed)
            elif self.dy < 0: self.dy = random.randint(self.minspeed, self.maxspeed)
        elif self.y <= 0:
            self.y = 0
            if self.dy > 0: self.dy = -random.randint(self.minspeed, self.maxspeed)
            elif self.dy < 0: self.dy = random.randint(self.minspeed, self.maxspeed)
        self.x += self.dx
        self.y += self.dy
        # move to next position
        self.rect.x = self.x
        self.rect.y = self.y

class PointGroup(pygame.sprite.Sprite):
    """ A collection of points connected by a line. """
    def __init__(self, screensize, points, color, numlines, changecolor=True, keeplines=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(screensize)
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        self.points = points
        self.curcolor = color
        self.change = changecolor
        self.keeplines = keeplines
        self.numlines = numlines
        self.pastpoints = []
        self.pointlist = []
        self.target = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

    def nextcolor(self, target, current, speed):
        next = []
        for i in range(3):
            if abs(current[i] - target[i]) < speed: next.append(target[i])
            elif current[i] < target[i]: next.append(current[i]+speed)
            elif current[i] > target[i]: next.append(current[i]+-speed)
        return next

    def update(self):
        self.points.update()
        self.pointlist = []
        for point in self.points.sprites():
            self.pointlist.append((point.x, point.y))
        self.pastpoints.append(self.pointlist)
        if len(self.pastpoints) > self.numlines:
            if not self.keeplines: pygame.draw.lines(self.image, (0,0,0), True, self.pastpoints[0])
            self.pastpoints = self.pastpoints[1:]
        if self.curcolor == self.target: self.target = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        if self.change: self.curcolor = self.nextcolor(self.target, self.curcolor, 1)
        pygame.draw.lines(self.image, self.curcolor, True, self.pointlist)
        
def main(resolution, pointgroups, fullscreen=False, screensaver=False):
    # start everything
    pygame.init()
    if fullscreen: screen = pygame.display.set_mode(resolution, FULLSCREEN)
    else: screen = pygame.display.set_mode(resolution, DOUBLEBUF)
    pygame.display.set_caption("Lines")
    pygame.mouse.set_visible(0)
    # make points groups
    groups = pygame.sprite.Group()
    for group in pointgroups:
        points = pygame.sprite.Group()
        for i in range(group['numpoints']):
            point = Point(random.randint(0, resolution[0]), random.randint(0, resolution[1]),
                          random.randint(group['minspeed'], group['maxspeed']), random.randint(group['minspeed'], group['maxspeed']),
                          resolution, group['maxspeed'], group['minspeed'])
            points.add(point)
        pointgroup = PointGroup(resolution, points, group['initialcolor'],
                                group['numlines'], group['changecolor'], group['keeplines'])
        groups.add(pointgroup)
    # draw the groups onto the screen
    groups.update()
    groups.draw(screen)
    # get the initial mouse position (used for screensavers)
    mousepos = pygame.mouse.get_pos()
    # start everything else
    clock = pygame.time.Clock()
    pygame.display.flip()

    while 1:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and screensaver:
                pygame.quit()
                sys.exit()

        if screensaver and mousepos != pygame.mouse.get_pos():
            pygame.quit()
            sys.exit()

        screen.fill((0,0,0))
        groups.update()
        groups.draw(screen)
        pygame.display.flip()

def preview():
    try: import cPickle as pickle
    except ImportError: import pickle
    settings = pickle.load(open('settings.conf', 'rb'))
    try: main(settings[0], settings[3], settings[1], settings[2])
    except: return None

if __name__ == '__main__':
  groups = [{'numpoints'    : 4,
             'numlines'     : 3,
             'minspeed'     : 2,
             'maxspeed'     : 8,
             'initialcolor' : (255,255,255),
             'changecolor'  : True,
             'keeplines'    : False},
            {'numpoints'    : 4,
             'numlines'     : 3,
             'minspeed'     : 2,
             'maxspeed'     : 8,
             'initialcolor' : (255,255,255),
             'changecolor'  : True,
             'keeplines'    : False},
            {'numpoints'    : 4,
             'numlines'     : 3,
             'minspeed'     : 2,
             'maxspeed'     : 8,
             'initialcolor' : (255,255,255),
             'changecolor'  : True,
             'keeplines'    : False}]
  main(resolution=(1024,768), pointgroups=groups, fullscreen=True, screensaver=True)
