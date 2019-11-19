# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:41:03 2019

@author: 1
"""
from graph import *

def row_pattern_1(x, y):
    brushColor("violet")
    polygon([(x, y), (x + 60, y + 60), (x, y + 60), (x + 60, y), (x, y)])


def row_pattern_2(x, y):
    brushColor("violet")
    polygon([(x, y), (x + 60, y + 60), (x + 60, y), (x, y + 60), (x, y)])

x = -60
y = 0
k = 1
while k < 15:
    if k % 2 == 1:
        x = -60
        for i in range(4):
            x += 60
            row_pattern_1(x, y)
            x += 60
            row_pattern_2(x, y)
    else:
        x = -60
        for i in range(4):
            x += 60
            row_pattern_2(x, y)
            x += 60
            row_pattern_1(x, y)
    y += 60
    k += 1
    

    


run()