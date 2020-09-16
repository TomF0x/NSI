# Colision sans utiliser de POO
import time
import pygame
from random import randint

ecran = (640, 480)
pygame.display.init()
fenetre = pygame.display.set_mode((ecran[0], ecran[1]))
fenetre.fill([0, 0, 0])

vitesse = randint(5,10)
xa = randint(11,ecran[0]-11)
ya = randint(11,ecran[1]-11)
xb = randint(11,ecran[0]-11)
yb = randint(11,ecran[1]-11)
dxa = vitesse
dya = -vitesse
dxb = vitesse
dyb = -vitesse
couleur = (44, 170, 250)
bleu = (0, 255, 0)

while True:
    if (((xa - xb) ** 2) + ((ya - yb) ** 2)) ** 0.5 < 10:
        temp1 = dxa
        temp2 = dxb
        dxa = dxb
        dya = dyb
        dxb = temp1
        dyb = temp2
    fenetre.fill([0, 0, 0])
    pygame.draw.circle(fenetre, couleur, (xa, ya), 10)
    pygame.draw.circle(fenetre, bleu, (xb, yb), 10)
    if xa > ecran[0] - 20 or xa < 0 + 20:
        dxa = dxa * (-1)
    if ya > ecran[1] - 20 or ya < 0 + 20:
        dya = dya * (-1)
    if xb > ecran[0] - 20 or xb < 0 + 20:
        dxb = dxb * (-1)
    if yb > ecran[1] - 20 or yb < 0 + 20:
        dyb = dyb * (-1)
    xa += dxa
    ya += dya
    xb += dxb
    yb += dyb
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    time.sleep(0.01)
