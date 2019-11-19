# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:38:13 2019

@author: 1
"""

from graph import *

def row(x, y):
    """ Рисует восемь кружочков
    """
    for i in range(8):
        circle(x, y, 20)
        x += 60

N = int(input("Enter a number using the keyboard: "))

def row_rhombus(N):
    """ Рисует N рядов по пять куружочков, каждый следующий ряд смещаеться на 
        один в право
    """
    x = 40
    y = 40
    brushColor("green")
    for i in range(N):
        for k in range(5):
            circle(x, y, 20)
            x += 60
        y += 60
        x -= 240

def row_right_triangle(N):
    """ Рисует прямоугольный трехугольник из кружочков
    """
    x = 40
    y = 40
    j = 1
    brushColor("green")
    for i in range(N):
        x = 40
        for k in range(j):
            circle(x, y, 20)
            x += 60
        j += 1
        y += 60
        
def row_isosceles_triangle(N):
    #x = 250
    y = 40
    j = 1
    for i in range(N):
        brushColor(randColor())
        x = 250 - 60 * i
        for k in range(j):
            circle(x, y, 20)
            x += 60
        j += 2
        y += 60
        i += 1
x = 20
y = 0        
def row_diamonds(x, y):
    brushColor("violet")
    polygon([(x, y), (x + 20, y + 20),
             (x, y + 40), (x - 20, y + 20), (x, y)])


def row_five_diamonds():
    global x 
    global y
    for i in range(5):
        row_diamonds(x, y)
        y += 40

def row_N_diamonds():
        global x 
        global y
        for i in range(N):
            y = 0
            i = 0
            x = x - (x * i - 1)
            row_five_diamonds()
            x += 40
            i += 1

row_N_diamonds()
#row_diamonds())
#row_isosceles_triangle(N)    
#row_right_triangle(N)           
#row_rhombus(N)    
run()