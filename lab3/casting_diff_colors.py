# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:31:43 2019

@author: 1
"""

from graph import *

def grayscale(x1, y1, x2, y2, N):
    x = x1
    c = 255
    h = (x2 - x1) / (N + 1)
    hc = 255 // N
    for i in range(N):
        penColor(c, c, c)
        brushColor(c, c, c)
        rectangle(x, y1, x + h, y2)
        x += h
        c -= hc
#grayscale(100, 100, 450, 450, 50)

def grayscale_2(x1, y1, x2, y2, N):
    y = y1
    c = 0
    h = (y2 - y1) / (N + 1)
    hc = 255 // N
    for i in range(N):
        penColor(c, c, c)
        brushColor(c, c, c)
        rectangle(x1, y, x2, y + h)
        y += h
        c += hc
#grayscale_2(100, 100, 450, 450, 50)

from graph import *

def diff_reds_color(x1, y1, x2, y2, N):
    hx = (x2 - x1) / (N + 1)
    hy = (y2 - y1) / (N + 1)
    R = 0; G = 0; B = 0
    hR = 255 // N
    x = x1 + hx
    y = y1 + hy
    for i in range(N):
        penColor(R, G, B)
        brushColor(R, G, B)
        polygon([(x1, y - hy), (x1, y),  (x, y),
                (x - hx, y - hy), (x1, y - hy)])   
        x += hx
        y += hy
        R += hR
        
#diff_reds_color(100, 100, 400, 400, 255)
        
def diff_circle(N):
    hR = 255 // N
    h = 150
    R = 255; G = 255; B = 0
    for i in range(N):
        brushColor(R, G, B)
        circle(250, 250, h)
        R -= hR
        G -= hR
        B += hR
        h -= 15

#diff_circle(10)    

def red_arrow(x1, y1, x2, y2, N):
    hx = (x2 - x1) / (N + 1)
    hy = (y2 - y1) / (N + 1)
    R = 255; G = 0; B = 0
    y3 = y2 + (y2 - y1)
    hR = 255 // N
    for i in range(N):
        penColor(R, G, B)
        brushColor(R, G, B)
        polygon([(x1, y1), (x1, y3), (x1 + hx, y3 - hy), (x1 + hx, y1 + hy), 
                 (x1, y1)])
        x1 += hx
        y1 += hy
        y3 -= hy
        R -= hR
    R = 0
    penColor(R, G, B)
    brushColor(R, G, B)
    polygon([(x1, y1), (x1, y3), (x1 + hx, y2), (x1, y1)])
    
        
red_arrow(10, 100, 450, 250, 255)







run()