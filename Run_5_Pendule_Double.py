#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:45:02 2023

@author: pofau
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:15:19 2023

@author: pofau
"""

from class_vecteur3D import Vecteur3D
from class_particule import Particule
from class_torseur import Torseur
from class_force import Force_Harmonique, Ressort_Amortisseur, force_Ponctuelle, Tige, Tige_CDM, gravite, force_const, Viscosite, Attracteur
from class_univers import Univers
import random
import numpy as np
import matplotlib.pyplot as plt
import sys
from math import pi,atan2
import pygame
from pylab import show, legend, title, plot
from pygame.locals import *
import random
import numpy as np

#Création de la taille de l'univers et de pygame
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000


#création de l'univers
dt = 0.00001
u1 = Univers(dt = dt)
p1masse = 10

#création d'une tige
tige = Tige()
coeff_tige = tige.setCoeff()

#création des longueurs du pendule
l1 = 0.15
l2 = 0.1

#Création des particules de liaison pour le pendule
p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="green", fixe = True)
p1.addPosition0(Vecteur3D(0.5,0.5,0))

p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='red')
p2.addPosition0(Vecteur3D(0.5-l1,0.5,0))

p3 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule3', color="yellow")
p3.addPosition0(Vecteur3D(0.5-(l1+l2),0.5,0))

T = Tige()

#création des fils : hypothèse d'un ressort-amortisseur par les petits angles
r1 = Ressort_Amortisseur(T.setCoeff()[0], c = T.setCoeff()[1], l0=l1, particules = [p1, p2])
r2 = Ressort_Amortisseur(T.setCoeff()[0], c = T.setCoeff()[1], l0=l2, particules = [p2, p3])

#r1 = Ressort_Amortisseur(T.setCoeff()[0], c = 10, l0=l1, particules = [p1, p2])
#r2 = Ressort_Amortisseur(T.setCoeff()[0], c = 10, l0=l2, particules = [p2, p3])

g1 = gravite(Vecteur3D(0,-9.81, 0))

#Ajout des forces
u1.addGenerateur(r1)
u1.addGenerateur(r2)
u1.addGenerateur(g1)

#Ajout des agents
u1.addAgent(p1)
u1.addAgent(p2)
u1.addAgent(p3)

#simulation pygame
u1.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)

run = True
while u1.run:
    if u1.gameKeys[K_ESCAPE]:
        u1.run = False

    u1.gameUpdate()
    
plt.figure(1)
T = u1.axeTemps()
X = p2.axePosition(1)
plt.plot(T,X)

T = u1.axeTemps()
X = p3.axePosition(1)
plt.plot(T,X)
plt.xlabel("t(s)")
plt.ylabel("X(m)")
plt.title("X en fonction du temps")
show()

plt.figure(2)
u1.plot2D()
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.title("x en fonction de y")
legend()
show()

pygame.quit()  
sys.exit()

