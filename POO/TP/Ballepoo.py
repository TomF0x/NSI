import time
from random import randint

import pygame

ecran = (640, 480)
pygame.display.init()
fenetre = pygame.display.set_mode((ecran[0], ecran[1]))
fenetre.fill([0, 0, 0])


class Balle:
    def __init__(self):
        self.couleur = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.size = randint(8, 15)
        self.x = randint(self.size, ecran[0] - self.size)
        self.y = randint(self.size, ecran[1] - self.size)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.size)

    def actu(self):
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
                    temp1 = self.dy
                    temp2 = self.dx
                    self.dy = balle.dy
                    self.dx = balle.dx
                    balle.dy = temp1
                    balle.dx = temp2


listeballe = [Balle() for i in range(10)]

while True:
    fenetre.fill([0, 0, 0])
    for i in range(len(listeballe)):
        listeballe[i].actu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    pygame.display.flip()
    time.sleep(0.01)
