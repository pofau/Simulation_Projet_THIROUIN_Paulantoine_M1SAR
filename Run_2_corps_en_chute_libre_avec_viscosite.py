#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:28:57 2023

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


def random_Particule(univers, p1masse, fenêtre_x, fenêtre_y):
    """fonction qui créé des particules aléatoirement dans l'espace
    """
    x = random.uniform(0, fenêtre_x)
    y = random.uniform(0, fenêtre_y)
    z = 0
    vx = random.uniform(0, 20)
    vy = random.uniform(0, 20)
    vz = 0
    particule = Particule(name='name1',masse=p1masse, position = Vecteur3D(x,y,z), vitesse=Vecteur3D(vx, vy, vz))
    univers.addAgent(particule)
        
#Taille de l'univers et de la fenêtre pygame
fenêtre_x = 100
fenêtre_y = 70
scale = 10

pmasse = 1

#création de l'univers
dt = 0.001
u1 = Univers(dt = dt)

#ajout des forces de gravité et de v iscosité
g1 = gravite(Vecteur3D(0,-9.81,0))
visc = Viscosite(0.01)
u1.addGenerateur(g1)
u1.addGenerateur(visc)


#Simulation Pygame
u1.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)

run = True
while u1.run :
    
    if u1.gameKeys[K_ESCAPE] :
        u1.run = False
        
    elif u1.gameKeys[K_SPACE] :
        random_Particule(u1, pmasse, fenêtre_x, fenêtre_y)

    u1.gameUpdate()


pygame.quit()        
u1.plot2D()
title("Corps en chute libre avec viscosité")
plt.xlabel("x")
plt.ylabel("y")
legend()
show()
sys.exit()

    


