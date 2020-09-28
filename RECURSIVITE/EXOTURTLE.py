#Turle récursif
from turtle import *

ang = 40


def trace(n, l):
    if n == 0:
        return None
    else:
        forward(l)
        left(ang)
        trace(n - 1, 0.7 * l)
        right(2 * ang)
        trace(n - 1, 0.7 * l)
        left(ang)
        forward(-l)


penup()
goto(0, -80)
pendown()
left(90)
speed(0)

trace(1, 100)