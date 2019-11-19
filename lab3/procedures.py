# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:00:24 2019

@author: 1
"""
from graph import *


def triangle(x, y, c):
    brushColor(c)
    polygon([(x, y), (x, y - 60),
             (x + 100, y), (x, y)])

    
def triangle2(x, y, c):
    brushColor(c)
    polygon([(x, y), (x + 100, y),
             (x, y + 60), (x, y)])
    
def triangle3(x, y, c):
    brushColor(c)
    polygon([(x, y), (x - 30, y - 40),
             (x + 30, y - 40), (x, y)])

def triangle4(y, dx):
    brushColor("green")
    polygon([(250, y), (250 + dx, y + 40),
             (250 - dx, y + 40), (250, y)])

def crown(x, y, dx, dy, RGB):
    brushColor(RGB)
    polygon([(x, y), (x + 50 + dx, y + 250 + dy),
             (x - 50 + dx, y + 250 + dy), (x, y)])
    circle(x, y, 15)

penColor("black")
brushColor("brown")
crown(400, 60, -120, -30, "green")
crown(100, 60, 120, -30, "blue")
crown(250, 30, 0, 0, "red")
#rectangle(240, 190, 260, 280)
#triangle4(200, 130)
#triangle4(170, 110)
#triangle4(140, 90)
#triangle4(110, 70)
#triangle4(80, 50)
#triangle4(50, 30)
run()