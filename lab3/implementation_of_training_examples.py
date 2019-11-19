from graph import *

## Цвет линий:
#penColor("red")
#""" white, black, gray, navy, blue, cyan, green, yellow, red, orange, brown, 
#    maroon, violet, purple, ...
#"""
#
## Толщина линий
#penSize(2)
## Цвет заливки
#brushColor("green")
#""" В формате RGB цвет задаёться набором из трёх цифр от нуля до двухсот 
#    пятидесяти пяти, разделённых запятой
#"""
#penColor(0, 0, 255)
#point(200, 300)
#penColor(0, 255, 0)
#line(50, 75, 200, 150)
#penColor(255, 0, 0)
#moveTo(21, 35)
#lineTo(90, 30)
#lineTo(110, 90)
#lineTo(85, 150)
#lineTo(21, 100)
#%% Простейшие фигуры
penColor("blue")
brushColor("yellow")
rectangle(10, 20, 50, 40)
penColor("cyan")
brushColor("magenta")
polygon([(60, 10), (100, 50), (60, 50), (60, 10)])
penColor("red")
brushColor("green")
circle(120, 30, 20)
run()