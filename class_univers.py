#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:14:52 2023

@author: pofau
"""

from class_vecteur3D import Vecteur3D
from class_particule import Particule
from class_torseur import Torseur
from class_force import Force_Harmonique, Ressort_Amortisseur, force_Ponctuelle, Tige, Tige_CDM, gravite, force_const, Viscosite, Attracteur
import sys
from math import pi,atan2
import pygame
from pylab import show, legend, title, plot
from pygame.locals import *
import random
import numpy as np
import matplotlib.pyplot as plt

###class Univers
class Univers(object) :
    """classe qui applique des forces sur des particules pendant un espace de temps dt
    c'est le moteur du simulateur
    """
    
    def __init__(self,name="l'Univers",temps=[0], population = [], dt=0.01):
        self.name = name
        self.population=[]
        self.generateur = []
        self.dt = dt
        self.temps = temps
    
    
    def __str__(self):
        """fonction qui renvoie un string des attributs de la classe
        """
        return f"{self.name}: population={self.population}, generateur={self.generateur}, temps={self.temps}, dt={self.dt}"
    
    
    def getPopulation(self):
        """fonction qui print la population appartenant à l'univers
        """
        for p in self.population:
            print(p.name)


    def getTime(self):
        """fonction qui renvoie le temps courant
        """
        return self.temps[-1]
            
    
    def addAgent(self, *args):
        """fonction qui ajoute un agent à l'univers
        """
        for agent in args:
            self.population.append(agent)
    
    
    def addGenerateur(self,*args):
        """fonction qui ajoute un générateur de force 
        à l'univers
        """
        for generateur in args :
            self.generateur.append(generateur)  
    
    
    def getGenerateur(self):
        """fonction qui print les générateurs de force
        au sein de l'univers
        """
        for g in self.generateur :
            print(g)
        
        
    def simule(self):
        """fonction qui simule le mouvement des particules
        en faisant le calcul du PFD sur chaque particule
        """
        for p in self.population:
            somme_force = Vecteur3D()
            
            for g in self.generateur:
                somme_force = somme_force + g.setForce(p)
                
            p.PFD(somme_force)
            p.move(self.dt)
            
        self.temps.append(self.temps[-1]+self.dt)


    def plot2D(self):
        """fonction qui plot dans l'espace (x,y)
        """
        for p in self.population:
            p.plot2D()
        plt.show()  
    
    
    def plot3D(self):
        """fonction qui plot dans l'espace (x,y,z)
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for p in self.population:
            p.plot3D(ax)
        
        plt.show()  
    
    
    def simuleAll(self,Tf):
        """fonction qui simule toutes les particules durant un temps défini
        """
        while self.temps[-1]<Tf:
            self.simule()
            
            
    def axeTemps(self):
        """fonction qui renvoie le vecteur temporel
        """
        return self.temps
    
    
    def gameInit(self,W,H,fps=60,background=(0,0,0),scale=1):
        """fonction initialisant pygame
        """
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.background=background
        self.fps=fps
        self.scale=scale
        self.run=True
                
        pygame.display.set_caption(self.name)
        self.gameKeys = pygame.key.get_pressed()

        
    def gameUpdate(self):
        """fonction qui met à jour pygame
        """
        now = self.temps[-1]
        while self.temps[-1] < (now + (1/self.fps)):
            self.simule()
        
        font_obj = pygame.font.Font('freesansbold.ttf', 24)
        text_surface_obj = font_obj.render('Time: '+str(now)[:4] , True, 'black', self.background)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (25, 10)

        self.screen.fill(self.background)
        
        for p in self.population:
            p.gameDraw(self.screen,self.scale)
            
        self.screen.blit(text_surface_obj, (5,10))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        
        self.gameKeys = pygame.key.get_pressed()
        self.clock.tick(self.fps)
               

if __name__=="__main__": #false lors d'un import 
   
    particule = Particule()
    visc = Viscosite()
    gravite = gravite(Vecteur3D(1,1,1))
    
    univers = Univers()
    print(univers)
    
    univers.addAgent(particule)
    univers.addGenerateur(visc)
    univers.addGenerateur(gravite)
    
    univers.getPopulation()
    print(univers.getTime())
    
    univers.getGenerateur()
    univers.simule()
    print(univers)
    univers.simuleAll(1)
    print(univers)
    univers.plot2D()
    univers.plot3D()
    print(univers.axeTemps())
    univers.gameInit(100, 100)
    univers.gameUpdate()
    pygame.quit()        

    
    
    