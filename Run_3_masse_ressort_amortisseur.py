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
import matplotlib.pyplot as plt

#Taille de l'univers et de la fenêtre pygame
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000


#Création de l'univers
dt = 0.00001
u1 = Univers(dt = dt)

#Création des particules
p1masse = 10

p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="green", fixe = True)
p1.addPosition0(Vecteur3D(0.5,0.4,0))

p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='red')
p2.addPosition0(Vecteur3D(0.5,0.3,0))

#Création du ressort
l0 = (p1.getPosition()-p2.getPosition()).mod() 
r1 = Ressort_Amortisseur(raideur=10000, c=10., l0=l0, particules = [p1, p2])

#Ajout du ressort et des particules à l'univers
u1.addGenerateur(r1)
u1.addAgent(p1)
u1.addAgent(p2)


#Simulation pygame
u1.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)

run = True
while u1.run:
    if u1.gameKeys[K_ESCAPE]:
        u1.run = False
    
    if u1.gameKeys[ord('q')] or u1.gameKeys[pygame.K_LEFT]:
        # Activez la force constante et désactivez la force harmonique
        fh = force_const(Vecteur3D(0, 1, 0), [p1, p2],etat=True)
        u1.addGenerateur(fh)


    elif u1.gameKeys[ord('d')] or u1.gameKeys[pygame.K_RIGHT]:
        # Activez la force harmonique et désactivez la force constante
        fh = Force_Harmonique(Vecteur3D(0, 1, 0), etat=True, omega=0.05, u = [u1], particule=[p1, p2])
        u1.addGenerateur(fh)
    
        

    u1.gameUpdate()

T = u1.axeTemps()
X = p2.axePosition(2)
plt.plot(T,X)
title("Masse-Ressort-Amortisseur")
plt.xlabel("t(s)")
plt.ylabel("Y(m)")
legend()
show()

pygame.quit()        
sys.exit()
