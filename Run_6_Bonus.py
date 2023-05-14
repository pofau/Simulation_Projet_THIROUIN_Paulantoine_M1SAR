#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:59:01 2023

@author: pofau
"""

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

def randomMR(nb, p1masse, Univers):
    """fonction qui créé des pendules
    """

    k = 10000
    c = 0
    x_start = 0.1
    x_final = 0.9
    dx = (x_final - x_start)/nb
    
    #Création des particules
    p = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='bati', color="white", fixe = True)
    p.addPosition0(Vecteur3D(x_start,0.3, 0))
    p_list = []
    r_list = []
    p_list.append(p)
    
    for i in range(1,nb):
        p = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='particule'+str(i), color="white")
        p.addPosition0(Vecteur3D(0.1 + dx * i,0.3, 0))
        p_list.append(p)
        
        l0 = (p_list[-1].getPosition()-p_list[-2].getPosition()).mod() 
        r = Ressort_Amortisseur(k, c, l0=l0, particules = [p_list[-2], p_list[-1]])
        r_list.append(r)
        
    p = Particule(vitesse=Vecteur3D(0,0,0),masse=p1masse,name='bati', color="white", fixe = True)
    p.addPosition0(Vecteur3D(x_final,0.3, 0))
    p_list.append(p)
    
    l0 = (p_list[-1].getPosition()-p_list[-2].getPosition()).mod() 
    r = Ressort_Amortisseur(k, c, l0=l0, particules = [p_list[-2], p_list[-1]])
    r_list.append(r)
    
    print(Univers)
    print()
    for p1 in p_list :
        Univers.addAgent(p1)
    
    for r1 in r_list :
        Univers.addGenerateur(r1)
        print()
        print(Univers)


    #création des pulsations propres
    omega_1 = np.sqrt((k )/p1masse)
    omega_2 = np.sqrt((nb*k)/p1masse)
    return p_list, omega_1, omega_2

#taille de l'univers et de pygame
fenêtre_x = 1
fenêtre_y = 0.7
scale = 1000

#création des particules
dt = 0.00001
p1masse = 1
nb = int(input("Entrez le nombre de ressort : "))

#création de l'univers
u3 = Univers(dt = dt)
# http://res-nlp.univ-lemans.fr/NLP_E_M01_G04/co/NLP_E_M01_G04_15.html

p, omega_1, omega_2 = randomMR(nb, p1masse, u3)


#simulation pygame
u3.gameInit(fenêtre_x*scale, fenêtre_y*scale, background='gray', scale=scale)
    
run = True
while u3.run :
    if u3.gameKeys[K_ESCAPE] :
        u3.run = False
    if u3.gameKeys[ord('q')] or u3.gameKeys[pygame.K_LEFT]:
        # Activez la force constante et désactivez la force harmonique
        fh = Force_Harmonique(Vecteur3D(1,0, 0), etat=True, omega=omega_1, u = [u3], particule=[p[1]])
        u3.addGenerateur(fh)
        print("en phase")

    elif u3.gameKeys[ord('d')] or u3.gameKeys[pygame.K_RIGHT]:
        # Activez la force harmonique et désactivez la force constante
        fh = Force_Harmonique(Vecteur3D(1,0, 0), etat=True, omega= omega_2, u = [u3], particule=[p[1]])
        u3.addGenerateur(fh)
        print("opposition de phase")

    u3.gameUpdate()


pygame.quit()        
sys.exit()

