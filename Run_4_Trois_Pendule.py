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

#création de la tige
tige = Tige()
coeff_tige = tige.setCoeff()

#Création du pendule 1
p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="green", fixe = True)
p1.addPosition0(Vecteur3D(0.5,0.5,0))

p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='red')
l1 = 0.1
p2.addPosition0(Vecteur3D(0.5-l1,0.5,0))

r1 = Ressort_Amortisseur(raideur=coeff_tige[0], c=coeff_tige[1], l0=l1, particules = [p1, p2])

u1.addGenerateur(r1)
u1.addAgent(p1)
u1.addAgent(p2)

#Création du pendule 2
p3 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule3', color="green", fixe = True)
p3.addPosition0(Vecteur3D(0.5,0.5,0.1))

p4 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule4', color='blue')
l2 = 0.2
p4.addPosition0(Vecteur3D(0.5-l2,0.5,0))
r2 = Ressort_Amortisseur(raideur=coeff_tige[0], c=coeff_tige[1], l0=l2, particules = [p3, p4])

u1.addGenerateur(r2)
u1.addAgent(p3)
u1.addAgent(p4)

#Création du pendule 3
p5 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule5', color="green", fixe = True)
p5.addPosition0(Vecteur3D(0.5,0.5,0.2))

p6 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule6', color='yellow')
l3 = 0.3 
p6.addPosition0(Vecteur3D(0.5-l3,0.5,0))

r3 = Ressort_Amortisseur(raideur=coeff_tige[0], c=coeff_tige[1], l0=l3, particules = [p5, p6])

u1.addGenerateur(r3)
u1.addAgent(p5)
u1.addAgent(p6)


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
    
plt.figure(1)
T = u1.axeTemps()
X = p2.axePosition(1)
plt.plot(T,X)

T = u1.axeTemps()
X = p4.axePosition(1)
plt.plot(T,X)
plt.xlabel("t(s)")
plt.ylabel("X(m)")
plt.title("X en fonction du temps")

T = u1.axeTemps()
X = p6.axePosition(1)
plt.plot(T,X)
plt.show()

plt.figure(2)
u1.plot2D()
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.title("X en fonction de Y")
legend()
show()

plt.figure(3)
plt.plot(T,p1.angleTheta(p2))
plt.plot(T,p3.angleTheta(p4))
plt.plot(T,p5.angleTheta(p6))
plt.xlabel("T(s)")
plt.ylabel("Theta")
plt.title("Theta en fonction du temps")
plt.legend(["L1", "L2", "L3"])  # Ajoutez les étiquettes souhaitées correspondant à chaque plot
plt.show()


pygame.quit()        
sys.exit()