#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:09:13 2023

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


def random_position(nb_particule, univers, fenêtre_x, fenêtre_y, pmasse):
    """fonction qui renvoie une liste de particule généré avec des positions aléatoires dans le plan
    """
    list_particule = []
    
    for i in range(nb_particule):
        x = random.uniform(0, fenêtre_x)
        y = random.uniform(0, fenêtre_y)
        z = fenêtre_y
        name1 = "particule" + str(i)
        position = Vecteur3D(x, y, z)
        particule = Particule(name=name1, position=position, masse=pmasse)
        univers.addAgent(particule)
        list_particule.append(particule)
        
    return list_particule


#Taille Univers et fenêtre pygame
fenêtre_x = 10
fenêtre_y = 7
scale = 100

#Création de l'univers
dt = 0.0001
u1 = Univers(dt = dt)

#Création de la liste des particules
pmasse = 1
nb_particule = 10
list_particule = random_position(nb_particule, u1, fenêtre_x, fenêtre_y, pmasse)

#Attracteur de champ
attract = Particule(name='attracteur', color = 'red', position=Vecteur3D(fenêtre_x/2, fenêtre_y/2, -5), masse=pmasse, fixe = True)
u1.addAgent(attract)
a1 = Attracteur(0.5, Vecteur3D(fenêtre_x/2, fenêtre_y/2, -5))
u1.addGenerateur(a1)

#Ajout de la gravité
g1 = gravite(Vecteur3D(0,0,-9.81))
u1.addGenerateur(g1)

#Simulation Pygame
u1.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)
run = True
while u1.run :
    if u1.gameKeys[K_ESCAPE] :
        u1.run = False
    u1.gameUpdate()


pygame.quit()        
u1.plot3D()
title("Corps en chute libre avec attracteur")
plt.xlabel("x")
plt.ylabel("y")
legend()
show()
sys.exit()

    


