#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL3) 
# Version: 1.0 - 23/Jun/2012

import pygame
from pygame.locals import *
import sys

class Control:
    '''
    User interaction class. 
    '''
    def __init__(self,CONF):
        return

# Check keyboard or mouse clicks and return without waiting
    def check_user_action(self):
        for event in pygame.event.get() :

            if event.type == pygame.KEYDOWN: # KEYBOARD
                key_name = pygame.key.name(event.key)
                key_mods=pygame.key.get_mods()
                if key_mods & KMOD_LSHIFT and key_name == 'escape':
                    sys.exit(0)
                return "K",key_name,key_mods
        return "N"
 
# Stop until user press a key or a mouse button
    def wait_for_user_action(self):
        while True:
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN: # KEYBOARD
                    key_name = pygame.key.name(event.key)
                    key_mods=pygame.key.get_mods()
                    if key_mods & KMOD_LSHIFT and key_name == 'escape':
                        sys.exit(0)
                    return "K",key_name,key_mods

                if event.type == pygame.MOUSEBUTTONDOWN: # MOUSE
                    return "M",event.pos, event.button


