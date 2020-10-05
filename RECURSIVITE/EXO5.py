#Exercice 5
#Dessin récursif
from turtle import *

def dessin(t):
    for i in range(4):
        forward(t)
        left(90)
    penup();forward(t/2);pendown()
    left(45)
    dessin(t/2**0.5)

penup();goto(-200, -200);pendown()
dessin(400)