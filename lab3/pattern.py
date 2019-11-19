# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:13:39 2019

@author: 1
"""

from graph import *

N = int(input("Enter a number using the keyboard: "))

def row_pattern_tile(x, y):

    brushColor("violet")
    for i in range(3):
        polygon([(x, y), (x + 20, y + 20),
                 (x, y + 40), (x - 20, y + 20), (x, y)])
        y += 40
        
    y1 = y - 80
    x1 = x - 40
    for j in range(2):
        polygon([(x1, y1), (x1 + 20, y1 + 20),
                 (x1, y1 + 40), (x1 - 20, y1 + 20), (x1, y1)])
        x1 += 80
    return x, y

def row_pave_tiles(N):
    x = 60
    y = 0
    for i in range(N):
        row_pattern_tile(x, y)
        x += 120
    

row_pave_tiles(N)
















run()