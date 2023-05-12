#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 08:43:33 2023

@author: pofau
"""

###penser à aller dans le bon répertoire pour pouvoir avoir l'import
from class_vecteur3D import Vecteur3D

#Classe représentant un torseur 
class Torseur(Vecteur3D):

    #Initialisation de l'objet torseur
    def __init__(self, p=Vecteur3D(), r=Vecteur3D(), m=Vecteur3D()): #p : point d'application / R : résultante / M : moment
        self.p = p
        self.r = r
        self.m = m
    
    
    def __str__(self):
        return "torseur en ({}) = ({}, {})".format(self.p, self.r, self.m)

    def __repr__(self):
        rep = 'Torseur : \n' + '(R = ' + str(self.r.x) +'|' + str(self.r.y)  + '|' + str(self.r.z) + ') \n'
        rep += '(M = ' + str(self.m.x) +'|' + str(self.m.y)  + '|' + str(self.m.z) + ')'
        return rep    

    def chgPt(self, Po):
        MD = self.m + (self.p - Po) * self.r
        self.p = Po
        self.m = MD
        return (self)
        
    def __add__(self, other):
        Po = other.p
        other.chgPt(self.p)
        T = Torseur(self.p, self.r + other.r, self.m + other.m)
        other.chgPt(Po)
        return (T)
    
    def __sub__(self, other):
        return (self + (-other))
        
    def __neg__(self):
        return Torseur(self.p, -self.r, -self.m)
    
    def __eq__(self, other):
        p = other.p
        other.chgPt(self.p)
        test = self.r == other.r and self.m==other.m
        other.chgPt(p)
        return test


if __name__=="__main__": #false lors d'un import    
    V1 = Vecteur3D(1., 0., 0.)
    V2 = Vecteur3D(0., 1., 0.)
    V3 = Vecteur3D(0., 0., 1.)
    
    T1 = Torseur(V1, V1, V2)
    T2 = Torseur(V2, V1, V3)
    T3 = Torseur(V2, V2, V3)
    T4 = Torseur(V3, V1, V2)
    
    print(T1)
        
    T1.chgPt(V3)
    print(T1)
    
    T11 = T2 + T3
    print(T11)
    
    T12 = T2 - T3
    print(T12)
    
    T12 = -T12
    print(T12)


    

    