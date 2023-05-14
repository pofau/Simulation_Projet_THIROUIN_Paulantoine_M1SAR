#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:38:08 2023

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
    
def randomPendule(nb, p1masse):
    """fonction qui créé des pendules
    """
    for i in range(nb):
        #création de la tige
        tige = Tige()
        coeff_tige = tige.setCoeff()

        #Création du pendule 1
        p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="green", fixe = True)
        p1.addPosition0(Vecteur3D(0.5,0.5,0))

        p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='red')
        l1 = i/100
        p2.addPosition0(Vecteur3D(0.5-l1,0.5,0))

        r1 = Ressort_Amortisseur(raideur=coeff_tige[0], c=coeff_tige[1], l0=l1, particules = [p1, p2])

        u1.addGenerateur(r1)
        u1.addAgent(p1)
        u1.addAgent(p2)
        
#Création de la taille de l'univers et de pygame
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000

#création de l'univers
dt = 0.0001
u1 = Univers(dt = dt)
p1masse = 10

nb = 15
randomPendule(nb, p1masse)

#Ajout de la gravité
g1 = gravite(Vecteur3D(0,-9.81, 0))
u1.addGenerateur(g1)


#Simulation de pygame
u1.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)

run = True
while u1.run:
    if u1.gameKeys[K_ESCAPE]:
        u1.run = False

    u1.gameUpdate()

pygame.quit()        
sys.exit()