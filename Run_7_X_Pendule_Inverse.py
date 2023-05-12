#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:29:12 2023

@author: pofau
"""
from class_vecteur3D import Vecteur3D
from class_particule import Particule
from class_torseur import Torseur
from class_force import Force_Harmonique, Ressort_Amortisseur, force_Ponctuelle, Tige, Tige_CDM, gravite, force_const, Viscosite, Attracteur, Prisme, Rod
from class_univers import Univers
#from class_PID import PIDController
import random
import sys
from math import pi,atan2
import pygame
from pylab import show, legend, title, plot
from pygame.locals import *
import random
import numpy as np
import matplotlib.pyplot as plt

#taille fenêtre pygame et univers
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000

#création des particules
p1masse = 0.1
p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="white", fixe = False, prisme=[])
p1.addPosition0(Vecteur3D(0.299999,0.4, 0))
    
p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='Green', fixe = False)
p2.addPosition0(Vecteur3D(0.3,0.5, 0))
    
#création des tiges
l0 = (p1.getPosition()-p2.getPosition()).mod()    
T = Tige()
r1 = Rod([p1, p2])

#création de la gravité
g1 = gravite(Vecteur3D(0,-9.81,0),  p2)

#création de l'univers
dt = 0.0001
u3 = Univers(dt = dt)

#ajout des forces et agents
u3.addGenerateur(r1)
u3.addGenerateur(g1)
u3.addAgent(p1)
u3.addAgent(p2)

#simulation pygame
u3.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)
run = True
    
while u3.run :
        
    pygame.event.pump() # process event queue
    keys = pygame.key.get_pressed() 
    
    if keys[ord('q')] or keys[pygame.K_LEFT]: 
        p1.setForce(Vecteur3D(-0.02,0,0))
        print('left')

    elif keys[ord('d')] or keys[pygame.K_RIGHT]: 
        p1.setForce(Vecteur3D(0.02,0,0))  
        print('right')
            
    elif keys[ord('z')] or keys[ord('s')] or keys[pygame.K_DOWN]: 
        p1.setForce(Vecteur3D(0,0,0))
        p1.setSpeed(Vecteur3D(0,0,0))  

        print('right')
            
    else :
        p1.setForce(Vecteur3D(0,0,0))
            
    u3.gameUpdate()

plt.figure(1)
T = u3.axeTemps()
X = p2.axePosition(1)
plt.plot(T,X)

plt.xlabel("t(s)")
plt.ylabel("X(m)")
plt.title("X en fonction du temps")
show()

plt.figure(2)
u3.plot2D()
title("X en fonction de Y")
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
legend()
show()

pygame.quit()  
sys.exit()