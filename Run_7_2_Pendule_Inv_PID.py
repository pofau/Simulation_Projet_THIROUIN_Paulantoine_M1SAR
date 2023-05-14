#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:29:12 2023

@author: pofau
"""
from class_vecteur3D import Vecteur3D
from class_particule import Particule
from class_force import *
from class_univers import Univers
from class_PID import PIDController
from math import pi
import pygame
from pylab import show, legend, title
import matplotlib.pyplot as plt

#taille fenêtre
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000

#création du prisme
p1masse = 0.1
prisme = Prisme(Vecteur3D(1,0,0))

#création des particules
p1 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule1', color="Yellow", fixe = False, prisme=[prisme])
p1.addPosition0(Vecteur3D(0.3,0.4, 0))
    
p2 = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule2', color='Green', fixe = False)
p2.addPosition0(Vecteur3D(0.3,0.5, 0))
    
#création des tiges rigides
l0 = (p1.getPosition()-p2.getPosition()).mod()
 
T = Tige()
r1 = Rod([p1, p2])

#création de la viscosité et de la gravité
g1 = gravite(Vecteur3D(0,-9.81,0))
visc = Viscosite(0.000018)

#création de l'univers
dt = 0.00001
u3 = Univers(dt = dt)

#ajout des forces et des agents
u3.addGenerateur(r1)
u3.addGenerateur(visc)
u3.addGenerateur(g1)
u3.addAgent(p1)
u3.addAgent(p2)

#création et ajout du PID
PID = PIDController(150, 50, 10, dt = dt, p1 = p1, p2 = p2, start = pi/2)
u3.addGenerateur(PID)

#Simulation pygame
u3.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)
    
run = True
    
while u3.run :
        
    pygame.event.pump() # process event queue
    keys = pygame.key.get_pressed() 
    
    if keys[ord('q')] or keys[pygame.K_LEFT]: 
        p2.setForce(Vecteur3D(-0.1,0,0))
        print('left')

    elif keys[ord('d')] or keys[pygame.K_RIGHT]: 
        p2.setForce(Vecteur3D(0.1,0,0))  
        print('right')
                     
    else :
        p2.setForce(Vecteur3D(0,0,0))
        p2.setSpeed(Vecteur3D(0,0,0))          
    u3.gameUpdate()


plt.figure(2)
u3.plot2D()
title("X en fonction de Y")
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
legend()
show()

plt.figure(3)
T = u3.axeTemps()
plt.plot(T,p1.angleTheta(p2))
plt.xlabel("T(s)")
plt.ylabel("Theta")
plt.title("Theta en fonction du temps")
plt.show()

pygame.quit()  
sys.exit()