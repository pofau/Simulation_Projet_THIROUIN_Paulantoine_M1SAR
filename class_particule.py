#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:15:11 2023

@author: pofau
"""
# Importer les modules nécessaires
from class_vecteur3D import Vecteur3D
import matplotlib.pyplot as plt
from class_force import Viscosite
import pygame
from pylab import plot

###Class Particule
class Particule(object):
    """Objet Particule permettant de créer un objet dans l'espace 3D et simuler sa dynamique en fonction des efforts qui lui sont appliqués
    """
    
    def __init__(self, vitesse=Vecteur3D(), accel=Vecteur3D(),position=Vecteur3D(),masse=1,name='particule',color='blue', fixe = False, prisme = []):
        self.position=[position]
        self.name=name
        self.vitesse=[vitesse]
        self.accel=[accel]
        self.masse=masse
        self.color=color
        self.fixe = fixe #False or True
        self.prisme = prisme
        
        
    def __str__(self):
        """fonction retournant les attributs sous forme de string
        """
        return f"{self.name}: position={self.position[-1]}, vitesse={self.vitesse[-1]}, accel={self.accel[-1]}, masse={self.masse}, color={self.color}, fixe={self.fixe}"


    def __repr__(self):
        return f"Particule(name={self.name!r}, position={self.position[-1]}, vitesse={self.vitesse[-1]}, accel={self.accel[-1]}, masse={self.masse}, color={self.color}, fixe={self.fixe})"


    def __eq__(self, other):
        """fonction qui renvoie si deux objets sont identiques
        """
        if not isinstance(other, Particule):
            return False
        
        return (self.name == other.name and
                self.position == other.position and
                self.vitesse == other.vitesse and
                self.accel == other.accel and
                self.masse == other.masse and
                self.color == other.color and
                self.fixe == other.fixe)
    
    
    def axePosition(self, axe):
        """fonction qui renvoie l'axe demandé (X, Y, Z)
        """
        X = []
        if axe == 1:
            for p in self.position :
                X.append(p.x)
        elif axe == 2:
            for p in self.position :
                X.append(p.y)
        elif axe == 3:
            for p in self.position :
                X.append(p.z)
        return X


    def addPosition0(self, pos=Vecteur3D()):
        """fonction permettant d'ajouter une position initiale
        """
        self.position[0] = pos


    def setForce(self, f):
        """
        forcer la force pour la particule indépendamment des autres forces
        
        A UTILISER POUR LA GLISSIERE
        """
        self.accel.append((1/self.masse)*f)
        self.fixe = True

        
    def setSpeed(self, v):
        """imposer la vitesse et ignorer le PFD
        on met la vitesse imposer par l'utilsateur
        """
        self.accel.append(Vecteur3D())
        self.vitesse.append(v)
        self.fixe = True


    def setPosition(self, p):
        """imposer la position et ignorer le PFD
        et ignorer le setSpeed => on met à la position défini par l'utilsateur
        """
        self.accel.append(Vecteur3D())
        self.vitesse.append(Vecteur3D())
        self.position.append(p)
        self.fixe = True


    def getPosition(self):
        """fonction retournant la position courante
        """
        return self.position[-1]
    
    
    def getVitesse(self):
        """fonction retournant la vitesse courante
        """
        return self.vitesse[-1]    
    
    
    def getAcceleration(self):
        """fonction retournant l'accélération courante
        """
        return self.accel[-1]    
    
    
    def PFD(self, generateur):
        """Fonction calculant et incrémentant l'accélération en fonction du PFD,
        sauf si la particule est fixe dans l'espace ou bien selon un seul axe si la 
        liaison est prismatique
        """
        if self.fixe == True :
            self.accel.append(self.getAcceleration())
        
        elif self.fixe == False :
            self.accel.append((1/self.masse)*generateur)
        
        if len(self.prisme) > 0 :
            for p in self.prisme :
                axe = p.setForce()
                if axe.x == 0 :
                    self.accel[-1].x = 0
                if axe.y == 0 :
                    self.accel[-1].y = 0
                if axe.z == 0 :
                    self.accel[-1].z = 0
                    
                    
    def move(self, dt):
        """fonction qui intègre numériquement l'accélération et incrémente la position et la vitesse
        """
        self.position.append(self.getPosition() + self.getVitesse()*dt + (self.getAcceleration() * dt **2) * 0.5) 
        self.vitesse.append(self.getVitesse() + self.getAcceleration()*dt)


    def plot2D(self):
        """fonction qui plot dans l'espace (x,y)
        """
        X=[]
        Y=[]
        for p in self.position:
            X.append(p.x)
            Y.append(p.y)
        return plot(X, Y,color=self.color,label=self.name)
    
    
    def plot3D(self, ax):
        """fonction qui plot dans l'espace (x,y,z)
        """
        X=[]
        Y=[]
        Z=[]
        for p in self.position:
            X.append(p.x)
            Y.append(p.y)
            Z.append(p.z)
        return ax.plot(X, Y, Z,color=self.color,label=self.name)


    def gameDraw(self, screen, scale):
        """fonction qui dessine la particule dans pygame
        """
        screen_width, screen_height = screen.get_size()
        
        X = int(scale*self.position[-1].x)
        Y = screen_height - int((self.position[-1].y) * scale)
        
        vit = self.vitesse[-1]
        VX = int(scale*vit.x) + X
        VY = - int(scale*vit.y) + Y
        size=5
        
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))


if __name__=="__main__": #false lors d'un import    

    particule = Particule()
    print(particule)
    
    particule1 = Particule()
    if particule == particule1 :
        print("True")
    else :
        print("False")
        
    X = particule.axePosition(1)
    print(X)
    particule.addPosition0()

    particule.move(1)
    
    print(particule.getAcceleration())
    particule.setForce(Vecteur3D(1, 1, 1))
    print(particule.getAcceleration())

    print(particule.getVitesse())
    particule.setSpeed(Vecteur3D(1, 1, 1))
    print(particule.getVitesse())

    
    print(particule.getPosition())
    particule.setPosition(Vecteur3D(1, 1, 1))
    print(particule.getPosition())

    particule.move(1)

    visc = Viscosite()
    particule.PFD(visc)
    particule.move(10)
    
    particule.plot2D()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    particule.plot3D(ax)

