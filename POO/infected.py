import time
from random import randint

import pygame

from graph import graphique

ecran = (640, 480)
pygame.display.init()
fenetre = pygame.display.set_mode((ecran[0], ecran[1]))
fenetre.fill([0, 0, 0])
start = time.time()

t = []
nb = []


class Balle:
    def __init__(self, infect):
        self.size = 10
        self.couleur = (0, 255, 0)
        self.x = randint(0, ecran[0] - self.size)
        self.y = randint(0, ecran[1] - self.size)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        self.infecte = infect

    def actu(self):
        if self.infecte:
            self.couleur = (255, 0, 0)
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.size)
        self.x += self.dx
        self.y += self.dy
        if self.x > ecran[0] - self.size or self.x < 0 + self.size:
            self.dx = self.dx * (-1)
        if self.y > ecran[1] - self.size or self.y < 0 + self.size:
            self.dy = self.dy * (-1)
        for balle in listeballe:
            if self.x != balle.x and self.y != balle.y:
                if (((self.x - balle.x) ** 2) + ((self.y - balle.y) ** 2)) ** 0.5 < self.size + balle.size:
                    if self.infecte:
                        balle.infecte = True
                    if balle.infecte:
                        self.infecte = True
                    temp1 = self.dy
                    temp2 = self.dx
                    self.dy = balle.dy
                    self.dx = balle.dx
                    balle.dy = temp1
                    balle.dx = temp2


listeballe = [Balle(False) for i in range(20)]
listeballe.append(Balle(True))
total = 0
nombrecycle = 0
while True:
    fenetre.fill([0, 0, 0])
    for i in range(len(listeballe)):
        listeballe[i].actu()
        if listeballe[i].infecte:
            total += 1
    if total == len(listeballe):
        print("Les {0} balles sont toutes infectées après {1}s".format(len(listeballe), time.time() - start))
        t.append(time.time() - start)
        nb.append(len(listeballe))
        listeballe.clear()
        listeballe = [Balle(False) for i in range(total + 10)]
        listeballe.append(Balle(True))
        start = time.time()
        nombrecycle += 1
        if nombrecycle == 10:
            graphique(t, nb)
            break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    pygame.display.flip()
    time.sleep(0.01)
    total = 0
