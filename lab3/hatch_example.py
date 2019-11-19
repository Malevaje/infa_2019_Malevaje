# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:32:08 2019

@author: 1
"""
from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10

rectangle(x1, y1, x2, y2)

h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
    line(x, y1, x, y2)
    x += h

x1 = 50; y1 = 20
x2 = 10; y2 = 90
a = x1 - x2
x3 = 90
N = 9
polygon([(x1, y1), (x2, y2), (x3, y2), (x3 + a, y1), (x1, y1)])
h = (x3 - x2) / (N + 1)
x = x1 + h
for i in range(N):
    line(x, y1, x - a, y2)
    x += h


x1 = 20; y1 = 10
x2 = 100; y2 = 85
N = 7
hx = (x2 - x1) / (N + 1)
hy = (y2 - y1) / (N + 1)

polygon([(x1, y1), (x1, y2), (x2, y2), (x1, y1)])
x = x1 + hx
y = y1 + hy
for i in range(N):
    line(x1, y + hy, x + hx, y + hy)
    x += hx
    y += hy

run()
