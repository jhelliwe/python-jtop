#!/usr/bin/python

import os

def termsize():
    size = os.get_terminal_size() 
    width=size[0]
    height=size[1]
    return width, height
