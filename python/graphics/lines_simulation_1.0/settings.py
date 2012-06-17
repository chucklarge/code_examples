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

try: import cPickle as pickle
except ImportError: import pickle
import lines, sys

try: settings = pickle.load(open('settings.conf', 'rb'))
except IOError: settings = [(640,480), True, True, [{'numpoints' : 4, 'numlines' : 3, 'minspeed' : 2, 'maxspeed' : 8, 'initialcolor' : (255,255,255), 'changecolor' : True, 'keeplines' : False}, {'numpoints' : 4, 'numlines' : 3, 'minspeed' : 2, 'maxspeed' : 8, 'initialcolor' : (255,255,255), 'changecolor' : True, 'keeplines' : False}, {'numpoints' : 4, 'numlines' : 3, 'minspeed' : 2, 'maxspeed' : 8, 'initialcolor' : (255,255,255), 'changecolor' : True, 'keeplines' : False}]]

def main_menu():
    while 1:
        print """Lines Screen Saver Settings
    0 - Quit without saving
    1 - Preview with saved settings
    2 - Change settings
    3 - Review current settings"""

        selection = raw_input('>>> ')

        try: selection = int(selection)
        except ValueError: print 'Invalid selection!'
        else:
            if selection == 0: sys.exit()
            elif selection == 1: lines.preview()
            elif selection == 2: change_settings()
            elif selection == 3: print_settings()
            else: print 'Invalid selection!'

def print_settings():
    print 'Current resolution: '+str(settings[0][0])+'x'+str(settings[0][1])
    print 'Fullscreen: '+str(settings[1])
    print 'In screensaver mode: '+str(settings[2])
    print 'Number of groups: '+str(len(settings[3]))
    raw_input('--More--')
    for i, group in enumerate(settings[3]):
        print 'Group '+str(i+1)
        print 'Number of points: '+str(group['numpoints'])
        print 'Number of lines: '+str(group['numlines'])
        print 'Maximum speed: '+str(group['maxspeed'])
        print 'Minimum speed: '+str(group['minspeed'])
        print 'Initial color: '+str(group['initialcolor'])
        print 'Changing color: '+str(group['changecolor'])
        print 'Infinite lines: '+str(group['keeplines'])
        raw_input('--More--')

def change_main_settings():
    print 'Current resolution: '+str(settings[0][0])+'x'+str(settings[0][1])
    s = None; r = None; new = []
    while s not in ('y', 'n'): s = raw_input('Change this?[y/n]: ')
    if s == 'y':
        while not r:
            try: new.append(int(raw_input('New width: ')))
            except ValueError: r = None
        while not r:
            try: new.append(int(raw_input('New height: ')))
            except ValueError: r = None
        settings[0] = new
    print 'Fullscreen: '+str(settings[1])
    s = None; r = None; new = []
    while s not in ('y', 'n'): s = raw_input('Change this?[y/n]: ')
    if s == 'y':
        s = None
        while s not in ('y', 'n'): s = raw_input('Fullscreen?[y/n]: ')
        if s == 'y': settings[1] = True
        else: settings[1] = False
    print 'In screensaver mode: '+str(settings[2])
    s = None; r = None; new = []
    while s not in ('y', 'n'): s = raw_input('Change this?[y/n]: ')
    if s == 'y':
        s = None
        while s not in ('y', 'n'): s = raw_input('Screensaver mode?[y/n]: ')
        if s == 'y': settings[2] = True
        else: settings[2] = False

def change_group_settings():
    s = None
    while s not in ('y', 'n'): s = raw_input('Add groups?[y/n]: ')
    if s == 'y':
        s = None
        while not s:
            try: s = int(raw_input('Number of new groups: '))
            except ValueError: s = None
        for i in range(s):
            group = {}
            print 'New Group '+str(i+1)
            group['numpoints'] = int(raw_input('Number of points: '))
            group['numlines'] = int(raw_input('Number of lines: '))
            group['maxspeed'] = int(raw_input('Maximum speed: '))
            group['minspeed'] = int(raw_input('Minimum speed: '))
            incolor = []
            incolor.append(int(raw_input('Initial color red[0-255]: ')))
            incolor.append(int(raw_input('Initial color green[0-255]: ')))
            incolor.append(int(raw_input('Initial color blue[0-255]: ')))
            group['initialcolor'] = incolor
            r = raw_input('Changing color?[y/n]: ')
            if r == 'y': group['changecolor'] = True
            else: group['changecolor'] = False
            r = raw_input('Keep lines?[y/n]: ')
            if r == 'y': group['keeplines'] = True
            else: group['keeplines'] = False
            settings[3].append(group)
    s = None
    while s not in ('y', 'n'): s = raw_input('Remove groups?[y/n]: ')
    if s == 'y':
        s = None
        while s != 'd':
            s = raw_input('Group to remove[1-'+str(len(settings[3]))+', d when done]: ')
            try: s = int(s)
            except ValueError:
                if s == 'd': break
            try: del settings[3][s-1]
            except IndexError: print 'Group not found.'

def change_settings():
    while 1:
        print """Change Settings
0 - Back to main menu
1 - Save current settings
2 - Change main settings
3 - Change group settings"""
        print '\nTotal groups: '+str(len(settings[3]))

        selection = raw_input('>>> ')

        try: selection = int(selection)
        except ValueError: print 'Invalid selection!'
        else:
            if selection == 0: return None
            elif selection == 1: pickle.dump(settings, open('settings.conf', 'wb'))
            elif selection == 2: change_main_settings()
            elif selection == 3: change_group_settings()
                    
if __name__ == '__main__': main_menu()
