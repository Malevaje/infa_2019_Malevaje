# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:26:30 2019

@author: 1
"""
from graph import *

def easy_hatch_Y(x1, y1, x2, y2, N):
    rectangle(x1, y1, x2, y2)
    h = (x2 - x1) / (N + 1)
    x = x1 + h
    for i in range(N):
        line(x, y1, x, y2)
        x += h

#easy_hatch_Y(10, 10, 490, 590, 50)

def easy_hatch_X(x1, y1, x2, y2, N):
    rectangle(x1, y1, x2, y2)
    h = (y2 - y1) / (N + 1)
    y = y1 + h
    for i in range(N):
        line(x1, y, x2, y)
        y += h

#easy_hatch_X(10, 10, 490, 590, 60)
from graph import *

def not_easy_hatch(x1, y1, x2, y2, N, j=0):
    """ Функция Y штрихует по y. 
        Функция X штрихует по x.
        Не обязательный коэфициент j может принимать значения:
            -1 в этом случаии штриховка только по y
             1 в этом случаии штриховка только по x
             если коэффициент j не задан штрихуеться квадрат
    """
    error = [-1, 0, 1]
    assert j in error, ("j cen take values: [0, 1 or -1]")
    hy = (y2 - y1) / (N - 1)
    hx = (x2 - x1) / (N - 1)
    def Y(x1, y1, x2, y2, N, hy):
        for i in range(N):
            line(x1, y1, x2, y2)
            y1 += hy
            y2 -= hy
    def X(x1, y1, x2, y2, N, hx):
        for k in range(N):
            line(x1, y1, x2, y2)
            x1 += hx
            x2 -= hx
    if j == -1:
        Y(x1, y1, x2, y2, N, hy)
    elif j == 1:
        X(x1, y1, x2, y2, N, hx)
    else:
        Y(x1, y1, x2, y2, N, hy)
        X(x1, y1, x2, y2, N, hx)

#not_easy_hatch(100, 100, 450, 450, 50)

def not_easy_hatch_2(x1, y1, x2, y2, x3, N):
    a = x2 - x1
    x4 = x3 + a
    hy1 = (x4 - x1) / (N - 1)
    hy2 = (x3 - x2) / (N - 1)
    line(x1, y1, x4, y1)
    line(x2, y2, x3, y2)
    for k in range(N):
        line(x2, y2, x1, y1)
        x2 += hy2
        x1 += hy1
not_easy_hatch_2(100, 100, 200, 300, 300, 50)
run()
        
        