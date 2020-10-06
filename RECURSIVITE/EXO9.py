from turtle import *
import time

def floc(n,l):
    if n==0:
        forward(l)
    else:
        floc(n-1,l/3)
        left(60)
        floc(n-1,l/3)
        right(120)
        floc(n-1,l/3)
        left(60)
        floc(n - 1, l / 3)
goto(-100,100)
speed(0)
for i in range(3):
    floc(5,500)
    right(120)
time.sleep(5)