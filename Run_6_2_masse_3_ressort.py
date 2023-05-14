#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:05:32 2023

@author: pofau
"""

from class_vecteur3D import Vecteur3D
from class_particule import Particule
from class_torseur import Torseur
from class_force import Force_Harmonique, Ressort_Amortisseur, force_Ponctuelle, Tige, Tige_CDM, gravite, force_const, Viscosite, Attracteur
from class_univers import Univers
import random

import sys
from math import pi,atan2
import pygame
from pylab import show, legend, title, plot
from pygame.locals import *
import random
import numpy as np
import matplotlib.pyplot as plt

#taille de l'univers et de pygame
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000

#création des particules
dt = 0.00001
p1masse = 1
    
p0 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='bati', color="white", fixe = True)
p0.addPosition0(Vecteur3D(0.1,0.3, 0))
    
p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="green")
p1.addPosition0(Vecteur3D(0.2,0.3, 0))
    
p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='red')
p2.addPosition0(Vecteur3D(0.3,0.3, 0))

p3 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='bâti', color='white', fixe = True)
p3.addPosition0(Vecteur3D(0.4,0.3, 0))

#création du ressort
l0 = (p0.getPosition()-p1.getPosition()).mod() 

k = 10000
K2 = k 
c = 0

r0 = Ressort_Amortisseur(k, c, l0=l0, particules = [p0, p1])
r1 = Ressort_Amortisseur(K2, c, l0=l0, particules = [p1, p2])
r2 = Ressort_Amortisseur(k, c, l0=l0, particules = [p2, p3])


#création de l'univers
u3 = Univers(dt = dt)
# http://res-nlp.univ-lemans.fr/NLP_E_M01_G04/co/NLP_E_M01_G04_15.html

#création des pulsations propres
omega_1 = np.sqrt((k )/p1masse)
omega_2 = np.sqrt((3*k)/p1masse)


u3.addGenerateur(r0)
u3.addGenerateur(r1)
u3.addGenerateur(r2)

u3.addAgent(p0)
u3.addAgent(p1)
u3.addAgent(p2)
u3.addAgent(p3)

#simulation pygame
u3.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)
    
run = True
while u3.run :
    if u3.gameKeys[K_ESCAPE] :
        u3.run = False
    if u3.gameKeys[ord('q')] or u3.gameKeys[pygame.K_LEFT]:
        # Activez la force constante et désactivez la force harmonique
        fh = Force_Harmonique(Vecteur3D(0.1,0, 0), etat=True, omega=omega_1, u = [u3], particule=[p2])
        u3.addGenerateur(fh)
        print("en phase")

    elif u3.gameKeys[ord('d')] or u3.gameKeys[pygame.K_RIGHT]:
        # Activez la force harmonique et désactivez la force constante
        fh = Force_Harmonique(Vecteur3D(0.1,0, 0), etat=True, omega= omega_2, u = [u3], particule=[p2])
        u3.addGenerateur(fh)
        print("opposition de phase")

    u3.gameUpdate()


pygame.quit()        

plt.figure(1)
T = u3.axeTemps()
X = p1.axePosition(1)
plot(T,X)

T = u3.axeTemps()
X = p2.axePosition(1)
plot(T,X)

plt.xlabel("t(s)")
plt.ylabel("X(m)")
plt.title("X en fonction du temps")
legend()
show()

pygame.quit()        
sys.exit()

